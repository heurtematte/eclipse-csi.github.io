---
title: Secure your project
description: >-
  A checklist for the committers and project leads of Eclipse projects: the project security team, the reporting
  channel, GitHub as code, accounts and workflows, SBOMs and signing, the threat model and the reviews.
---

# Secure your project

A checklist for the committers and project leads of Eclipse projects: what to set up, step by step, to receive
vulnerability reports, protect your repositories and your releases, and know where your project is exposed. Each step
points to the tool of Eclipse CSI or to the page of the [Security Handbook](https://csi.eclipse.dev/security-handbook/)
that helps.
{ .csi-lead }

## 1. Set up your project security team { #security-team }

Vulnerability reports are assigned automatically to the people listed as the security team of your project in the
PMI. When no team is set, all the committers receive them: too many people for a confidential report.

- Open the page of your project on the [PMI](https://projects.eclipse.org/) and review its Security Team setting.
- Keep it to a small group of committers who will triage and handle the reports, **typically 2 to 4 people**. Other
  committers can be brought in after the first triage.
- Make sure the people listed are active and reachable, and that each of them has signed in once on
  [gitlab.eclipse.org](https://gitlab.eclipse.org), where the reports are handled.

See [the project security team](https://www.eclipse.org/projects/handbook/#projects-security-team) in the Eclipse
Project Handbook.

## 2. Tell reporters where to go { #reporting }

- **Publish a `SECURITY.md`**, from the
  [template](https://github.com/eclipse-csi/security-handbook/blob/main/templates/SECURITY.md) of the Security
  Handbook. On GitHub, the `default-security-policy`
  [blueprint](https://csi.eclipse.dev/otterdog/reference/blueprints/) of Otterdog adds one to the `.github` repository
  of your organization when it has none.
- **Choose your channel**: the confidential issues of the vulnerability reports tracker, or the private vulnerability
  reporting of GitHub, which [Otterdog enables](https://csi.eclipse.dev/otterdog/userguide/guides/repository-security/#private-vulnerability-reporting).

Then read [Handle a vulnerability](handle-a-vulnerability.md): it is what your security team does when a report
arrives.

## 3. Manage your GitHub organization as code { #github }

[Otterdog](projects.md#otterdog) keeps the settings of your GitHub organization and repositories in a configuration
that changes only through reviewed pull requests, with the policies of the Eclipse Foundation applied to all of them.

- Make your project security team a
  [security manager](https://csi.eclipse.dev/otterdog/userguide/guides/repository-security/#organization-settings-related-to-security)
  of the organization, so that it sees the security alerts and can create draft security advisories.
- Merge the pull requests of the [blueprints](https://csi.eclipse.dev/otterdog/reference/blueprints/): they add a
  `SECURITY.md`, [pin GitHub Actions](https://csi.eclipse.dev/otterdog/reference/blueprints/pin-workflow/) to commit
  hashes, or set up the [OpenSSF Scorecard](https://csi.eclipse.dev/otterdog/reference/blueprints/scorecard-integration/).

## 4. Secure your accounts, machines and branches { #accounts }

The Security Handbook gathers the practices of the developers of Eclipse projects:

- [Securing developer accounts](https://csi.eclipse.dev/security-handbook/developer/account.html);
- [Securing development machines](https://csi.eclipse.dev/security-handbook/developer/machine.html);
- [Securing development branches](https://csi.eclipse.dev/security-handbook/developer/branches.html).

## 5. Harden your workflows and releases { #workflows }

A compromised workflow or a stolen publishing credential reaches every user of your releases. Read:

- [Stop trusting mutable references](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/stop-trusting-mutable-references-how-eclipse-foundation-projects-should-harden):
  how Eclipse projects should harden GitHub Actions;
- [Don't become the next Trivy](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/dont-become-next-trivy-how-make-your-releases-tags-and-automation-resistant):
  releases, tags and automation resistant to compromise;
- [Fewer keys under the doormat](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/fewer-keys-under-doormat-why-trusted-publishing-matters-open-vsx):
  why trusted publishing matters.

## 6. Publish SBOMs and sign your releases { #supply-chain }

- **SBOMs**: generate the software bill of materials of each release and upload it to
  [sbom.eclipse.org](https://sbom.eclipse.org), which watches its dependencies for known vulnerabilities. See
  [how to generate and upload SBOMs](https://csi.eclipse.dev/security-handbook/sbom/howto.html) and the
  [upload-sbom](https://github.com/eclipse-csi/workflows/tree/main/upload-sbom) workflow, which authenticates through
  [PIA](projects.md#pia) with OpenID Connect, without any long-lived secret.
- **Signing**: sign your executables and release artifacts with the
  [codesign tools](https://csi.eclipse.dev/codesign-tools/).

## 7. Maintain a threat model { #threat-model }

Know what your project protects, where its trust boundaries are, and which deployment assumptions matter: the
[threat model](threat-model.md) is what every vulnerability report is assessed against, by your team and by the
reviewers of your project.

## 8. Measure and review { #review }

- **OpenSSF Scorecard**: a score of the security practices of each repository, set up by the
  [scorecard blueprint](https://csi.eclipse.dev/otterdog/reference/blueprints/scorecard-integration/).
- **Rapid Security Review**: a self-evaluation of the security posture of your project, described in the
  [Security Handbook](https://csi.eclipse.dev/security-handbook/project/reviews.html), whose checks the
  [Rapid Security Review Runner](projects.md#rsrr) automates.
- **AI-assisted review**: the Eclipse Foundation Security Team reviews Eclipse projects with AI-assisted analysis, and
  your project can ask to be prioritized: see [AI-assisted security reviews](ai-security-reviews.md).

## 9. Prepare for the Cyber Resilience Act { #cra }

Most of these steps are also what the manufacturers that use your project expect of it under the
[Cyber Resilience Act](cra.md).

!!! tip "Questions?"

    Ask them in the [GitHub Discussions](https://github.com/orgs/eclipse-csi/discussions) of Eclipse CSI, or see the
    [Support](support.md) page.
