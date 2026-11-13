#!/usr/bin/env python3
"""Write docs/projects.md, the page listing the projects of the eclipse-csi GitHub organization.

The repositories come from the GitHub REST API (public ones only), their arrangement on the page from projects.toml.
A public repository that projects.toml does not list is still shown, under "Other projects", so that a new repository
appears on the site at the next build; the script warns about it (as an annotation when run by GitHub Actions). An
archived repository is never shown: it is no longer maintained.

Each project shows its metrics: stars, forks, contributors and latest release (GitHub API), last push, and the score of
the OpenSSF Scorecard (api.securityscorecards.dev) when the repository publishes one. The page shows their totals: the
project leads and committers of the Eclipse project (PMI, projects.eclipse.org), the contributors, counted once
across the projects, and the releases of the last 12 months (the current one included), month
by month. A metric that cannot be read is left out, with a warning: the page is still written.

The projects with GitHub Discussions get a link to them, and includes/discussions.md lists the discussions of the
organization and of its projects for docs/support.md.

Usage: python scripts/generate_projects.py [--config projects.toml] [--output docs/projects.md]

docs/projects.md is not versioned (.gitignore): it is written at every build. If the GitHub API cannot be read, the
file of the previous run is kept with a warning when there is one, as in a working copy, so that the site can be
previewed offline; otherwise the script fails. In CI, which starts from a fresh checkout, the build then stops and
GitHub Pages keeps serving the last site deployed.

The environment variable GITHUB_TOKEN (or GH_TOKEN) is optional: it only raises the rate limit of the API, which
the metrics need (two requests per project), and is only sent to the GitHub API.
Only the standard library is used, so that the script runs before anything is installed.
"""

from __future__ import annotations

import argparse
import datetime
import html
import json
import os
import re
import sys
import tomllib
import urllib.error
import urllib.request
from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# the GitHub Discussions of the organization and of its projects, inserted in docs/support.md (pymdownx.snippets)
DISCUSSIONS_INCLUDE = ROOT / "includes" / "discussions.md"
API = "https://api.github.com"
USER_AGENT = "eclipse-csi-website"
SCORECARD_API = "https://api.securityscorecards.dev/projects/github.com/{org}/{name}"
SCORECARD_VIEWER = "https://scorecard.dev/viewer/?uri=github.com/{org}/{name}"
PMI_API = "https://projects.eclipse.org/api/projects/{id}.json"
PMI_WHO = "https://projects.eclipse.org/projects/{id}/who"

# The GitHub Pages of the organization are served at csi.eclipse.dev, eclipse-csi.github.io redirects there.
PAGES_HOST = "https://eclipse-csi.github.io/"
SITE_HOST = "https://csi.eclipse.dev/"

DEFAULT_HOMEPAGE = {"title": "Documentation", "icon": "lucide/book-open"}
REPOSITORY_LINK = {"title": "Repository", "icon": "fontawesome/brands/github"}
DISCUSSIONS_LINK = {"title": "Discussions", "icon": "lucide/messages-square"}
MAX_TOPICS = 4
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


@dataclass
class Release:
    tag: str
    url: str
    date: datetime.date


@dataclass
class Activity:
    """What the contributors and the releases of a repository say about it."""

    contributors: set[str]
    releases: Counter[tuple[int, int]]  # by (year, month), for the last 12 months
    latest: Release | None


@dataclass
class Repository:
    name: str
    url: str
    description: str
    language: str | None
    topics: list[str]
    homepage: str | None
    archived: bool
    discussions: bool = False
    stars: int = 0
    forks: int = 0
    pushed: datetime.date | None = None
    links: list[dict] = field(default_factory=list)
    activity: Activity | None = None
    scorecard: float | None = None


def warn(message: str, level: str = "warning") -> None:
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::{level} title=projects.toml::{message}")
    else:
        print(f"{level}: {message}", file=sys.stderr)


def next_page(link_header: str | None) -> str | None:
    """The url of the next page from the Link header of a paginated response of the API."""
    for part in (link_header or "").split(","):
        match = re.match(r'\s*<([^>]+)>;\s*rel="next"', part)
        if match:
            return match.group(1)
    return None


def github_pages(url: str | None) -> Iterator[list[dict]]:
    """The pages of a list of the GitHub API, with the token when there is one (never sent elsewhere)."""
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28", "User-Agent": USER_AGENT}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    while url:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as response:
            body = response.read()
            url = next_page(response.headers.get("Link"))
        # an empty repository has no contributors: 204, without a body
        yield json.loads(body) if body else []


def fetch_repositories(org: str) -> list[dict]:
    repositories = [r for page in github_pages(f"{API}/orgs/{org}/repos?type=public&per_page=100&sort=full_name") for r in page]
    # type=public already excludes them, a private repository must never be listed even if the API changes
    return [repository for repository in repositories if not repository.get("private")]


def day(value: str) -> datetime.date:
    """The day of a time of the GitHub API (ISO 8601, in UTC)."""
    return datetime.datetime.fromisoformat(value).date()


def fetch_activity(org: str, name: str, since: datetime.date) -> Activity:
    """The contributors (people, not bots) and the releases (neither drafts nor pre-releases) of a repository."""
    contributors = {
        contributor["login"]
        for page in github_pages(f"{API}/repos/{org}/{name}/contributors?per_page=100")
        for contributor in page
        if contributor.get("type") != "Bot"
    }
    latest, releases = None, Counter()
    # the releases come newest first: the pages stop at the first one older than 12 months
    for page in github_pages(f"{API}/repos/{org}/{name}/releases?per_page=100"):
        for release in page:
            if release.get("draft") or release.get("prerelease") or not release.get("published_at"):
                continue
            published = day(release["published_at"])
            latest = latest or Release(tag=release["tag_name"], url=release["html_url"], date=published)
            if published >= since:
                releases[published.year, published.month] += 1
        if not page or day(page[-1]["created_at"]) < since:
            break
    return Activity(contributors=contributors, releases=releases, latest=latest)


@dataclass
class Team:
    """The project team of the Eclipse project, as the PMI lists it."""

    project_leads: int
    committers: int


def fetch_team(project_id: str) -> Team:
    request = urllib.request.Request(PMI_API.format(id=project_id), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    data = data[0] if isinstance(data, list) else data
    return Team(project_leads=len(data["project_leads"]), committers=len(data["committers"]))


def fetch_scorecard(org: str, name: str) -> float | None:
    """The OpenSSF Scorecard score of a repository, None when it publishes no results (most do not)."""
    request = urllib.request.Request(SCORECARD_API.format(org=org, name=name), headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return float(json.load(response)["score"])
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def site_url(url: str) -> str:
    return SITE_HOST + url.removeprefix(PAGES_HOST) if url.startswith(PAGES_HOST) else url


def to_repository(data: dict, extras: dict) -> Repository:
    homepage = (data.get("homepage") or "").strip() or None
    discussions = bool(data.get("has_discussions"))
    links = [{**REPOSITORY_LINK, "url": data["html_url"]}]
    # the GitHub Discussions of the repository, right after it, when they are enabled
    if discussions:
        links.append({**DISCUSSIONS_LINK, "url": data["html_url"] + "/discussions"})
    if homepage:
        links.append({**DEFAULT_HOMEPAGE, **extras.get("homepage", {}), "url": site_url(homepage)})
    links.extend(extras.get("links", []))
    description = (extras.get("description") or data.get("description") or "").strip()
    if description and description[-1] not in ".!?":
        description += "."
    return Repository(
        name=data["name"],
        url=data["html_url"],
        description=description,
        language=data.get("language"),
        topics=data.get("topics") or [],
        homepage=homepage,
        archived=bool(data.get("archived")),
        discussions=discussions,
        stars=data.get("stargazers_count") or 0,
        forks=data.get("forks_count") or 0,
        pushed=day(data["pushed_at"]) if data.get("pushed_at") else None,
        links=links,
    )


# --- rendering ---------------------------------------------------------------------------------------------------


def escape(text: str) -> str:
    """Text shown as is in Markdown: HTML is escaped, and so are the characters that would start markup."""
    return re.sub(r"([\\`*_\[\]{}#!])", r"\\\1", html.escape(text, quote=False))


def short_date(value: datetime.date) -> str:
    return f"{value.day} {MONTHS[value.month - 1]} {value.year}"


def count(number: int, noun: str) -> str:
    return f"{number} {noun}" + ("" if number == 1 else "s")


def metrics(repository: Repository, org: str) -> list[str]:
    """The metrics of a card, in Markdown: a star or a fork count of zero is left out."""
    def metric(name: str, text: str, title: str) -> str:
        return f'<span class="csi-metric" title="{title}">{icon(name)} {text}</span>'

    result = []
    if repository.stars:
        result.append(metric("lucide/star", count(repository.stars, "star"), "Stars on GitHub"))
    if repository.forks:
        result.append(metric("lucide/git-fork", count(repository.forks, "fork"), "Forks on GitHub"))
    if repository.activity:
        result.append(metric("lucide/users", count(len(repository.activity.contributors), "contributor"),
                             "Contributors, bots excluded"))
        if latest := repository.activity.latest:
            result.append(metric("lucide/tag", f"[{escape(latest.tag)}]({latest.url}) · {short_date(latest.date)}",
                                 "Latest release"))
    if repository.scorecard is not None:
        viewer = SCORECARD_VIEWER.format(org=org, name=repository.name)
        result.append(metric("lucide/shield-check", f"[Scorecard {repository.scorecard:.1f}/10]({viewer})",
                             "OpenSSF Scorecard score"))
    if repository.pushed:
        result.append(metric("lucide/history", f"Updated {short_date(repository.pushed)}", "Last push"))
    return result


def anchor(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def icon(name: str) -> str:
    return ":" + name.replace("/", "-") + ":"


def tags(repository: Repository) -> list[str]:
    """The tags of a card, in raw HTML (not parsed as Markdown)."""
    result = []
    if repository.language:
        result.append(f'<span class="csi-tag csi-tag--language">{html.escape(repository.language)}</span>')
    language = (repository.language or "").lower()
    topics = [topic for topic in repository.topics if topic != language][:MAX_TOPICS]
    result.extend(f'<span class="csi-tag">{html.escape(topic)}</span>' for topic in topics)
    return result


def card(repository: Repository, org: str) -> str:
    lines = [
        '<article class="csi-card" markdown>',
        "",
        f"### [{escape(repository.name)}]({repository.url}) {{ #{anchor(repository.name)} }}",
        "",
        escape(repository.description) if repository.description else "*No description.*",
        "",
    ]
    if card_metrics := metrics(repository, org):
        lines += [f'<p class="csi-card__metrics" markdown>{" ".join(card_metrics)}</p>', ""]
    if card_tags := tags(repository):
        lines += ['<p class="csi-card__tags">', *card_tags, "</p>", ""]
    links = " ".join(f"[{icon(link['icon'])} {escape(link['title'])}]({link['url']})" for link in repository.links)
    lines += [f'<p class="csi-card__links" markdown>{links}</p>', "", "</article>", ""]
    return "\n".join(lines)


def cards(repositories: list[Repository], org: str) -> str:
    return "\n".join(['<div class="csi-cards" markdown>', "", *(card(r, org) for r in repositories), "</div>", ""])


def last_months(today: datetime.date, count: int = 12) -> list[tuple[int, int]]:
    """The (year, month) of the last months, the current one included, the oldest first."""
    index = today.year * 12 + today.month - 1
    return [(year, month + 1) for year, month in (divmod(i, 12) for i in range(index - count + 1, index + 1))]


def month_name(month: tuple[int, int]) -> str:
    return f"{MONTHS[month[1] - 1]} {month[0]}"


def compact(number: int) -> str:
    """A figure as a stat tile shows it: 1,284 then 12.9K."""
    return f"{number:,}" if number < 10_000 else f"{number / 1000:.1f}K".replace(".0K", "K")


def sparkline(counts: list[int], months: list[tuple[int, int]]) -> list[str]:
    """The releases month by month: one bar per month, the current one in the accent, a month without any drawing
    none. The text of the chart is its accessible name; hovering a month gives its count."""
    top = max(counts) or 1
    summary = ", ".join(f"{month_name(month)}: {n}" for month, n in zip(months, counts))
    lines = [f'<div class="csi-spark" role="img" aria-label="Releases per month: {summary}">']
    for i, (month, n) in enumerate(zip(months, counts)):
        bar = ""
        if n:
            current = " csi-spark__bar--current" if i == len(counts) - 1 else ""
            bar = f'<span class="csi-spark__bar{current}" style="height: {max(n / top * 100, 8):.0f}%"></span>'
        lines.append(f'<span class="csi-spark__month" title="{month_name(month)}: {count(n, "release")}">{bar}</span>')
    return lines + ["</div>",
                    f'<p class="csi-kpi__axis"><span>{month_name(months[0])}</span>'
                    f"<span>{month_name(months[-1])}</span></p>"]


def kpi(icon_name: str, value: int, label: str, caption: str, trend: list[str] | None = None) -> list[str]:
    """A stat tile: its icon, its figure, its label, a caption in Markdown and an optional trend, beside them in a
    tile twice as wide."""
    lines = [f'<div class="csi-kpi{" csi-kpi--wide" if trend else ""}" markdown>', "",
             f'<p class="csi-kpi__icon" markdown>{icon(icon_name)}</p>', "",
             '<div class="csi-kpi__body" markdown>', "",
             f'<p class="csi-kpi__value">{compact(value)}</p>', "",
             f'<p class="csi-kpi__label">{html.escape(label)}</p>', "",
             f'<p class="csi-kpi__caption" markdown>{caption}</p>', "",
             "</div>", ""]
    if trend:
        lines += ['<div class="csi-kpi__trend">', *trend, "</div>", ""]
    return lines + ["</div>", ""]


def join() -> list[str]:
    """The invitation to join the team, beside its figures: how a contributor becomes a committer."""
    return [
        '<div class="csi-join" markdown>', "",
        '<p class="csi-join__title" markdown>:lucide-user-plus: Join the team</p>', "",
        '<p class="csi-join__text">Every committer started as a contributor: contribute regularly, and the '
        "committers can elect you, by a public vote.</p>", "",
        '<p class="csi-join__links" markdown>[:lucide-arrow-right: How to contribute](contribute.md) '
        "[:lucide-vote: How elections work](contribute.md#committer)</p>", "",
        "</div>", "",
    ]


def kpis(shown: list[Repository], areas: int, months: list[tuple[int, int]], team: Team | None,
         who: str) -> list[str]:
    """The totals of the page, in two rows: the activity of the projects, then their team and how to join it. The
    contributors and the releases are shown only when the metrics of every project were read, the project leads and
    committers when the PMI was."""
    complete = bool(shown) and all(repository.activity for repository in shown)
    lines = ['<p class="csi-kpis__title">Activity</p>', "", '<div class="csi-kpis" markdown>', ""]
    lines += kpi("lucide/boxes", len(shown), "Projects", f"in {count(areas, 'area')}")
    if complete:
        counts = [sum(repository.activity.releases[month] for repository in shown) for month in months]
        lines += kpi("lucide/tag", sum(counts), "Releases", "in the last 12 months", sparkline(counts, months))
    lines += kpi("lucide/star", sum(repository.stars for repository in shown), "GitHub stars", "across the projects")
    lines += ["</div>", "", '<p class="csi-kpis__title">Team</p>', "", '<div class="csi-kpis" markdown>', ""]
    if team:
        lines += kpi("lucide/crown", team.project_leads, "Project leads", "elected among the committers")
        lines += kpi("lucide/key-round", team.committers, "Committers", f"elected by their peers · [who]({who})")
    if complete:
        contributors = set().union(*(repository.activity.contributors for repository in shown))
        lines += kpi("lucide/users", len(contributors), "Contributors", "on GitHub, bots excluded")
    return lines + join() + ["</div>", ""]


@dataclass
class Space:
    """A space of GitHub Discussions: the one of the organization, or the one of a project."""

    name: str
    url: str
    description: str


def discussion_spaces(org: str, repositories: dict[str, Repository], shown: list[Repository]) -> list[Space]:
    """The organization first, when its discussions are enabled (they are those of its .github repository), then the
    projects that have their own, in the order of the page."""
    spaces = []
    if (profile := repositories.get(".github")) and profile.discussions:
        spaces.append(Space(org, f"https://github.com/orgs/{org}/discussions",
                            "Eclipse CSI as a whole, or a topic across several projects."))
    return spaces + [Space(r.name, r.url + "/discussions", r.description) for r in shown if r.discussions]


def discussions_callout(spaces: list[Space]) -> list[str]:
    """The invitation of the projects page to ask in the discussions, below its figures."""
    if not spaces:
        return []
    links = ", ".join(f"[{escape(space.name)}]({space.url})" for space in spaces)
    return ['!!! question "Questions, ideas, feedback?"', "",
            f"    Ask them in GitHub Discussions: {links}. The [Support](support.md) page lists the other channels.", ""]


def render_discussions(org: str, spaces: list[Space]) -> str:
    """The cards of the discussions, for docs/support.md."""
    out = ["<!-- Written by scripts/generate_projects.py (the GitHub Discussions of the organization and of its "
           "projects): do not edit. -->", ""]
    if not spaces:
        return "\n".join(out + [f"None of the projects of [{org}](https://github.com/{org}) has discussions yet.", ""])
    out += ['<div class="csi-cards csi-cards--compact" markdown>', ""]
    for space in spaces:
        out += ['<article class="csi-card" markdown>', "", ":lucide-messages-square:{ .csi-card__icon }", "",
                f"### [{escape(space.name)}]({space.url})", "", escape(space.description), "",
                f'<p class="csi-card__links" markdown>[:lucide-arrow-right: Open the discussions]({space.url})</p>',
                "", "</article>", ""]
    return "\n".join(out + ["</div>", ""])


def render(config: dict, repositories: dict[str, Repository], months: list[tuple[int, int]],
           team: Team | None) -> tuple[str, str]:
    """The projects page, and the cards of the discussions for the support page."""
    org = config["org"]
    # an archived repository is no longer maintained: it is left out of the page, wherever projects.toml lists it
    archived = {name for name, repository in repositories.items() if repository.archived}
    repositories = {name: repository for name, repository in repositories.items() if not repository.archived}
    organization = [name for name in config.get("organization", []) if name in repositories]

    listed: set[str] = set()
    areas = []
    for area in config["areas"]:
        members = []
        for name in area["repositories"]:
            if name in listed:
                warn(f"{name} is listed by more than one area, only the first one shows it")
            elif name in archived:
                warn(f"{name} (area {area['id']}) is archived, it is not shown: remove it from projects.toml")
            elif name not in repositories:
                warn(f"{name} (area {area['id']}) is not a public repository of {org}, it is not shown")
            else:
                members.append(repositories[name])
            listed.add(name)
        if members:
            areas.append((area, members))

    others = sorted(
        (r for r in repositories.values() if r.name not in listed and r.name not in organization),
        key=lambda r: r.name.lower(),
    )
    for repository in others:
        warn(f"{repository.name} is in no area of projects.toml, it is shown under 'Other projects'")
    if others:
        areas.append(({"id": "other", "title": "Other projects",
                       "description": "Projects that are not yet sorted into an area."}, others))

    shown = [repository for _, members in areas for repository in members]
    spaces = discussion_spaces(org, repositories, shown)
    projects = len(shown)
    description = (f"The {projects} projects of Eclipse CSI, the Eclipse Common Security Infrastructure: tools and "
                   "services that secure the software supply chain of Eclipse Foundation projects.")
    out = [
        "---",
        "title: Projects",
        # a JSON string is a valid YAML scalar, whatever it contains
        f"description: {json.dumps(description)}",
        "hide:",
        "  - navigation",
        "---",
        "",
        "<!-- Written by scripts/generate_projects.py from projects.toml and the GitHub API: do not edit. -->",
        "",
        "# Projects",
        "",
        f"Eclipse CSI develops its tools in the open, in the [{org}](https://github.com/{org}) GitHub organization. "
        "They are released under the Eclipse Public License 2.0 unless stated otherwise in their repository, and "
        "contributions are welcome. They support the [security services of the Eclipse Foundation]"
        "(https://www.eclipse.org/security/): vulnerability reporting and advisories, repository and infrastructure "
        "security, code signing.",
        "{ .csi-lead }",
        "",
        *kpis(shown, len(areas), months, team, PMI_WHO.format(id=config["pmi"])),
        *discussions_callout(spaces),
    ]
    for area, members in areas:
        out += [f"## {escape(area['title'])} {{ #{area['id']} }}", "", area["description"].strip(),
                "{ .csi-area-lead }", "", cards(members, org)]
    if organization:
        out += ["## About this organization { #organization }", "",
                "The repositories that run the organization itself.", "{ .csi-area-lead }", "",
                "| Repository | Purpose |", "| --- | --- |"]
        for name in organization:
            repository = repositories[name]
            purpose = escape(repository.description).replace("|", r"\|") or "–"
            out.append(f"| [{escape(name)}]({repository.url}) | {purpose} |")
        out.append("")
    return "\n".join(out), render_discussions(org, spaces)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", type=Path, default=ROOT / "projects.toml")
    parser.add_argument("--output", type=Path, default=ROOT / "docs" / "projects.md")
    args = parser.parse_args()

    config = tomllib.loads(args.config.read_text(encoding="utf-8"))
    extras = config.get("repositories", {})
    # the files of a previous run are kept only together: docs/support.md inserts the discussions
    previous = args.output.exists() and DISCUSSIONS_INCLUDE.exists()
    # OSError: the API cannot be reached or answers an error; ValueError: what it answers cannot be read
    try:
        found = fetch_repositories(config["org"])
    except (OSError, ValueError) as error:
        if previous:
            warn(f"the GitHub API cannot be read ({error}); the file of the previous run is kept")
            return 0
        warn(f"the GitHub API cannot be read ({error}); there is no file of a previous run to keep", "error")
        return 1
    repositories = {data["name"]: to_repository(data, extras.get(data["name"], {})) for data in found}

    # the metrics of the projects (neither archived nor of the organization itself): a source that cannot be read
    # keeps the page of the previous run when there is one (a working copy), otherwise leaves its metrics out: in CI,
    # which starts from a fresh checkout, the page is still written
    unread = []
    organization = set(config.get("organization", []))
    projects = [r for r in repositories.values() if not r.archived and r.name not in organization]
    months = last_months(datetime.datetime.now(datetime.UTC).date())
    since = datetime.date(*months[0], 1)
    try:
        activities = {r.name: fetch_activity(config["org"], r.name, since) for r in projects}
    except (OSError, ValueError, KeyError) as error:
        unread.append(f"the contributors and releases ({error})")
    else:
        for repository in projects:
            repository.activity = activities[repository.name]
    try:
        scores = {r.name: fetch_scorecard(config["org"], r.name) for r in projects}
    except (OSError, ValueError, KeyError) as error:
        unread.append(f"the OpenSSF Scorecard scores ({error})")
    else:
        for repository in projects:
            repository.scorecard = scores[repository.name]
    try:
        team = fetch_team(config["pmi"])
    except (OSError, ValueError, KeyError) as error:
        team = None
        unread.append(f"the project leads and committers of the PMI ({error})")
    if unread and previous:
        warn(f"cannot read {'; '.join(unread)}: the page of the previous run is kept (set GITHUB_TOKEN to raise the "
             "rate limit of the GitHub API)")
        return 0
    for what in unread:
        warn(f"cannot read {what}: the page is written without it")
    page, discussions = render(config, repositories, months, team)
    args.output.write_text(page, encoding="utf-8")
    DISCUSSIONS_INCLUDE.parent.mkdir(parents=True, exist_ok=True)
    DISCUSSIONS_INCLUDE.write_text(discussions, encoding="utf-8")
    print(f"{args.output.relative_to(ROOT) if args.output.is_relative_to(ROOT) else args.output}: "
          f"{len(repositories)} public repositories of {config['org']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
