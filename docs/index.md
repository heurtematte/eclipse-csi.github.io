---
title: Eclipse Common Security Infrastructure
description: >-
  Eclipse CSI develops the tools, services and best practices that secure the software supply chain of Eclipse
  Foundation projects: GitHub organizations as code, SBOMs, code signing, security advisories and reviews.
hide:
  - navigation
  - toc
---

# Eclipse Common Security Infrastructure

<!-- the hero above the page (overrides/main.html) shows the logo, this title is hidden by the stylesheet -->

The Eclipse Common Security Infrastructure (CSI) project develops the cyber security and supply chain management
tools and best practices shared by Eclipse Foundation projects, and by any open source project that wants them. It
makes the security infrastructure available to projects visible, defines the policies that keep their development
secure, and gives them the tools to apply these policies and to check continuously that they do.
{ .csi-lead }

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

## News { #news }

The latest CVEs of Eclipse projects, the latest posts of the Eclipse Foundation blog on security, and the events of
the Eclipse Foundation Security Team.
{ .csi-area-lead }

--8<-- "news.md"

## What Eclipse CSI provides { #services }

<div class="csi-cards" markdown>

<article class="csi-card" markdown>

:lucide-git-pull-request-arrow:{ .csi-card__icon }

### GitHub organizations as code

Eclipse projects configure their GitHub organizations and repositories as code with
[Otterdog](projects.md#otterdog): every change is a reviewed pull request. Its
[blueprints](https://csi.eclipse.dev/otterdog/reference/blueprints/) spread security best practices across all of
them, with pull requests that add a `SECURITY.md`, pin GitHub Actions to commit hashes or set up OpenSSF Scorecard.

<p class="csi-card__links" markdown>[:lucide-book-open: Documentation](https://csi.eclipse.dev/otterdog/) [:lucide-blocks: Blueprints](https://csi.eclipse.dev/otterdog/reference/blueprints/) [:lucide-arrow-right: Projects](projects.md#github-ci)</p>

</article>

<article class="csi-card" markdown>

:lucide-package-search:{ .csi-card__icon }

### SBOMs and dependency tracking

Projects publish the software bills of materials (SBOMs) of their releases to
[sbom.eclipse.org](https://sbom.eclipse.org), which monitors their dependencies for known vulnerabilities. Workflows
authenticate with OpenID Connect through [PIA](projects.md#pia), without any long-lived secret.

<p class="csi-card__links" markdown>[:lucide-globe: sbom.eclipse.org](https://sbom.eclipse.org) [:fontawesome-brands-github: upload-sbom](https://github.com/eclipse-csi/workflows/tree/main/upload-sbom) [:lucide-arrow-right: Projects](projects.md#supply-chain)</p>

</article>

<article class="csi-card" markdown>

:lucide-file-signature:{ .csi-card__icon }

### Code signing

[Codesign tools](projects.md#codesign-tools) sign executables and other release artifacts through the SignPath
service, from any CI/CD pipeline: a native command line tool, a Maven plugin and a Java API.

<p class="csi-card__links" markdown>[:lucide-book-open: Documentation](https://csi.eclipse.dev/codesign-tools/) [:lucide-arrow-right: Projects](projects.md#supply-chain)</p>

</article>

<article class="csi-card" markdown>

:lucide-shield-alert:{ .csi-card__icon }

### Security advisories

[AdvisoryHub](projects.md#advisoryhub) is where the security advisories of Eclipse projects are authored, reviewed
and published, then exported to the OSV and CSAF formats.

<p class="csi-card__links" markdown>[:lucide-book-open: Documentation](https://csi.eclipse.dev/advisoryhub/dev/) [:lucide-arrow-right: Projects](projects.md#vulnerabilities)</p>

</article>

<article class="csi-card" markdown>

:lucide-fingerprint:{ .csi-card__icon }

### CVE Numbering Authority

The Eclipse Foundation is a
[CVE Numbering Authority](https://www.cve.org/PartnerInformation/ListofPartners/partner/eclipse) (CNA) for all its
projects and services: its Security Team assigns the CVE IDs of their vulnerabilities and publishes the CVE records.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Request a CVE ID](handle-a-vulnerability.md#process) [:lucide-list: Known vulnerabilities](https://www.eclipse.org/security/known/)</p>

</article>

<article class="csi-card" markdown>

:lucide-scan-search:{ .csi-card__icon }

### Security reviews

The [Rapid Security Review Runner](projects.md#rsrr) automates the checks of the Rapid Security Reviews of Eclipse
projects, such as their Dependabot alerts, security advisories and private vulnerability reporting.

<p class="csi-card__links" markdown>[:fontawesome-brands-github: Repository](https://github.com/eclipse-csi/rsrr) [:lucide-arrow-right: Projects](projects.md#vulnerabilities)</p>

</article>

</div>

## Report a vulnerability { #report }

!!! warning "Found a vulnerability in an Eclipse project?"

    Please do not report it in a public issue, pull request or discussion. Report it confidentially, through the
    channel given by the `SECURITY.md` of the project:

    - open a [confidential issue](https://gitlab.eclipse.org/security/vulnerability-reports/-/work_items/new?issue%5Bconfidential%5D=true)
      in the vulnerability reports tracker of the Eclipse Foundation;
    - or, if the project uses them, open a private security advisory on its GitHub repository (Security tab, "Report a
      vulnerability").

    The Eclipse Foundation Security Team then brings in the project, as set out in the
    [Eclipse Foundation Security Policy](https://www.eclipse.org/security/policy/).
    [What to include in your report, and what happens next](report-a-vulnerability.md).

    Committer of an Eclipse project that received a report? See [Handle a vulnerability](handle-a-vulnerability.md).

## Get involved { #get-involved }

<div class="csi-cards csi-cards--compact" markdown>

<article class="csi-card" markdown>

:fontawesome-brands-github:{ .csi-card__icon }

### Contribute

Every project of Eclipse CSI is developed in the open: code, documentation, testing and feedback are welcome.

<p class="csi-card__links" markdown>[:lucide-arrow-right: How to contribute](contribute.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-life-buoy:{ .csi-card__icon }

### Support

A question, a bug or an idea: GitHub issues and discussions, and the csi-dev mailing list.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Where to ask](support.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-landmark:{ .csi-card__icon }

### Governance

Eclipse CSI is a project of Eclipse Technology: its committers, releases and plans are on the Eclipse project
management infrastructure.

<p class="csi-card__links" markdown>[:lucide-arrow-right: projects.eclipse.org](https://projects.eclipse.org/projects/technology.csi)</p>

</article>

<article class="csi-card" markdown>

:lucide-shield-check:{ .csi-card__icon }

### Security at Eclipse

The Eclipse Foundation Security Team coordinates the disclosure of vulnerabilities and helps projects secure their
development.

<p class="csi-card__links" markdown>[:lucide-arrow-right: eclipse.org/security](https://www.eclipse.org/security/)</p>

</article>

</div>
