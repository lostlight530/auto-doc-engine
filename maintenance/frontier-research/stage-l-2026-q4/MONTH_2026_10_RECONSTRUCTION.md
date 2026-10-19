# 2026-Q4 / 10 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/auto-doc-engine`; research month: `2026-10-01 through 2026-10-19`
- Stage owner: `L / 2026-Q4`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_OPEN — as of 2026-10-19`

## Selected events and evidence
### 2026-10-08 — Citation parsing and new FODT source surface
- **Primary source:** https://github.com/jgm/pandoc/releases/tag/3.12.1 (`jgm/pandoc@3.12.1`, `S9`)
- **Publisher-described observation:** Pandoc 3.12.1 adds FODT input/output and changes citeproc interpretation of structured surname particles, alongside several regression fixes.
- **Analytic implication:** A citation-provenance path depends on a named converter revision and reference semantics; apparently identical data may yield different derivative citations.
- **Alternative / qualification:** No local bibliography regression test or semantic-fidelity replay was performed.
- **Research owner:** `L1` in this Stage; one originating source family, no independent validation.

### 2026-10-09 — Interpreter-default and lock/runtime separation
- **Primary source:** https://github.com/astral-sh/uv/releases/tag/0.13.0 (`astral-sh/uv@0.13.0`, `S10`)
- **Publisher-described observation:** uv 0.13.0 announces Python 3.15 as its default stable Python, together with correctness and compatibility changes.
- **Analytic implication:** Environment resolution defaults are another independent clock for reproducible document generation; lock representation does not establish the realized interpreter.
- **Alternative / qualification:** Published installer defaults are not evidence of which interpreter this repository installed.
- **Research owner:** `L2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O9 / S9 (pandoc 3.12.1), O10 / S10 (uv 0.13.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. lineage != truth; hash identity != semantic equivalence; format support != fidelity; released specification != local conformance; packaging != independent reproduction.
No `auto-doc-engine` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
