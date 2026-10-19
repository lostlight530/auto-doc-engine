# Source and Research-Object Register — I/2026-Q1

- Repository: `lostlight530/auto-doc-engine`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | astral-sh/uv `0.9.23` | 2026-01-09 | S1 | `astral-sh/uv` | https://github.com/astral-sh/uv/releases/tag/0.9.23 | Published upstream release note describing SBOM synthetic-root dependency fixes and portable installed RECORD paths; NOT local deployment or reproduction |
| O2 | jgm/pandoc `3.9` | 2026-02-04 | S2 | `jgm/pandoc` | https://github.com/jgm/pandoc/releases/tag/3.9 | Published upstream release note describing WASM/browser compilation, JSON/YAML defaults, media ZIP extraction and citation-state controls; NOT local deployment or reproduction |
| O3 | jgm/pandoc `3.9.0.2` | 2026-03-19 | S3 | `jgm/pandoc` | https://github.com/jgm/pandoc/releases/tag/3.9.0.2 | Published upstream release note describing Typst-template regression correction; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
