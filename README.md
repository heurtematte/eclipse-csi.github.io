# eclipse-csi.github.io

Source of [csi.eclipse.dev](https://csi.eclipse.dev/), the website of the
[Eclipse Common Security Infrastructure](https://projects.eclipse.org/projects/technology.csi) (CSI) project: its home
page, a page listing the projects of the [eclipse-csi](https://github.com/eclipse-csi) GitHub organization, and the
blog posts and events of the Eclipse Foundation Security Team. The projects support the security services of the
Eclipse Foundation, presented on [eclipse.org/security](https://www.eclipse.org/security/).

It is built with [Zensical](https://zensical.org/) and follows the brand guidelines of Eclipse CSI
([eclipse-csi/.github](https://github.com/eclipse-csi/.github/tree/main/artwork/eclipse-csi)): its colors, the
Montserrat typeface and the official artwork, unaltered.

## Layout

| Path | Content |
| --- | --- |
| `docs/index.md` | The home page, below the hero of `overrides/main.html`. |
| `docs/support.md`, `docs/contribute.md` | Where to ask for help, and how to contribute. |
| `docs/report-a-vulnerability.md` | The entry of security researchers: how to report, what to include, what happens next. |
| `docs/handle-a-vulnerability.md` | The entry of the committers of Eclipse projects: how to be ready, then handle a report. |
| `docs/projects.md` | The projects page, **generated** and not versioned: edit `projects.toml` instead. |
| `projects.toml` | How the repositories are arranged on the projects page: areas, extra links, descriptions. |
| `scripts/generate_projects.py` | Writes `docs/projects.md`, metrics included, from `projects.toml`, the GitHub API, the OpenSSF Scorecard API and the PMI. |
| `docs/blog.md`, `docs/events.md` | The blog and events pages, **generated** and not versioned: edit `news.toml`. |
| `includes/` | **Generated** and not versioned: the news of the home page (`news.md`) and the discussions of the support page (`discussions.md`). |
| `news.toml` | What the news list: the tags of blogs.eclipse.org, the channel of the newsroom, the latest CVEs. |
| `scripts/generate_news.py` | Writes the blog and events pages and `includes/news.md` from `news.toml`, blogs.eclipse.org, the newsroom and the CVEs of api.eclipse.org. |
| `docs/assets/stylesheets/csi.css` | The brand: colors, typeface, hero and cards. |
| `zensical.toml` | The configuration of the site. |
| `.github/workflows/site.yml` | Builds and deploys the site to GitHub Pages. |

## Working on the site

```sh
make serve      # regenerate the generated pages, then preview at http://127.0.0.1:8000/
make build      # regenerate the generated pages, then build strictly into site/: broken links and anchors fail
make generate   # only regenerate them: make projects (set GITHUB_TOKEN to raise the API rate limit) and make news
```

The metrics of the projects page (contributors and releases) take two requests to the GitHub API per project: without
a token, its rate limit of 60 requests an hour allows a couple of builds. `make` therefore uses the token of the GitHub
CLI (`gh auth login`) when `GITHUB_TOKEN` is not set; the script only sends it to the GitHub API. If a metric cannot be
read all the same, the page of the previous run is kept.

The generated pages are not versioned: every build writes them from their sources, as CI does, so that no copy lags
behind the site. A source that cannot be read keeps the pages of the previous run, with a warning, when there are some:
the site can be previewed offline once it has been built.

`make install` creates `.venv` with Zensical, installed from `requirements.txt` with the hashes of every file, as in
CI. `make requirements` relocks it (requires [uv](https://docs.astral.sh/uv/)).

## Listing a new project

Every public repository of the organization appears on the projects page at the next build, even before it is
curated: one that `projects.toml` does not list is shown under "Other projects", and the build warns about it. Add it
to the `repositories` of an area of `projects.toml` to place it. An archived repository leaves the page by itself:
the build warns if `projects.toml` still lists it.

## Listing a blog post or an event

The blog lists the posts of [blogs.eclipse.org](https://blogs.eclipse.org) that have one of the `tags` of
`news.toml` (`security` and `sbom`): tag a post with one of them to list it. Each tag is read from its RSS feed, which
holds its 10 latest posts; the page links to blogs.eclipse.org for the older ones.

The events are those of the [newsroom of the Eclipse Foundation](https://newsroom.eclipse.org) published to the
`security` channel ("Publish to" of the event), except those where only member organizations take part: publish an
event to this channel to list it. An event is upcoming until its last day, then moves to the past events at the next
build.


## Deployment

`.github/workflows/site.yml` builds the site on every pull request and deploys it from `main` to GitHub Pages, on every
change and once a day, so that the projects page follows the organization, and the blog and the events their
sources. CI starts from a fresh checkout, without the pages of a previous run: if the GitHub API, blogs.eclipse.org or
the newsroom cannot be read, the build fails, the deployment is skipped and GitHub Pages keeps serving the last site
deployed. GitHub suspends the daily run after 60 days without a commit in the repository: it is resumed from the
Actions tab.

GitHub Pages must be built by a workflow: `gh_pages_build_type: 'workflow'` in the otterdog configuration of the
organization ([eclipse-csi/.eclipsefdn](https://github.com/eclipse-csi/.eclipsefdn)).

## Copyright and license

Copyright the [Eclipse Foundation](https://www.eclipse.org) and others. The logos are the intellectual property of the
Eclipse Foundation and are used under the
[Eclipse Foundation Trademark Usage Policy](https://www.eclipse.org/legal/logo_guidelines.php). Montserrat is
licensed under the SIL Open Font License 1.1 (`docs/assets/fonts/OFL.txt`).
