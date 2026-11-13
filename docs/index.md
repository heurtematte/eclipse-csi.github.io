---
title: Eclipse Common Security Infrastructure (CSI)
description: >-
  Eclipse CSI develops the tools, services and practices that secure the software supply chain of Eclipse projects:
  Otterdog, SBOMs, code signing and more.
hide:
  - navigation
  - toc
---

<!-- the hero above the page (overrides/main.html) shows the logo, its tagline (site_description) and the entries of
     each audience, and holds the title of the page: the page has no heading of its own -->

<!-- the Security Handbook, featured: styled by .csi-feature (assets/stylesheets/csi.css) -->
<section class="csi-feature" markdown>

<div markdown>

<p class="csi-feature__kicker">Best practices</p>

## Eclipse Foundation Security Handbook { #handbook }

The best practices that secure the development of Eclipse projects: the accounts and machines of their developers,
their repositories and branches, the handling of their vulnerabilities and the publication of their SBOMs. It is
developed in the open by Eclipse CSI, and contributions are welcome.

[:lucide-book-open: Read the handbook](https://csi.eclipse.dev/security-handbook/){ .md-button .md-button--primary }
[:fontawesome-brands-github: Contribute](https://github.com/eclipse-csi/security-handbook){ .md-button }

</div>

<div class="csi-feature__topics" markdown>

- :lucide-user-lock: **[Developers](https://csi.eclipse.dev/security-handbook/developer/index.html)**: accounts, machines, development environment and
  branches.
- :lucide-clipboard-check: **[Projects](https://csi.eclipse.dev/security-handbook/project/index.html)**: the Rapid Security Review.
- :lucide-shield-alert: **[Vulnerabilities](https://csi.eclipse.dev/security-handbook/vulnerabilities/index.html)**: embargoes and security advisories.
- :lucide-package-search: **[SBOMs](https://csi.eclipse.dev/security-handbook/sbom/index.html)**: generate and upload them, opt in for vulnerability alerts,
  tooling.

</div>

</section>

## What Eclipse CSI provides { #services }

The tools and services that Eclipse projects use to secure their repositories, their releases and the handling of
their vulnerabilities. See all of them in [Projects](projects.md).
{ .csi-area-lead }

<div class="csi-cards" markdown>

<article class="csi-card" markdown>

:lucide-git-pull-request-arrow:{ .csi-card__icon }

### Manage GitHub repositories

Eclipse projects configure their GitHub organizations and repositories as code with
[Otterdog](projects.md#otterdog): every change is a reviewed pull request. Its
[blueprints](https://csi.eclipse.dev/otterdog/reference/blueprints/) spread security best practices across all of
them, with pull requests that add a `SECURITY.md`, pin GitHub Actions to commit hashes or set up OpenSSF Scorecard.

<p class="csi-card__links" markdown>[:lucide-book-open: Guide](https://csi.eclipse.dev/otterdog/userguide/) [:lucide-blocks: Blueprints](https://csi.eclipse.dev/otterdog/reference/blueprints/) [:lucide-arrow-right: Projects](projects.md#github-ci)</p>

</article>

<article class="csi-card" markdown>

:lucide-package-search:{ .csi-card__icon }

### Publish and monitor SBOMs

Projects publish the software bills of materials (SBOMs) of their releases to
[sbom.eclipse.org](https://sbom.eclipse.org), which monitors their dependencies for known vulnerabilities. Workflows
authenticate with OpenID Connect through [PIA](projects.md#pia), without any long-lived secret.

<p class="csi-card__links" markdown>[:lucide-book-open: Guide](https://csi.eclipse.dev/security-handbook/sbom/index.html) [:lucide-globe: sbom.eclipse.org](https://sbom.eclipse.org) [:fontawesome-brands-github: upload-sbom](https://github.com/eclipse-csi/workflows/tree/main/upload-sbom) [:lucide-arrow-right: Projects](projects.md#supply-chain)</p>

</article>

<article class="csi-card" markdown>

:lucide-file-signature:{ .csi-card__icon }

### Sign release artifacts

[Codesign tools](projects.md#codesign-tools) sign executables and other release artifacts through the SignPath
service, from any CI/CD pipeline: a native command line tool, a Maven plugin and a Java API.

<p class="csi-card__links" markdown>[:lucide-book-open: Guide](https://csi.eclipse.dev/codesign-tools/) [:lucide-arrow-right: Projects](projects.md#supply-chain)</p>

</article>

<article class="csi-card" markdown>

:lucide-shield-alert:{ .csi-card__icon }

### Publish security advisories

<p class="csi-card__tags"><span class="csi-tag csi-tag--soon">Coming soon</span></p>

[AdvisoryHub](projects.md#advisoryhub), soon available, will be where the security advisories of Eclipse projects are
authored, reviewed and published, then exported to the OSV and CSAF formats. Until then, projects publish their
advisories as the [Security Handbook](https://csi.eclipse.dev/security-handbook/vulnerabilities/advisories.html)
explains.

<p class="csi-card__links" markdown>[:lucide-book-open: Guide](https://csi.eclipse.dev/security-handbook/vulnerabilities/advisories.html) [:lucide-arrow-right: AdvisoryHub](projects.md#advisoryhub)</p>

</article>

<article class="csi-card" markdown>

:lucide-fingerprint:{ .csi-card__icon }

### Request a CVE ID

The Eclipse Foundation is a
[CVE Numbering Authority](https://www.cve.org/PartnerInformation/ListofPartners/partner/eclipse) (CNA) for all its
projects and services: its Security Team assigns the CVE IDs of their vulnerabilities and publishes the CVE records.

<p class="csi-card__links" markdown>[:lucide-book-open: Guide](handle-a-vulnerability.md#process) [:lucide-list: Published CVEs](cves.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-scan-search:{ .csi-card__icon }

### Review your project's security

The [Rapid Security Review Runner](projects.md#rsrr) automates the checks of the Rapid Security Reviews of Eclipse
projects, and the Security Team reviews every Eclipse project with
[AI-assisted analysis](ai-security-reviews.md), validated by people.

<p class="csi-card__links" markdown>[:lucide-book-open: Guide](https://csi.eclipse.dev/security-handbook/project/index.html) [:fontawesome-brands-github: rsrr](https://github.com/eclipse-csi/rsrr) [:lucide-arrow-right: AI-assisted reviews](ai-security-reviews.md)</p>

</article>

</div>

## News { #news }

The latest CVEs of Eclipse projects, the latest posts of the Eclipse Foundation blog on security, and the events of
the Eclipse Foundation Security Team.
{ .csi-area-lead }

--8<-- "news.md"

<p class="csi-links" markdown>[:lucide-rss: Subscribe to the news (Atom feed)](feed.xml)</p>

## Learn { #learn }

The free security trainings of the Eclipse Foundation Security Team, in video, and the talks of its members.
{ .csi-area-lead }

<div class="csi-cards csi-cards--compact" markdown>

<article class="csi-card" markdown>

:lucide-user-lock:{ .csi-card__icon }

### Security training, part 1

The security of developers, in five videos: workstation, accounts, version control and day-to-day security.

<p class="csi-card__links" markdown>[:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=pAlsonP1gJQ) [:lucide-arrow-right: Sessions](learn.md#training-developers)</p>

</article>

<article class="csi-card" markdown>

:lucide-shield-alert:{ .csi-card__icon }

### Security training, part 2

Vulnerability management and SBOMs, in five videos with their slides: CVEs, coordinated disclosure, dependencies.

<p class="csi-card__links" markdown>[:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=JdeSEzAVy8Q) [:lucide-arrow-right: Sessions](learn.md#training-vulnerabilities)</p>

</article>

<article class="csi-card" markdown>

:lucide-presentation:{ .csi-card__icon }

### Talks and webinars

Otterdog, security audits, SBOMs and the Cyber Resilience Act, at OCX and in the webinars of the Eclipse Foundation.

<p class="csi-card__links" markdown>[:lucide-arrow-right: All the talks](talks.md)</p>

</article>

</div>

<p class="csi-links" markdown>[:fontawesome-brands-youtube: The playlist of the trainings](https://www.youtube.com/playlist?list=PLy7t4z5SYNaT7JN8FIVTGAy1QUnLTdv9R) [:lucide-arrow-right: Learn](learn.md)</p>
