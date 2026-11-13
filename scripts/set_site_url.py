#!/usr/bin/env python3
"""Set the address of the site (site_url of zensical.toml) to the GitHub Pages of a fork.

The site of eclipse-csi is served at csi.eclipse.dev, the site_url of zensical.toml. A fork serves it on its own GitHub
Pages, at https://<owner>.github.io/<repository>/ (https://<owner>.github.io/ for a repository named
<owner>.github.io): its canonical links, its sitemap, its feed and its instant navigation must use that address.
.github/workflows/site.yml runs this script before the build, in a fork only.

Usage: python scripts/set_site_url.py <owner>/<repository>

Only the standard library is used, so that the script runs before anything is installed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ZENSICAL_TOML = Path(__file__).resolve().parent.parent / "zensical.toml"
# the names that GitHub allows for an owner and a repository: nothing else may reach zensical.toml
REPOSITORY = re.compile(r"(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/(?P<name>[A-Za-z0-9._-]{1,100})")
SITE_URL = re.compile(r'^site_url = "[^"\n]*"$', re.MULTILINE)


def pages_url(repository: str) -> str:
    match = REPOSITORY.fullmatch(repository)
    if not match:
        raise ValueError(f"not a GitHub repository: {repository!r}")
    owner, name = match["owner"].lower(), match["name"]
    return f"https://{owner}.github.io/" if name.lower() == f"{owner}.github.io" else f"https://{owner}.github.io/{name}/"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.splitlines()[-3], file=sys.stderr)
        return 2
    url = pages_url(sys.argv[1])
    config = ZENSICAL_TOML.read_text(encoding="utf-8")
    if len(SITE_URL.findall(config)) != 1:
        print("zensical.toml: expected exactly one site_url line", file=sys.stderr)
        return 1
    ZENSICAL_TOML.write_text(SITE_URL.sub(f'site_url = "{url}"', config), encoding="utf-8")
    print(f"zensical.toml: site_url = {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
