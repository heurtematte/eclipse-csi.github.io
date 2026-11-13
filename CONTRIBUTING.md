# Contributing to the website of Eclipse CSI

Thanks for your interest in the website of the Eclipse Common Security Infrastructure (CSI), served at
[csi.eclipse.dev](https://csi.eclipse.dev/). This file explains how to contribute to this repository; the
[Contribute](https://csi.eclipse.dev/contribute/) page of the site explains how to contribute to Eclipse CSI as a whole.

## Project description

Eclipse CSI develops the tools, services and best practices that secure the software supply chain of Eclipse
Foundation projects. This repository holds the source of its website.

- <https://projects.eclipse.org/projects/technology.csi>

## Developer resources

The site is built with [Zensical](https://zensical.org/). The [README](README.md) describes its layout; in short:

```sh
make serve      # regenerate the generated pages, then preview at http://127.0.0.1:8000/
make build      # regenerate them, then build strictly into site/: broken links and anchors fail
```

- **Hand-written pages** are in `docs/`: edit them directly.
- **Generated pages** (projects, blog, events, CVEs, team, news) are written at every build by `scripts/` and are not
  versioned: edit `projects.toml`, `news.toml` or the scripts instead.
- **The brand** of Eclipse CSI (colors, Montserrat, official artwork, unaltered) is in
  `docs/assets/stylesheets/csi.css` and `overrides/`.

Before opening a pull request, run `make build`: it must finish without any warning of the strict build.

## Reporting issues and asking questions

- Report a problem of the site, or propose an improvement, in the
  [issues](https://github.com/eclipse-csi/eclipse-csi.github.io/issues) of this repository.
- Ask a question in the [GitHub Discussions](https://github.com/orgs/eclipse-csi/discussions) of Eclipse CSI.
- **Never report a vulnerability in public**: follow [SECURITY.md](https://github.com/eclipse-csi/.github/blob/main/SECURITY.md)
  and the [Report a vulnerability](https://csi.eclipse.dev/report-a-vulnerability/) page.

## Eclipse Development Process

This Eclipse Foundation open project is governed by the Eclipse Foundation Development Process and operates under the
terms of the Eclipse IP Policy.

- <https://eclipse.org/projects/dev_process>
- <https://www.eclipse.org/org/documents/Eclipse_IP_Policy.pdf>

## Eclipse Contributor Agreement

In order to be able to contribute to Eclipse Foundation projects you must electronically sign the Eclipse Contributor
Agreement (ECA):

- <https://www.eclipse.org/legal/eca/>

The ECA provides the Eclipse Foundation with a permanent record that you agree that each of your contributions will
comply with the commitments documented in the Developer Certificate of Origin (DCO). Having an ECA on file associated
with the email address matching the "Author" field of your contribution's Git commits fulfills the DCO's requirement
that you sign-off on your contributions.

For more information, please see the Eclipse Committer Handbook:

- <https://www.eclipse.org/projects/handbook/#resources-commit>

## Code of Conduct

This project follows the [Eclipse Community Code of Conduct](https://www.eclipse.org/org/documents/Community_Code_of_Conduct.php).

## License

The source of this website is released under the [Eclipse Public License 2.0](LICENSE), except the logos of the Eclipse
Foundation and of Eclipse CSI, which are its intellectual property and are used under the
[Eclipse Foundation Trademark Usage Policy](https://www.eclipse.org/legal/logo_guidelines.php), and Montserrat, licensed
under the SIL Open Font License 1.1 (`docs/assets/fonts/OFL.txt`).
