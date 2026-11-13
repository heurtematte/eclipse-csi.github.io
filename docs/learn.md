---
title: Learn
description: >-
  The security trainings of the Eclipse Foundation Security Team, its guides and its reading list for the developers
  of Eclipse projects.
---

# Learn

The trainings of the Eclipse Foundation Security Team, the guides of this site and a reading list: what the developers
of Eclipse projects need to know about vulnerability management, the software supply chain and secure development.
{ .csi-lead }

## Security trainings { #trainings }

The Eclipse Foundation Security Team gives free security trainings for the developers of Eclipse projects, in two
parts. Their recordings are on the YouTube channel of the Eclipse Foundation, in the
[Eclipse Foundation Security Training](https://www.youtube.com/playlist?list=PLy7t4z5SYNaT7JN8FIVTGAy1QUnLTdv9R)
playlist.

<p class="csi-links" markdown>[:fontawesome-brands-youtube: Watch the playlist](https://www.youtube.com/playlist?list=PLy7t4z5SYNaT7JN8FIVTGAy1QUnLTdv9R)</p>

### Part 1: the security of developers { #training-developers }

| Session | What it covers | Video |
| --- | --- | --- |
| 1. Introduction | Why the security of developers matters, and what the training covers | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=pAlsonP1gJQ) |
| 2. Workstation security | Securing the machine you develop on | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=lvXVvWMKt14) |
| 3. Account security | Securing your accounts and their credentials | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=bxFxr7EYjYo) |
| 4. Version control security | Securing your repositories, branches and commits | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=j4MY9gQ6uvY) |
| 5. Day-to-day security | The habits that keep a project secure | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=b73k-vdb5xQ) |

### Part 2: vulnerability management and SBOMs { #training-vulnerabilities }

Given in June 2025, then again in November 2025: the videos are those of June, the slides those of November (see the
[post that presents them](https://blogs.eclipse.org/post/marta-rybczynska/security-training-vulnerability-management-and-sboms-november-2025-videos-are)).

| Session | What it covers | Video | Slides |
| --- | --- | --- | --- |
| 1. Vulnerability management introduction | What a vulnerability is, the vulnerability databases, CVE, NVD and CVSS | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=JdeSEzAVy8Q) | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_1_Vulnerability_management_introduction.pdf) |
| 2. Vulnerability management at the Eclipse Foundation | How the reports are handled: the GitLab tracker, the private advisories of GitHub, the security teams of the projects | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=Teed6BCwTbE) | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_2_Vulnerability_management_at_EF.pdf) |
| 3. Coordinated disclosures and embargoes | Fixing an issue across several projects, synchronized releases, embargoes and coordinators | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=9gEMwbnY0PU) | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_3_Coordinated_disclosures_and_embargoes.pdf) |
| 4. Dependency management | The lessons of XZ and Log4j, and the handling of dependencies, Dependabot included | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=0Jw9yQBHMv4) | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_4_Dependency_Management.pdf) |
| 5. SBOM | What an SBOM is, the tools that generate one, dependency tracking and the early adopters program | [:fontawesome-brands-youtube: Watch](https://www.youtube.com/watch?v=A45V__wcXBM) | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_5_SBOMs_0.pdf) |

The next trainings are announced on the [Events](events.md) page.

## Talks and webinars { #talks }

Recordings from the YouTube channel of the [Eclipse Foundation](https://www.youtube.com/user/EclipseFdn):

| Video | Where |
| --- | --- |
| [Security at the Eclipse Foundation](https://www.youtube.com/watch?v=2KHI5HFqIl8) | A short presentation of the security work of the Eclipse Foundation |
| [GitHub for Fun, Profit, and Security](https://www.youtube.com/watch?v=k5tSbZ8YDA0) | OCX 2024: managing GitHub organizations at scale and securely |
| [Security Audits Panel](https://www.youtube.com/watch?v=yYA2Gny7-io) | OCX 2024 |
| [Navigating a security audit](https://www.youtube.com/watch?v=v96kTZTuils) | OCX 2024: the insights, challenges and lessons learnt |
| [Demystifying SBOMs: why the CRA wants your software's DNA](https://www.youtube.com/watch?v=4j37a2gYCw8) | Open Community Webinar |
| [OSS provenance and code signing](https://www.youtube.com/watch?v=_fGOgByN08c) | CRA Mondays |
| [When Disclosure Fails: Europe's Struggle with CVD](https://www.youtube.com/watch?v=G37gXO0KG6I) | CRA Mondays: coordinated vulnerability disclosure |

On the Cyber Resilience Act, the Open Regulatory Compliance Working Group publishes two playlists:
[Unpacking the CRA](https://www.youtube.com/playlist?list=PLy7t4z5SYNaTnHCiz8ADmGZ_z6YZGd0wI) and
[CRA Mondays](https://www.youtube.com/playlist?list=PLy7t4z5SYNaT-DjqGR0ORSSZGZYW8qmRs).

## Guides { #guides }

<div class="csi-cards csi-cards--compact" markdown>

<article class="csi-card" markdown>

:lucide-list-checks:{ .csi-card__icon }

### Secure your project

The checklist of a project: its security team, its reporting channel, its workflows, its SBOMs and its reviews.

<p class="csi-card__links" markdown>[:lucide-arrow-right: The checklist](secure-your-project.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-map:{ .csi-card__icon }

### Threat model

What a threat model contains, why it speeds up the handling of reports, and how to start one.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Threat model](threat-model.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-bot:{ .csi-card__icon }

### Secure development with AI

The guidelines of the Eclipse Foundation, sandboxes for coding agents, least privilege and review.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Secure development with AI](ai-secure-development.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-shield-check:{ .csi-card__icon }

### Handle a vulnerability

What the security team of a project does, from the report to the publication of the CVE.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Handle a vulnerability](handle-a-vulnerability.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-book-lock:{ .csi-card__icon }

### Security Handbook

The best practices of Eclipse projects: accounts, machines, branches, vulnerability management and SBOMs.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Read the handbook](https://csi.eclipse.dev/security-handbook/)</p>

</article>

</div>

## Reading list { #reading }

A selection of the posts of the Eclipse Foundation blog; the [Blog](blog.md) lists the latest ones.

- [The Vulnerability Report Is Dead. Long Live the Prompt!](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/vulnerability-report-dead-long-live-prompt):
  what an AI-assisted vulnerability report should include.
- [Stop trusting mutable references](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/stop-trusting-mutable-references-how-eclipse-foundation-projects-should-harden)
  and [Don't become the next Trivy](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/dont-become-next-trivy-how-make-your-releases-tags-and-automation-resistant):
  hardening GitHub Actions, releases and tags.
- [Fewer keys under the doormat](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/fewer-keys-under-doormat-why-trusted-publishing-matters-open-vsx):
  why trusted publishing matters.
- [Eclipse Foundation GitLab incident postmortem: CVE-2026-85706](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/eclipse-foundation-gitlab-incident-postmortem-cve-2026-85706):
  what happened, and what was learned.
