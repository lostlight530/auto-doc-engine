# 2026-Q1 / 03 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/auto-doc-engine`; research month: `2026-03-01 through 2026-03-31`
- Stage owner: `I / 2026-Q1`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-03-19 — Typst-template regression repair
- **Primary source:** https://github.com/jgm/pandoc/releases/tag/3.9.0.2 (`jgm/pandoc@3.9.0.2`, `S2`)
- **Publisher-described observation:** Pandoc 3.9.0.2 is explicitly a fix for a regression in the Typst template introduced in an earlier 3.9 patch sequence.
- **Analytic implication:** A patch-release boundary can affect the rendered derivative even when source content is unchanged.
- **Alternative / qualification:** A repaired reported regression does not establish semantic equivalence across all Typst document cases.
- **Research owner:** `I2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O2 / S2 (pandoc 3.9.0.2) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. lineage != truth; hash identity != semantic equivalence; format support != fidelity; released specification != local conformance; packaging != independent reproduction.
No `auto-doc-engine` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
