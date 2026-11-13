---
title: Cyber Resilience Act
description: >-
  The EU Cyber Resilience Act and open source: how the Eclipse Foundation works on it, and how the tools and practices
  of Eclipse CSI help Eclipse projects meet what is expected of them.
---

# Cyber Resilience Act

The EU Cyber Resilience Act (CRA) sets cybersecurity requirements for the products with digital elements sold in the
European Union, and through them it reaches the open source they are built from. This page explains how the Eclipse
Foundation works on it, and how the tools and practices of Eclipse CSI help Eclipse projects meet what is expected of
them.
{ .csi-lead }

!!! note "Not legal advice"

    This page gives pointers, not a legal interpretation of the regulation. For that, start from the resources of the
    Open Regulatory Compliance Working Group below.

## The Open Regulatory Compliance Working Group { #orc }

The [Open Regulatory Compliance Working Group](https://orcwg.org/) (ORC WG), hosted by the Eclipse Foundation, brings
together manufacturers, small and medium enterprises, research institutions, open source foundations and maintainers.
Together, they interpret the rules, contribute to standards, and produce free resources that make the obligations
actionable for open source. The CRA is its current focus, followed by its
[special interest group on cyber resilience](https://orcwg.org/special-interest-groups/cyber-resilience/); see its
[charter](https://www.eclipse.org/collaborations/working-groups/open-regulatory-compliance/charter/).

## OCCTET: an open source compliance toolkit { #occtet }

[OCCTET](https://occtet.eu/) (Open-source Compliance: Comprehensive Techniques and Essential Tools) is an EU-funded
project, in which the Eclipse Foundation takes part, that helps small and medium-sized enterprises and open source
projects get ready for the CRA, with free, open source tools and practical guidance:

- a **CRA self-assessment platform**, to measure where you stand;
- a **toolchain**, the ORT Server, OCCTET Curator and VulnerableCode, that turns source code into SBOMs, VEX documents
  and audit reports;
- **checklists, templates and guidance** for SMEs, open source projects and open source stewards;
- its **deliverables and webinars**, such as
  [Turn CRA Awareness into Action](https://www.youtube.com/watch?v=54S-kJj1bv4).

<p class="csi-links" markdown>[:lucide-arrow-right: occtet.eu](https://occtet.eu/)</p>

## What it means for open source { #open-source }

The CRA places its main obligations on manufacturers, the companies that place products on the EU market. They must,
among other things, know the components of their products, handle their vulnerabilities and provide security updates:
for the open source they use, they turn to its projects. The regulation also introduces a lighter regime for the
stewards of open source, the organizations, such as foundations, that support open source projects intended for
commercial use.

For an Eclipse project, this means that its users increasingly expect it to:

- **describe its components**, in a software bill of materials (SBOM);
- **handle its vulnerabilities** through a known process, with CVEs and security advisories;
- **release its fixes** and tell its users about them;
- **develop and release securely**, with protected accounts, repositories and workflows.

## How Eclipse CSI helps { #csi }

| Expectation | Tools and practices |
| --- | --- |
| Describe the components | [SBOMs](https://csi.eclipse.dev/security-handbook/sbom/index.html), uploaded to [sbom.eclipse.org](https://sbom.eclipse.org), which watches the dependencies for known vulnerabilities |
| Handle the vulnerabilities | The [coordinated process](handle-a-vulnerability.md) of the Eclipse Foundation, the [CVEs](cves.md) it publishes as a CNA, and [security advisories](https://csi.eclipse.dev/security-handbook/vulnerabilities/advisories.html) (soon in [AdvisoryHub](projects.md#advisoryhub)) |
| Act quickly on an exploited vulnerability | Tell the Eclipse Foundation Security Team [at once](handle-a-vulnerability.md#urgent) |
| Develop and release securely | The [Security Handbook](https://csi.eclipse.dev/security-handbook/), [Otterdog](projects.md#otterdog), [code signing](projects.md#codesign-tools) and a [threat model](threat-model.md) |

[Secure your project](secure-your-project.md) puts these steps in order.

## Webinars and resources { #resources }

- The playlists of the ORC WG on the YouTube channel of the Eclipse Foundation:
  [Unpacking the CRA](https://www.youtube.com/playlist?list=PLy7t4z5SYNaTnHCiz8ADmGZ_z6YZGd0wI), and
  [CRA Mondays](https://www.youtube.com/playlist?list=PLy7t4z5SYNaT-DjqGR0ORSSZGZYW8qmRs), whose sessions include
  [OSS provenance and code signing](https://www.youtube.com/watch?v=_fGOgByN08c) and
  [When Disclosure Fails: Europe's Struggle with CVD](https://www.youtube.com/watch?v=G37gXO0KG6I).
- [Demystifying SBOMs: why the CRA wants your software's DNA](https://www.youtube.com/watch?v=4j37a2gYCw8) (Open
  Community Webinar).
- [Unpacking the CRA](https://www.crowdcast.io/c/orc-28042025): how the open source community collaborates in the
  ORC WG to address the CRA (webinar, April 2025).
- [Exploring an Open Source Toolkit for SMEs to manage Cyber Resilience Act compliance](https://www.digitalsme.eu/events/exploring-an-open-source-toolkit-for-smes-to-manage-cyber-resilience-act-compliance/):
  the toolkit of [OCCTET](#occtet) (webinar, October 2026).
- The [events](events.md) of the Eclipse Foundation Security Team, many of which are about the CRA.
