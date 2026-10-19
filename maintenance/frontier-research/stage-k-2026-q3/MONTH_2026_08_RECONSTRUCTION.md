# 2026-Q3 / 08 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/auto-doc-engine`; research month: `2026-08-01 through 2026-08-31`
- Stage owner: `K / 2026-Q3`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-08-29 — Math-method and template-fetch semantics
- **Primary source:** https://github.com/jgm/pandoc/releases/tag/3.11 (`jgm/pandoc@3.11`, `S6`)
- **Publisher-described observation:** Pandoc 3.11 introduces --math-method, changes the default to mathml, retains deprecated aliases and reports a security-related template-fetch fix.
- **Analytic implication:** Math rendering policy, config aliases and fetching/source trust can change independently of source text.
- **Alternative / qualification:** Neither a security fix nor a new default proves the absence of residual threats or identical rendering in any host.
- **Research owner:** `K2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O6 / S6 (pandoc 3.11) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. lineage != truth; hash identity != semantic equivalence; format support != fidelity; released specification != local conformance; packaging != independent reproduction.
No `auto-doc-engine` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
