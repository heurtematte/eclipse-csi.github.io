---
title: Contribute
description: >-
  How to contribute to Eclipse CSI: code, documentation, testing and feedback from Eclipse projects, and how to
  become a committer.
---

# Contribute

From code and documentation to testing and feedback from the projects that use them: contributions of every kind make
the tools of Eclipse CSI better, and the software supply chain of Eclipse projects safer.
{ .csi-lead }

## Not sure where to start? { #start }

- **New to Eclipse CSI?** A good starting point is the [documentation](#documentation), the Security Handbook in
  particular, or [testing and bug reports](#testing).
- **Developer?** Fix a bug or build a feature in one of the [projects](projects.md): see
  [development](#development).
- **Committer or project lead of an Eclipse project?** Share your [feedback](#feedback): what works for your
  project, and what is missing.

!!! tip "Looking for help?"

    If you came here with a question, a problem or a usage topic to discuss, the [Support](support.md) page explains
    where and how to ask.

## Before your first contribution { #first }

1. Create an [Eclipse account](https://accounts.eclipse.org/user/register) and sign the
   [Eclipse Contributor Agreement](https://www.eclipse.org/legal/eca/) (ECA), with the email address of the "Author"
   field of your commits: the ECA is checked on every pull request.
2. Read the contribution guide of the repository when it has one, such as the
   [developer guide of Otterdog](https://csi.eclipse.dev/otterdog/developing_otterdog/) or the `CONTRIBUTING.md` of
   [codesign-tools](https://github.com/eclipse-csi/codesign-tools/blob/main/CONTRIBUTING.md) and
   [advisoryhub](https://github.com/eclipse-csi/advisoryhub/blob/main/CONTRIBUTING.md).
3. Follow the [Eclipse Community Code of Conduct](https://www.eclipse.org/org/documents/Community_Code_of_Conduct.php).

Eclipse CSI is governed by the [Eclipse Development Process](https://eclipse.org/projects/dev_process), as every
Eclipse project: see [contributing to an Eclipse project](https://www.eclipse.org/projects/handbook/#contributing).

## Development { #development }

**Who:** software developers, DevOps and platform engineers.

**How you can contribute:**

- Contribute code to any of the [projects](projects.md): fix bugs or implement new features.
- Improve the tests, the CI pipelines and the release engineering, and keep them as secure as the projects they
  serve.

**Getting started:**

- Look for issues labeled
  [good first issue](https://github.com/search?q=org%3Aeclipse-csi+label%3A%22good+first+issue%22+state%3Aopen&type=issues)
  across the organization, or for the open issues of a project.
- Ask your questions in [GitHub Discussions](https://github.com/orgs/eclipse-csi/discussions) or on the
  [csi-dev mailing list](https://accounts.eclipse.org/mailing-list/csi-dev).
- For a large change, open an issue or a discussion first to agree on the approach.

## Documentation { #documentation }

**Who:** everyone, and first of all those who apply the practices.

**How you can contribute:**

- Improve the [Security Handbook](https://github.com/eclipse-csi/security-handbook): fix an outdated or unclear page,
  add a best practice learned on your project.
- Improve the documentation of a tool, in its repository.
- Improve this website: [eclipse-csi.github.io](https://github.com/eclipse-csi/eclipse-csi.github.io).

## Testing and bug reports { #testing }

**Who:** users of the tools, testers, developers.

**How you can contribute:**

- Use the tools and report the bugs you find, following [Before you ask](support.md#before).
- Reproduce the reported issues, and complete them with reproduction steps or minimal examples.
- Write automated tests for the untested parts.

## Feedback from Eclipse projects { #feedback }

**Who:** committers and project leads of Eclipse projects.

**How you can contribute:**

- Tell what works and what is missing when your project adopts Otterdog, SBOMs, code signing or security advisories.
- Share your use cases and your workarounds in [GitHub Discussions](https://github.com/orgs/eclipse-csi/discussions):
  they shape what the tools do next.

## Security research { #security }

Found a weakness in one of the tools of Eclipse CSI? Do not open a public issue or pull request: report it
confidentially, as explained in [Report a vulnerability](report-a-vulnerability.md). The fix is then developed in
private.

## Becoming a committer { #committer }

[Committers](https://www.eclipse.org/projects/handbook/#roles-cm) decide what goes into the projects: they push to
the repositories, review the pull requests of contributors, and vote in the elections of the project. Every committer
of Eclipse CSI started as a contributor: committer status is earned by contributing, whoever your employer is, and the
path is the same for everyone, as in every Eclipse project. The
[Eclipse Project Handbook](https://www.eclipse.org/projects/handbook/#elections-committer) describes it in full.

<div class="csi-steps" markdown>

1. **Contribute.** Pull requests, reviews, answers in discussions, design proposals: every public contribution counts,
   and a steady flow of good ones builds the trust of the committers. See
   [How much contribution is enough?](https://www.eclipse.org/projects/handbook/#elections-contribution)
2. **Nomination.** When your pull requests get merged with little discussion and no change, a committer can nominate
   you, with a public statement of merit that cites your contributions. See
   [What should a nomination look like?](https://www.eclipse.org/projects/handbook/#elections-nomination)
3. **Election.** The [committers](https://projects.eclipse.org/projects/technology.csi/who) vote for one week, on the
   [csi-dev mailing list](https://accounts.eclipse.org/mailing-list/csi-dev): the election needs at least three +1
   votes and no -1, and every committer votes when there are three or fewer. See
   [How does an election work?](https://www.eclipse.org/projects/handbook/#elections-how)
4. **Approval.** The Project Management Committee reviews the result, then the paperwork of the new committer starts:
   a committer agreement, depending on your employer. See
   [Committer paperwork](https://www.eclipse.org/projects/handbook/#paperwork).

</div>

[Project leads](https://www.eclipse.org/projects/handbook/#roles-pl), the link between the team and the Eclipse
Foundation, are elected the same way, among the committers, then appointed by the Eclipse Management Organization: see
[Project lead elections](https://www.eclipse.org/projects/handbook/#elections-pl).

!!! info "In the Eclipse Project Handbook"

    - [Committers](https://www.eclipse.org/projects/handbook/#roles-cm) and
      [Project Lead](https://www.eclipse.org/projects/handbook/#roles-pl): the roles and their responsibilities.
    - [Committer Elections](https://www.eclipse.org/projects/handbook/#elections-committer): the requirements, the
      nomination, how much contribution is enough, and how an election works.
    - [Project Lead Elections](https://www.eclipse.org/projects/handbook/#elections-pl).
    - [Committer Paperwork](https://www.eclipse.org/projects/handbook/#paperwork): the agreements a new committer
      signs.
    - [Frequently Asked Questions](https://www.eclipse.org/projects/handbook/#elections-faq) about elections.
