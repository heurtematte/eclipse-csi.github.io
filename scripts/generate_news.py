#!/usr/bin/env python3
"""Write the blog and events pages of the site, and the news of its home page.

- docs/blog.md: the posts of blogs.eclipse.org that have one of the tags of news.toml, read from the RSS feed of each
  tag, which holds its 10 latest posts. A post whose title names an incident (the keywords of news.toml) is marked so.
- docs/events.md: the events of the Eclipse Foundation newsroom published to the channel of news.toml, read from its
  API. An event is upcoming until its last day included.
- includes/news.md: the news of the home page, in three columns: the latest CVEs that the Eclipse Foundation published
  as the CVE Numbering Authority of its projects (api.eclipse.org/cve), the latest posts, and the events.

docs/index.md inserts includes/news.md with pymdownx.snippets (zensical.toml). The files are not versioned (.gitignore):
they are written at every build. A source that cannot be read keeps the files of the previous run with a warning when
there are some, as in a working copy, so that the site can be previewed offline; otherwise the script fails. In CI,
which starts from a fresh checkout, the build then stops and GitHub Pages keeps serving the last site deployed.

Usage: python scripts/generate_news.py [--config news.toml] [--today YYYY-MM-DD]

Only the standard library is used, so that the script runs before anything is installed.
"""

from __future__ import annotations

import argparse
import datetime
import email.utils
import html
import json
import os
import sys
import tomllib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from itertools import groupby
from pathlib import Path

# the text of a source is escaped in Markdown exactly as on the projects page
from generate_projects import escape

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INCLUDES = ROOT / "includes"

BLOGS = "https://blogs.eclipse.org"
EVENTS_API = "https://newsroom.eclipse.org/api/events"
CVE_API = "https://api.eclipse.org/cve"
CVE_RECORD = "https://www.cve.org/CVERecord?id={id}"
KNOWN_VULNERABILITIES = "https://www.eclipse.org/security/known/"
PMI_API = "https://projects.eclipse.org/api/projects/{id}.json"
PMI_PROJECT = "https://projects.eclipse.org/projects/{id}"
USER_AGENT = "eclipse-csi-website"
DC = "{http://purl.org/dc/elements/1.1/}"

SUMMARY_LENGTH = 220
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December")
# the severity of a CVE from its CVSS base score, as the CVSS v3 and v4 specifications rate it
SEVERITIES = ((9.0, "Critical"), (7.0, "High"), (4.0, "Medium"), (0.1, "Low"))
# the part of the Eclipse Foundation in an event (ef_participation in the newsroom API), as shown on its card
PARTICIPATION = {"ef_speaking": "Speaking", "ef_attending": "Attending", "ef_event": "Eclipse Foundation event"}
# an event where only member organizations of the Eclipse Foundation take part: the team is not there
NOT_SHOWN = {"member_org_participating"}
# the elements that separate words in the text of an HTML fragment
BLOCKS = {"p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre", "table", "tr",
          "td", "th"}


@dataclass
class Tag:
    name: str  # as in the URL of its page, blogs.eclipse.org/blog-tags/<name>
    title: str  # as shown by blogs.eclipse.org
    page: str
    feed: str


@dataclass
class Post:
    title: str
    url: str
    author: str
    date: datetime.date
    summary: str
    incident: bool = False


@dataclass
class Cve:
    id: str
    url: str
    date: datetime.date
    project: str  # its name, or its id when the PMI does not give it
    project_url: str
    score: float | None


@dataclass
class Event:
    title: str
    url: str | None
    registration: str | None
    start: datetime.date
    end: datetime.date
    place: str
    online: bool
    participation: str | None
    summary: str


def warn(message: str, level: str = "warning") -> None:
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::{level} title=news::{message}")
    else:
        print(f"{level}: {message}", file=sys.stderr)


def keep(paths: list[Path], reason: str) -> bool:
    """After a source failed for the reason given, whether the files of the previous run are there to be kept."""
    if all(path.exists() for path in paths):
        warn(f"{reason}; the files of the previous run are kept")
        return True
    warn(f"{reason}; there are no files of a previous run to keep", "error")
    return False


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


# --- the text of the sources -------------------------------------------------------------------------------------


class FeedLink(HTMLParser):
    """The RSS feed that a page announces: <link rel="alternate" type="application/rss+xml" href="…">."""

    def __init__(self) -> None:
        super().__init__()
        self.href: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if (tag == "link" and self.href is None and attributes.get("type") == "application/rss+xml"
                and "alternate" in (attributes.get("rel") or "").split()):
            self.href = attributes.get("href")


class Text(HTMLParser):
    """The text of an HTML fragment, or only of its <div> of the given class (the body of a post in its feed item)."""

    def __init__(self, div_class: str | None = None) -> None:
        super().__init__()
        self.div_class = div_class
        self.depth = 0  # inside the <div> of the class: its depth, counting the <div> nested in it
        self.parts: list[str] = []

    def capturing(self) -> bool:
        return self.div_class is None or self.depth > 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "div" and self.div_class:
            if self.depth:
                self.depth += 1
            elif self.div_class in (dict(attrs).get("class") or "").split():
                self.depth = 1
        if tag in BLOCKS and self.capturing():
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        if tag in BLOCKS and self.capturing():
            self.parts.append(" ")
        if tag == "div" and self.depth:
            self.depth -= 1

    def handle_data(self, data: str) -> None:
        if self.capturing():
            self.parts.append(data)


def text_of(fragment: str, div_class: str | None = None) -> str:
    parser = Text(div_class)
    parser.feed(fragment)
    parser.close()
    return " ".join("".join(parser.parts).split())


def shorten(text: str, width: int = SUMMARY_LENGTH) -> str:
    if len(text) <= width:
        return text
    return text[: width + 1].rsplit(" ", 1)[0].rstrip(" ,;:.-–—") + "…"


def safe_url(url: object) -> str | None:
    """A URL of a source as the target of a link: http(s) only, with the characters that would end the link encoded.
    The newsroom API gives false rather than null for a missing URL."""
    if not isinstance(url, str) or urllib.parse.urlsplit(url.strip()).scheme not in {"http", "https"}:
        return None
    return urllib.parse.quote(url.strip(), safe=":/?#[]@!$&'*+,;=%~")


# --- the sources -------------------------------------------------------------------------------------------------


def to_post(item: ET.Element) -> Post | None:
    url = safe_url(item.findtext("link"))
    title = " ".join((item.findtext("title") or "").split())
    published = item.findtext("pubDate")
    if not (url and title and published):
        return None
    description = item.findtext("description") or ""
    return Post(
        title=title,
        url=url,
        author=" ".join((item.findtext(f"{DC}creator") or "").split()),
        date=email.utils.parsedate_to_datetime(published).date(),
        summary=shorten(text_of(description, "field--name-body") or text_of(description)),
    )


def fetch_posts(names: list[str]) -> tuple[list[Tag], list[Post]]:
    """The tags, and their posts newest first: a post with several of the tags is listed once."""
    tags: list[Tag] = []
    posts: dict[str, Post] = {}
    for name in names:
        page = f"{BLOGS}/blog-tags/{urllib.parse.quote(name)}"
        link = FeedLink()
        link.feed(fetch(page).decode("utf-8", "replace"))
        if not link.href:
            raise ValueError(f"{page} announces no RSS feed")
        feed = urllib.parse.urljoin(page, link.href)
        channel = ET.fromstring(fetch(feed)).find("channel")
        if channel is None:
            raise ValueError(f"{feed} is not an RSS feed")
        tags.append(Tag(name=name, title=" ".join((channel.findtext("title") or name).split()), page=page, feed=feed))
        for post in filter(None, map(to_post, channel.findall("item"))):
            posts.setdefault(post.url, post)
    return tags, sorted(posts.values(), key=lambda post: (post.date, post.title), reverse=True)


def day(value: object) -> datetime.date | None:
    """The day of a time of the newsroom API: ISO 8601, in UTC."""
    return datetime.datetime.fromisoformat(value).date() if isinstance(value, str) and value else None


def to_event(data: dict) -> Event | None:
    title = " ".join((data.get("title") or "").split())
    start = day(data.get("date"))
    if not title or not start or data.get("ef_participation") in NOT_SHOWN:
        return None
    attendance = data.get("attendance_type")
    # the city when there is one: the name of the venue alone does not say where it is
    city = ((data.get("address") or {}).get("city") or "").strip()
    place = "" if attendance == "virtual" else city or " ".join((data.get("locationName") or "").split())
    return Event(
        title=title,
        url=safe_url(data.get("infoLink")),
        registration=safe_url(data.get("registration")),
        start=start,
        end=max(day(data.get("end-date")) or start, start),
        place=place,
        online=attendance in {"virtual", "hybrid"},
        participation=PARTICIPATION.get(data.get("ef_participation")),
        summary=shorten(text_of(data.get("description") or "")),
    )


def fetch_events(channel: str) -> list[Event]:
    """The events published to the channel, the earliest first. The pages of the API are numbered from 1."""
    events: list[Event] = []
    page, pages = 1, 1
    while page <= pages:
        query = urllib.parse.urlencode({"parameters[publish_to]": channel, "pagesize": 100, "page": page})
        data = json.loads(fetch(f"{EVENTS_API}?{query}"))
        events.extend(filter(None, map(to_event, data["events"])))
        pages = min(int(data["pager"]["total_pages"]), 50)
        page += 1
    return sorted(events, key=lambda event: (event.start, event.end, event.title))


def cve_order(item: dict) -> tuple:
    """The latest first: by date of publication, then by number (CVE-2026-123059 after CVE-2026-89292)."""
    parts = item["id"].split("-")
    number = (int(parts[1]), int(parts[2])) if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit() else (0, 0)
    return item["date_published"], number


def project_name(project_id: str) -> str:
    data = json.loads(fetch(PMI_API.format(id=urllib.parse.quote(project_id))))
    data = data[0] if isinstance(data, list) else data
    return " ".join((data.get("name") or project_id).split())


def fetch_cves(count: int) -> list[Cve]:
    """The latest public CVEs of Eclipse projects. The name of their project comes from the PMI: if it cannot be read,
    the id of the project is shown instead."""
    items = [item for item in json.loads(fetch(CVE_API))
             if item.get("status") == "PUBLIC" and item.get("id") and item.get("date_published")]
    names: dict[str, str] = {}
    cves = []
    for item in sorted(items, key=cve_order, reverse=True)[:count]:
        project = (item.get("project") or "").strip()
        if project and project not in names:
            try:
                names[project] = project_name(project)
            except (OSError, ValueError, SyntaxError, KeyError):
                names[project] = project
        score = item.get("cvss")
        cves.append(Cve(
            id=item["id"],
            url=CVE_RECORD.format(id=urllib.parse.quote(item["id"])),
            date=datetime.date.fromisoformat(item["date_published"][:10]),
            project=names.get(project, project),
            project_url=PMI_PROJECT.format(id=urllib.parse.quote(project)) if project else "",
            score=float(score) if isinstance(score, (int, float)) and not isinstance(score, bool) else None,
        ))
    return cves


def severity(score: float | None) -> str | None:
    return next((name for floor, name in SEVERITIES if score is not None and score >= floor), None)


# --- rendering ---------------------------------------------------------------------------------------------------


def long_date(value: datetime.date, year: bool = True) -> str:
    text = f"{value.day} {MONTHS[value.month - 1]}"
    return f"{text} {value.year}" if year else text


def dates(start: datetime.date, end: datetime.date, year: bool = True) -> str:
    if end == start:
        return long_date(start, year)
    if (start.year, start.month) == (end.year, end.month):
        return f"{start.day}–{long_date(end, year)}"
    if start.year == end.year:
        return f"{long_date(start, False)} – {long_date(end, year)}"
    return f"{long_date(start)} – {long_date(end)}"


def icon(name: str) -> str:
    return ":" + name.replace("/", "-") + ":"


def links(items: list[tuple[str, str, str]], css: str = "csi-card__links") -> str:
    """A row of links, each (icon, text, url)."""
    return f'<p class="{css}" markdown>' + " ".join(f"[{icon(i)} {escape(t)}]({u})" for i, t, u in items) + "</p>"


def card(title: str, url: str | None, meta: list[str], summary: str, tag: str | None = None,
         actions: list[tuple[str, str, str]] | None = None, tag_css: str = "csi-tag--accent") -> str:
    """A card: its title, a line of facts (each in Markdown, with its icon), a summary, a tag and links."""
    lines = [
        '<article class="csi-card" markdown>',
        "",
        f"### [{escape(title)}]({url})" if url else f"### {escape(title)}",
        "",
        f'<p class="csi-card__meta" markdown>{" · ".join(meta)}</p>',
        "",
    ]
    if summary:
        lines += [escape(summary), ""]
    if tag:
        lines += [f'<p class="csi-card__tags"><span class="csi-tag {tag_css}">{html.escape(tag)}</span></p>', ""]
    if actions:
        lines += [links(actions), ""]
    return "\n".join([*lines, "</article>", ""])


def cards(items: list[str]) -> str:
    return "\n".join(['<div class="csi-cards" markdown>', "", *items, "</div>", ""])


def post_card(post: Post) -> str:
    meta = [f":lucide-calendar: {long_date(post.date)}"]
    if post.author:
        meta.append(f":lucide-user: {escape(post.author)}")
    return card(post.title, post.url, meta, post.summary, "Security incident" if post.incident else None,
                [("lucide/arrow-right", "Read the post", post.url)], "csi-tag--incident")


def where(event: Event) -> list[str]:
    result = [f":lucide-map-pin: {escape(event.place)}"] if event.place else []
    return result + [":lucide-video: Online"] if event.online else result


def event_card(event: Event) -> str:
    actions = []
    if event.url:
        actions.append(("lucide/globe", "Event website", event.url))
    if event.registration and event.registration != event.url:
        actions.append(("lucide/ticket", "Register", event.registration))
    return card(event.title, event.url, [f":lucide-calendar: {dates(event.start, event.end)}", *where(event)],
                event.summary, event.participation, actions)


def past_event(event: Event) -> str:
    """An event of the list of past events, under the heading of its year."""
    title = f"[{escape(event.title)}]({event.url})" if event.url else escape(event.title)
    place = " and ".join(filter(None, [escape(event.place), "online" if event.online and event.place else
                                       "Online" if event.online else ""]))
    line = " · ".join(filter(None, [f"**{dates(event.start, event.end, year=False)}**", title, place]))
    if event.participation:
        line += f' <span class="csi-tag">{html.escape(event.participation)}</span>'
    return f"- {line}"


def front_matter(title: str, description: str, source: str) -> list[str]:
    return [
        "---",
        f"title: {title}",
        # a JSON string is a valid YAML scalar, whatever it contains
        f"description: {json.dumps(description)}",
        "hide:",
        "  - navigation",
        "  - toc",
        "---",
        "",
        f"<!-- Written by scripts/generate_news.py from news.toml and {source}: do not edit. -->",
        "",
    ]


def tag_names(tags: list[Tag]) -> str:
    names = [tag.title for tag in tags]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " or " + names[-1]


def render_blog(tags: list[Tag], posts: list[Post]) -> str:
    out = front_matter(
        "Blog",
        f"Security news and advice from the Eclipse Foundation blog: the posts tagged {tag_names(tags)}, by the "
        "Eclipse Foundation Security Team and others.",
        "blogs.eclipse.org",
    )
    out += [
        "# Blog",
        "",
        "News and advice on the security of open source projects from the "
        f"[Eclipse Foundation blog]({BLOGS}), by the Eclipse Foundation Security Team and others: the latest posts "
        f"tagged {escape(tag_names(tags))}.",
        "{ .csi-lead }",
        "",
        links([("lucide/rss", f"RSS feed: {tag.title}", tag.feed) for tag in tags], "csi-links"),
        "",
        cards(list(map(post_card, posts))) if posts else "No post yet.\n",
        "Older posts are on blogs.eclipse.org: "
        + ", ".join(f"[{escape(tag.title)}]({tag.page})" for tag in tags) + ".",
        "{ .csi-area-lead }",
        "",
    ]
    return "\n".join(out)


def meta(*parts: str) -> str:
    """The facts of an entry of the news, on the line below it."""
    return f' <span class="csi-news__meta">{" · ".join(filter(None, parts))}</span>'


def cve_entry(cve: Cve) -> str:
    """A CVE: its severity (a label with its score, never the color alone), its id and its project."""
    level = severity(cve.score)
    badge = f'<span class="csi-sev csi-sev--{level.lower()}">{level} {cve.score:.1f}</span> ' if level else ""
    project = f"[{escape(cve.project)}]({cve.project_url})" if cve.project_url else escape(cve.project)
    return f"- {badge}[{cve.id}]({cve.url}){meta(project, long_date(cve.date))}"


def post_entry(post: Post) -> str:
    badge = ' <span class="csi-tag csi-tag--incident">Security incident</span>' if post.incident else ""
    return f"- [{escape(post.title)}]({post.url}){badge}{meta(long_date(post.date), escape(post.author))}"


def event_entry(event: Event, today: datetime.date) -> str:
    """An event: the upcoming ones with the part of the Eclipse Foundation, the past ones marked so."""
    title = f"[{escape(event.title)}]({event.url})" if event.url else escape(event.title)
    label = event.participation if event.end >= today else "Past"
    badge = f' <span class="csi-tag{" csi-tag--accent" if event.end >= today else ""}">{html.escape(label)}</span>' \
        if label else ""
    place = escape(event.place) or ("Online" if event.online else "")
    return f"- {title}{badge}{meta(dates(event.start, event.end), place)}"


def news_column(icon_name: str, title: str, entries: list[str], empty: str, more: tuple[str, str]) -> list[str]:
    """A column of the news: its title, its entries, and the link to all of them."""
    return [
        '<section class="csi-news__column" markdown>', "",
        f'<p class="csi-news__title" markdown>{icon(icon_name)} {escape(title)}</p>', "",
        *(entries or [empty]), "",
        f'<p class="csi-news__more" markdown>[:lucide-arrow-right: {escape(more[0])}]({more[1]})</p>', "",
        "</section>", "",
    ]


def render_news(cves: list[Cve], posts: list[Post], events: list[Event], today: datetime.date,
                counts: dict[str, int]) -> str:
    """The news of the home page: the latest CVEs, the latest posts, and the events, the upcoming ones first, then the
    latest past ones up to their number."""
    upcoming = [event for event in events if event.end >= today]
    past = sorted((event for event in events if event.end < today), key=lambda e: (e.end, e.start), reverse=True)
    shown_events = (upcoming + past)[: counts["events"]]
    return "\n".join([
        "<!-- Written by scripts/generate_news.py (the news of the home page): do not edit. -->", "",
        '<div class="csi-news" markdown>', "",
        *news_column("lucide/shield-alert", "Latest CVEs", list(map(cve_entry, cves[: counts["cves"]])),
                     "No CVE yet.", ("All the known vulnerabilities", KNOWN_VULNERABILITIES)),
        *news_column("lucide/newspaper", "Latest posts", list(map(post_entry, posts[: counts["posts"]])),
                     "No post yet.", ("All the posts", "blog.md")),
        *news_column("lucide/calendar", "Events", [event_entry(event, today) for event in shown_events],
                     "No event yet.", ("All the events", "events.md")),
        "</div>", "",
    ])


def render_events(events: list[Event], today: datetime.date) -> str:
    upcoming = [event for event in events if event.end >= today]
    past = sorted((event for event in events if event.end < today), key=lambda e: (e.start, e.end), reverse=True)
    out = front_matter(
        "Events",
        "The conferences, trainings and webinars where the Eclipse Foundation Security Team speaks or takes part.",
        "the Eclipse Foundation newsroom",
    )
    out += [
        "# Events",
        "",
        "Where to meet the Eclipse Foundation Security Team: the conferences, trainings and webinars where it speaks "
        "or takes part, as announced by the [Eclipse Foundation](https://www.eclipse.org/events/).",
        "{ .csi-lead }",
        "",
        "## Upcoming events { #upcoming }",
        "",
        cards(list(map(event_card, upcoming))) if upcoming else "No upcoming event is announced yet.\n",
    ]
    if past:
        out += ["## Past events { #past }", ""]
        for year, group in groupby(past, key=lambda event: event.start.year):
            out += [f"### {year} {{ #past-{year} }}", "", '<div class="csi-past" markdown>', "",
                    *map(past_event, group), "", "</div>", ""]
    return "\n".join(out)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", type=Path, default=ROOT / "news.toml")
    parser.add_argument("--today", type=datetime.date.fromisoformat,
                        default=datetime.datetime.now(datetime.UTC).date(),
                        help="the day that splits the upcoming and past events (default: today, in UTC)")
    args = parser.parse_args()
    config = tomllib.loads(args.config.read_text(encoding="utf-8"))
    blog, events = config["blog"], config["events"]
    keywords = [keyword.lower() for keyword in blog.get("incident_keywords", [])]

    # OSError: the source cannot be reached or answers an error; ValueError, SyntaxError: what it answers cannot be read
    kept = True
    unread = []
    posts = found = cves = None
    try:
        tags, posts = fetch_posts(blog["tags"])
    except (OSError, ValueError, SyntaxError) as error:
        unread.append(f"blogs.eclipse.org ({error})")
        kept &= keep([DOCS / "blog.md"], f"blogs.eclipse.org cannot be read ({error})")
    else:
        for post in posts:
            post.incident = any(keyword in post.title.lower() for keyword in keywords)
        write(DOCS / "blog.md", render_blog(tags, posts))
        print(f"docs/blog.md: {len(posts)} posts tagged {', '.join(blog['tags'])}")

    try:
        found = fetch_events(events["channel"])
    except (OSError, ValueError, SyntaxError) as error:
        unread.append(f"the newsroom ({error})")
        kept &= keep([DOCS / "events.md"], f"the newsroom of the Eclipse Foundation cannot be read ({error})")
    else:
        write(DOCS / "events.md", render_events(found, args.today))
        upcoming = sum(event.end >= args.today for event in found)
        print(f"docs/events.md: {upcoming} upcoming and {len(found) - upcoming} past events of {events['channel']}")

    try:
        cves = fetch_cves(config["cves"]["home"])
    except (OSError, ValueError, SyntaxError, KeyError) as error:
        unread.append(f"the CVEs of api.eclipse.org ({error})")

    # the news of the home page are written only from the three sources
    if posts is not None and found is not None and cves is not None:
        counts = {"cves": config["cves"]["home"], "posts": blog["home"], "events": events["home"]}
        write(INCLUDES / "news.md", render_news(cves, posts, found, args.today, counts))
        print(f"includes/news.md: {len(cves)} CVEs, {min(len(posts), blog['home'])} posts and the events")
    else:
        kept &= keep([INCLUDES / "news.md"], f"the news of the home page cannot be written: {'; '.join(unread)}")
    return 0 if kept else 1


if __name__ == "__main__":
    sys.exit(main())
