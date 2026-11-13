.PHONY: help install projects news generate serve build requirements clean

VENV ?= .venv
PYTHON ?= python3
ADDR ?= 127.0.0.1:8000

help:  ## Show this help
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-14s %s\n", $$1, $$2}'

$(VENV)/bin/zensical: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --disable-pip-version-check --require-hashes --only-binary=:all: --no-deps \
		-r requirements.txt
	@touch $@

install: $(VENV)/bin/zensical  ## Install Zensical in .venv (hash-checked, as in CI)

# Without a token, the GitHub API allows 60 requests an hour and the metrics take two per project: the token of the
# GitHub CLI is used when GITHUB_TOKEN and GH_TOKEN are not set (the script only sends it to the GitHub API). It is
# exported to this target only, and never printed: it is not on the command line.
projects: export GITHUB_TOKEN ?= $(or $(GH_TOKEN),$(shell gh auth token 2>/dev/null))
projects:  ## Regenerate docs/projects.md from projects.toml, the GitHub API (with the token of gh, if any) and the PMI
	$(PYTHON) scripts/generate_projects.py

news:  ## Regenerate docs/blog.md, docs/events.md and includes/ from news.toml, blogs.eclipse.org and the newsroom
	$(PYTHON) scripts/generate_news.py

generate: projects news  ## Regenerate all the generated pages (not versioned: serve and build run it first)

serve: install generate  ## Preview the site with live reload, at http://127.0.0.1:8000/ unless ADDR is set
	$(VENV)/bin/zensical serve --dev-addr $(ADDR)

build: install generate  ## Build the site strictly into site/ (broken links and anchors fail)
	$(VENV)/bin/zensical build --strict --clean

requirements:  ## Relock requirements.txt from requirements.in, with hashes (needs uv)
	uv pip compile requirements.in --generate-hashes --python-version 3.12 --upgrade --quiet --no-header \
		-o requirements.txt
	sed -i '1i # Locked by `make requirements` from requirements.in (uv pip compile --generate-hashes): every file is hash-checked.' \
		requirements.txt

clean:  ## Remove the built site and the virtual environment
	rm -rf site .cache $(VENV)
