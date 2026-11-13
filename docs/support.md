---
title: Support
description: >-
  Where to ask a question about the tools of Eclipse CSI, report a bug or discuss an idea: GitHub issues, GitHub
  Discussions and the csi-dev mailing list.
---

# Support

Not sure where to ask your question? Each channel below suits one kind of question: choosing the right one gets you
an answer faster, and keeps it findable for the next person who has the same question.
{ .csi-lead }

!!! danger "Found a vulnerability? Do not use these channels"

    They are public. Report a vulnerability confidentially, as explained in
    [Report a vulnerability](report-a-vulnerability.md).

## Communication channels { #channels }

<div class="csi-cards csi-cards--compact" markdown>

<article class="csi-card" markdown>

:lucide-messages-square:{ .csi-card__icon }

### GitHub Discussions

For **questions and ideas that others may benefit from later**: how to use a tool, how others do it, an idea not yet
ready for an issue. The organization has its discussions, and some projects have their own.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Find the discussions](#discussions)</p>

</article>

<article class="csi-card" markdown>

:fontawesome-brands-github:{ .csi-card__icon }

### GitHub issues

For **concrete, technical topics** about one tool: reporting a bug or a regression, requesting a feature, proposing an
improvement. Each project tracks its issues in its own repository, for follow-up and long-term reference.

<p class="csi-card__links" markdown>[:lucide-arrow-right: Find the project](projects.md)</p>

</article>

<article class="csi-card" markdown>

:lucide-mail:{ .csi-card__icon }

### Mailing list

For **broader, project-wide topics**: a design that spans several tools, announcements, the life of the project
(releases, plans, committer elections). Subscribe to read and write to it.

<p class="csi-card__links" markdown>[:lucide-arrow-right: csi-dev](https://accounts.eclipse.org/mailing-list/csi-dev)</p>

</article>

</div>

## GitHub Discussions { #discussions }

The first place to ask a question or share an idea: in the discussions of the project it is about, or in those of the
organization for anything else. Answers stay there for the next person who has the same question.

--8<-- "discussions.md"

## Where should I ask my question? { #where }

A simple rule of thumb:

- **A question or a discussion others might benefit from later?** Use
  [GitHub Discussions](https://github.com/orgs/eclipse-csi/discussions).
- **A bug or a concrete problem that needs tracking?** Open an issue in the repository of the tool: see the
  [projects](projects.md).
- **An idea or a design across several tools?** Write to the
  [csi-dev mailing list](https://accounts.eclipse.org/mailing-list/csi-dev).
- **A vulnerability?** Never in public: [report it confidentially](report-a-vulnerability.md).

If in doubt, GitHub Discussions is usually the safest choice.

!!! tip "Going one step further?"

    Some questions lead to small improvements of the tools or of the Security Handbook, and there are many ways to
    help, not only by writing code: [learn how you can contribute](contribute.md).

## Before you ask { #before }

A few small steps help others help you:

- Search the existing issues and discussions first.
- Say which tool and which version you use.
- Include the relevant logs or error messages, **with the secrets removed**: tokens, passwords, private keys and
  internal URLs.
- If you can, give a minimal example that reproduces the problem.
- State what you expected to happen, and what happened instead.

Well-prepared questions get faster and more precise answers.

## New to Eclipse CSI? { #new }

Start with the documentation of the tools and with the Security Handbook: they explain the concepts and the setup,
which helps you ask more precise questions and understand the answers.

- [Otterdog](https://csi.eclipse.dev/otterdog/): GitHub organizations as code.
- [Codesign tools](https://csi.eclipse.dev/codesign-tools/): signing release artifacts through SignPath.
- [AdvisoryHub](https://csi.eclipse.dev/advisoryhub/dev/): security advisories.
- [sbom.eclipse.org](https://sbom.eclipse.org): the SBOMs of Eclipse projects and their dependencies.
- [Security Handbook](https://csi.eclipse.dev/security-handbook/): the best practices for Eclipse projects.

If a page is outdated or unclear, say so in an issue of its repository, or propose a fix: that is a contribution too.
