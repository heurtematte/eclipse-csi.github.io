---
title: AI-assisted security reviews
description: >-
  How the Eclipse Foundation Security Team reviews Eclipse projects with AI-assisted analysis, as part of Project
  Glasswing, and how a project is prioritized.
---

# AI-assisted security reviews

The Eclipse Foundation Security Team reviews the code of Eclipse projects with AI-assisted analysis, validated by
people, and handles what it finds through the coordinated vulnerability-management process of the Eclipse Foundation.
Every Eclipse project will be reviewed; the projects ready to work with the team can ask to be reviewed first.
{ .csi-lead }

## The program { #program }

- In September 2026, the Eclipse Foundation joined Anthropic's **Project Glasswing**: the Security Team uses Claude
  Mythos 5 to strengthen the security of Eclipse projects.
- Before that, thanks to its partnership with [Alpha-Omega](https://alpha-omega.dev/), the team had used the preview
  version of Mythos since the start of Glasswing, and scanned all the Eclipse Foundation projects with it: many
  projects received reports through the standard vulnerability-reporting process.
- A new campaign with Mythos 5 ran through the end of October 2026.

## How a review works { #how }

- **Automated and AI-assisted analysis, validated by people**: the Security Team checks every finding before it
  reaches a project.
- **Every project is reviewed**, enrolled or not. Enrollment is a way to be prioritized, neither a permission nor a way
  to opt out.
- **A review may start without notice.** When it finds a credible issue, a private vulnerability report is normally
  the first notification of the review. It is then handled like any other report: the team and the project work
  together on its validation, its fix, its release and its disclosure.
- **When a review finds nothing credible**, the project is told once the review is complete.
- **It is a best-effort assessment** of the analyzed repositories at a point in time: not a certification, nor a
  complete audit, nor a replacement for the secure development and vulnerability management of the project. A review
  without findings does not mean that the project has no vulnerability.

## Get your project prioritized { #enroll }

A project can ask for its review to be prioritized when:

- its team is ready to collaborate on the validation and the fixes;
- the repositories it lists are actively maintained;
- its project security team includes active committers who can act on the reports.

A project lead or a committer opens a merge request in the
[enrollment repository](https://gitlab.eclipse.org/eclipsefdn/security/ai-scan-enrollment), as its README explains.
Enrollment is not first come, first served, and it does not guarantee a date: the schedule depends on the priorities
of the program and on its capacity.

!!! warning "The enrollment repository is public"

    Its merge requests are public: never use them to report a vulnerability or to share anything sensitive.

## Be ready for the reports { #ready }

- **Set up your project security team**, 2 to 4 active committers, in the PMI: the reports are assigned to it. See
  [Secure your project](secure-your-project.md#security-team).
- **Know what to do when a report arrives**: see [Handle a vulnerability](handle-a-vulnerability.md).
- **Publish a [threat model](threat-model.md)**: findings are assessed against it, which tells a real vulnerability
  from a documented non-goal sooner.

## Read more { #more }

- [Growing the Eclipse Foundation Security Team to Meet the AI Moment](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/growing-eclipse-foundation-security-team-meet-ai-moment)
- [Frontier AI and the next phase of software vulnerability defence](https://blogs.eclipse.org/post/mike-milinkovich/frontier-ai-and-next-phase-software-vulnerability-defence-0)
- [The Vulnerability Report Is Dead. Long Live the Prompt!](https://blogs.eclipse.org/post/mika%C3%ABl-barbero/vulnerability-report-dead-long-live-prompt):
  what an AI-assisted vulnerability report should include.

Questions about the program are welcome in the [GitHub Discussions](https://github.com/orgs/eclipse-csi/discussions)
of Eclipse CSI.
