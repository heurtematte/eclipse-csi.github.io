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
| Handle the vulnerabilities | The [coordinated process](handle-a-vulnerability.md) of the Eclipse Foundation, the [CVEs](cves.md) it publishes as a CNA, and the security advisories of [AdvisoryHub](projects.md#advisoryhub) |
| Act quickly on an exploited vulnerability | Tell the Eclipse Foundation Security Team [at once](handle-a-vulnerability.md#urgent) |
| Develop and release securely | The [Security Handbook](https://csi.eclipse.dev/security-handbook/), [Otterdog](projects.md#otterdog), [code signing](projects.md#codesign-tools) and a [threat model](threat-model.md) |

[Secure your project](secure-your-project.md) puts these steps in order.

## Webinars and resources { #resources }

- [Unpacking the CRA](https://www.crowdcast.io/c/orc-28042025): how the open source community collaborates in the
  ORC WG to address the CRA (webinar, April 2025).
- [Exploring an Open Source Toolkit for SMEs to manage Cyber Resilience Act compliance](https://www.digitalsme.eu/events/exploring-an-open-source-toolkit-for-smes-to-manage-cyber-resilience-act-compliance/)
  (webinar, October 2026).
- The [events](events.md) of the Eclipse Foundation Security Team, many of which are about the CRA.
