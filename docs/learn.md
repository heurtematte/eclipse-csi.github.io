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

The Eclipse Foundation Security Team gives free security trainings for the developers of Eclipse projects. The second
part of its training, on vulnerability management and SBOMs, was given in June 2025, then again in November 2025;
the slides of each section are below, and the
[recordings of the June session](https://blogs.eclipse.org/post/marta-rybczynska/security-training-vulnerability-management-and-sboms-november-2025-videos-are)
are in the post that presents them.

| Section | What it covers | Slides |
| --- | --- | --- |
| 1. Vulnerability management introduction | What a vulnerability is, the vulnerability databases, CVE, NVD and CVSS | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_1_Vulnerability_management_introduction.pdf) |
| 2. Vulnerability management at the Eclipse Foundation | The process in practice: the GitLab tracker, the private advisories of GitHub, the security teams of the projects | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_2_Vulnerability_management_at_EF.pdf) |
| 3. Coordinated disclosures and embargoes | Fixing an issue across several projects, synchronized releases, embargoes and coordinators | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_3_Coordinated_disclosures_and_embargoes.pdf) |
| 4. Dependency management | The lessons of XZ and Log4j, and the handling of dependencies, Dependabot included | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_4_Dependency_Management.pdf) |
| 5. SBOM | What an SBOM is, the tools that generate one, and the early adopters program of sbom.eclipse.org | [PDF](https://blogs.eclipse.org/sites/default/files/2025-11/EF_Security_Training_Part_2_Section_5_SBOMs_0.pdf) |

The next trainings are announced on the [Events](events.md) page.

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
