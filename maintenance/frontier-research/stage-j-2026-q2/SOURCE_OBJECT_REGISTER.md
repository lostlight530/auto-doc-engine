# Source and Research-Object Register — J/2026-Q2

- Repository: `lostlight530/auto-doc-engine`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | astral-sh/uv `0.11.4` | 2026-04-08 | S1 | `astral-sh/uv` | https://github.com/astral-sh/uv/releases/tag/0.11.4 | Published upstream release note describing direct-URL hash matching and merged archive hashes; NOT local deployment or reproduction |
| O2 | astral-sh/uv `0.11.9` | 2026-05-05 | S2 | `astral-sh/uv` | https://github.com/astral-sh/uv/releases/tag/0.11.9 | Published upstream release note describing manual GitHub release publication after registry timeout with GitHub attestations unavailable; NOT local deployment or reproduction |
| O3 | CycloneDX/specification `1.7.1` | 2026-06-02 | S3 | `CycloneDX/specification` | https://github.com/CycloneDX/specification/releases/tag/1.7.1 | Published upstream release note describing Protobuf/XML model-card schema alignment; NOT local deployment or reproduction |
| O4 | jgm/pandoc `3.10` | 2026-06-04 | S4 | `jgm/pandoc` | https://github.com/jgm/pandoc/releases/tag/3.10 | Published upstream release note describing Typst sys.inputs parameters and ODT style-generation changes; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
