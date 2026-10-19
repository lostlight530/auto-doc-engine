# Source and Research-Object Register — K/2026-Q3

- Repository: `lostlight530/auto-doc-engine`; constructed 2026-10-19; source cutoff 2026-10-19.
- Identity rule: **tagged upstream release object != release-note report**. Official release note and tag belong to one origin; separate release versions remain separate objects. Version existence does not entail local execution.

| Object ID | Canonical release object | GitHub release publication | Source ID | Original source family | URL | What is established / not established |
|---|---|---|---|---|---|---|
| O1 | astral-sh/uv `0.12.0` | 2026-07-28 | S1 | `astral-sh/uv` | https://github.com/astral-sh/uv/releases/tag/0.12.0 | Published upstream release note describing uv init newly creates build-system declarations by default; NOT local deployment or reproduction |
| O2 | jgm/pandoc `3.11` | 2026-08-29 | S2 | `jgm/pandoc` | https://github.com/jgm/pandoc/releases/tag/3.11 | Published upstream release note describing math-method option migration, RTL handling and template-fetch security fix; NOT local deployment or reproduction |
| O3 | CycloneDX/specification `1.7.2` | 2026-09-17 | S3 | `CycloneDX/specification` | https://github.com/CycloneDX/specification/releases/tag/1.7.2 | Published upstream release note describing XML schema correction for related cryptographic assets; NOT local deployment or reproduction |
| O4 | jgm/pandoc `3.12` | 2026-09-29 | S4 | `jgm/pandoc` | https://github.com/jgm/pandoc/releases/tag/3.12 | Published upstream release note describing performance-focused release with changed XML standalone/fragment behavior; NOT local deployment or reproduction |

- Search/access date: 2026-10-19; release dates are upstream publication dates, not this repository's execution dates.
- Shared-origin dependence: any repeated releases from the same project remain **same-origin** even if separated by months. No independent reproducer linked/validated in this register.
- Source selection: purposefully chosen research objects from listed families; `SOURCE_BOUNDED` only, no exhaustive project-history claim.
