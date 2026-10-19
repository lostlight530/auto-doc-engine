# 2026-Q3 / 09 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/auto-doc-engine`; research month: `2026-09-01 through 2026-09-30`
- Stage owner: `K / 2026-Q3`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-09-17 — Cryptographic-related XML schema fix
- **Primary source:** https://github.com/CycloneDX/specification/releases/tag/1.7.2 (`CycloneDX/specification@1.7.2`, `S7`)
- **Publisher-described observation:** CycloneDX 1.7.2 adds an optional repeated XML node for relatedCryptographicAsset and introduces schema tests.
- **Analytic implication:** Evidence portability depends on schema revision and serialization-specific relations; a BOM can encode claims without verifying them.
- **Alternative / qualification:** XML schema presence alone does not establish producer adoption, correctness or cross-format equivalence.
- **Research owner:** `K3` in this Stage; one originating source family, no independent validation.

### 2026-09-29 — Performance and XML fragment output
- **Primary source:** https://github.com/jgm/pandoc/releases/tag/3.12 (`jgm/pandoc@3.12`, `S8`)
- **Publisher-described observation:** Pandoc 3.12 reports performance-oriented changes and makes -t xml respect --standalone, emitting a fragment when absent.
- **Analytic implication:** Latency claims and output framing are separate transformation evidence; an output structure change can affect derivative identity.
- **Alternative / qualification:** Publisher-reported benchmarks are not independent reproducibility or evidence of local speed-up.
- **Research owner:** `K4` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O7 / S7 (specification 1.7.2), O8 / S8 (pandoc 3.12) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. lineage != truth; hash identity != semantic equivalence; format support != fidelity; released specification != local conformance; packaging != independent reproduction.
No `auto-doc-engine` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
