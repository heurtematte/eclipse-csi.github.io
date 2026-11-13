---
title: Threat model
description: >-
  Why an Eclipse project should maintain a threat model, what it contains, how to start one, and examples from
  Eclipse CSI.
---

# Threat model

A threat model says what your project protects, from whom, and where an attacker could reach it. It is short,
written by the maintainers, and it is the reference against which every vulnerability report about your project is
assessed.
{ .csi-lead }

## Why maintain one { #why }

- **Reports are assessed faster.** Whether a reported input is trusted, whether a behavior is a documented non-goal,
  whether a deployment is supported: the threat model answers these questions, and makes it much easier to tell
  whether an issue is actually exploitable and what else it may affect.
- **Reviews follow what you said.** Reviewers, people or AI agents, audit a project against its own threat model when
  it has one: it is the authority on where its trust boundary sits. Without one, they fall back on general defaults,
  which may not match how your project is meant to be used.
- **Your users deploy it safely.** The deployment assumptions tell them what your project expects of its environment.
- **Design and code reviews have a reference.** A change that crosses a trust boundary is visible as such.

## What it contains { #contents }

| Part | What it says |
| --- | --- |
| Assets | What must be protected: data, credentials, integrity of the releases, availability of a service. |
| Trust boundaries | Which inputs are untrusted (network requests, files, archives, repository content) and which are controlled by the operator or the developer. |
| Entry points | Where an attacker can reach the project: interfaces, file formats, plugins, webhooks. |
| Threats and mitigations | What could go wrong at each entry point, for example by the STRIDE categories, and what prevents it. |
| Guarantees and non-goals | What the project promises ("paths cannot escape the root") and what it explicitly does not protect against. |
| Deployment assumptions | Runs as root or unprivileged, single or multi-tenant, local tool or network service. |
| Residual risks | The risks that are accepted, or that remain to be reduced. |

## How to start { #start }

1. **Keep it lightweight.** One page, `docs/threat-model.md` or a section of `SECURITY.md`, beats a complete model
   that nobody maintains.
2. **Draft it with help.** The [threat-model skill](https://github.com/alpha-omega-security/threat-model) of
   Alpha-Omega drafts `docs/threat-model.md` and `threat-model.yaml` from your repository, and tags each claim as
   documented, confirmed by a maintainer or inferred: review the inferred parts before you publish it.
3. **Publish it.** Link it from your `SECURITY.md` and your README, where reporters and reviewers look first.
4. **Revisit it** when the architecture, the exposed interfaces, the dependencies or the intended use of the project
   change.

## Examples and resources { #resources }

- [The threat model of Otterdog](https://csi.eclipse.dev/otterdog/threat-model/): assets, trust boundaries, entry
  points, a STRIDE analysis, a risk register and the security invariants to check in CI.
- [The generic security audit skill](https://github.com/eclipse-csi/skills/tree/main/generic-security-audit) of
  Eclipse CSI: how an audit starts from the threat model of the project, and what it extracts from it.
- [The Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
  of OWASP, and the [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/).

See also [Secure your project](secure-your-project.md), where the threat model is one of the steps.
