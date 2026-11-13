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

    This page gives pointers, not a legal interpretation of the regulation. Its facts come from the pages of the
    European Commission on the [CRA](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act),
    [open source](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source) and
    [reporting](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting); for an interpretation, start from the
    resources of the Open Regulatory Compliance Working Group below.

## Key dates { #dates }

| Date | What applies |
| --- | --- |
| 10 December 2024 | The CRA enters into force. |
| 11 September 2026 | **Manufacturers** must report the actively exploited vulnerabilities and the severe incidents that affect the security of their products, through the Single Reporting Platform of ENISA, operational since that day. |
| 11 December 2027 | The main obligations of the CRA apply, and **open-source software stewards** must report too (Article 24(3), in application from that date under Article 71(2)). |

The Commission published its [guidance on the CRA](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)
on 27 July 2026, to help manufacturers, developers and businesses of all sizes meet their obligations.

## Open source in the CRA { #open-source }

- **Only open source made available on the market is in scope**: open source supplied for distribution or use in the
  course of a commercial activity. Open source that its manufacturer does not monetise is not a commercial activity,
  and the CRA does not apply to the developers who contribute source code to open source that is not under their
  responsibility.
- **A manufacturer that places open source on the market** has the obligations of a manufacturer, as for any other
  product.
- **An open-source software steward** is a legal person that, without placing them on the market, provides
  systematic support on a sustained basis for the development of open source products intended for commercial
  activities, and ensures their viability. It has a light-touch regime of its own.

## The responsibilities of a foundation as a steward { #steward }

A foundation such as the Eclipse Foundation, which supports the development of its projects on a sustained basis,
takes on the role of open-source software steward. Article 24 of the CRA gives it three obligations:

1. **A cybersecurity policy** that fosters the secure development of its projects and the handling of their
   vulnerabilities: for the Eclipse Foundation, its [Security Policy](https://www.eclipse.org/security/policy/), the
   project security teams, the coordinated process to [handle a vulnerability](handle-a-vulnerability.md), and the
   [CVEs](cves.md) it assigns as a CNA.
2. **Cooperation with the market surveillance authorities.**
3. **Reporting the actively exploited vulnerabilities and the severe incidents** that affect the security of the
   products, from 11 December 2027, through the Single Reporting Platform, to the CSIRT of its main establishment, on
   the clocks of the CRA:

    | Step | Deadline |
    | --- | --- |
    | Early warning | Within 24 hours of becoming aware |
    | Notification | Within 72 hours |
    | Final report | No later than 14 days after a corrective measure is available, for an actively exploited vulnerability; within a month of the notification, for a severe incident |

Stewards are not subject to the administrative fines of the CRA (Article 64(10)).

## What it means for Eclipse projects { #projects }

- **Follow the security policy of the Eclipse Foundation.** Set up your
  [project security team](secure-your-project.md#security-team), handle your reports through the
  [coordinated process](handle-a-vulnerability.md), request your CVEs from the Eclipse Foundation, and release your
  fixes: it is the cybersecurity policy that the foundation documents as a steward.
- **Tell the Security Team at once** when you suspect that a vulnerability is actively exploited, or when an incident
  affects your project: the foundation has only 24 hours from becoming aware to send its early warning. See
  [when to tell the Security Team at once](handle-a-vulnerability.md#urgent).
- **Expect the questions of manufacturers.** The companies that build your project into the products they sell have
  the obligations of manufacturers: they will look for your software bill of materials, your vulnerability process,
  your security advisories and your fixes, and may report to you the vulnerabilities they find.
- **Publishing open source is not a commercial activity by itself**: a project does not become a manufacturer
  because companies use it. A company that places it on the market, as a product, does.

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

## How Eclipse CSI helps { #csi }

What the manufacturers that use Eclipse projects look for, and what the foundation needs of its projects as a steward:

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
- The pages of the European Commission on [open source in the CRA](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source)
  and on [its reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting), which link to
  its guidance, its FAQ and the Single Reporting Platform of ENISA.
