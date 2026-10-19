# 2026-Q2 / 06 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/auto-doc-engine`; research month: `2026-06-01 through 2026-06-30`
- Stage owner: `J / 2026-Q2`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-06-02 — Schema alignment across serializations
- **Primary source:** https://github.com/CycloneDX/specification/releases/tag/1.7.1 (`CycloneDX/specification@1.7.1`, `S3`)
- **Publisher-described observation:** CycloneDX 1.7.1 adds ModelCard.property in Protobuf and modelCard properties/consideration cardinality alignments in XML and adds matching tests.
- **Analytic implication:** Serializations of ostensibly one evidence object have versioned schema behavior; version and format need distinct identity.
- **Alternative / qualification:** An upstream schema fix does not prove that every producer or consumer correctly interprets the altered fields.
- **Research owner:** `J1` in this Stage; one originating source family, no independent validation.

### 2026-06-04 — Typst parameter and writer-default state
- **Primary source:** https://github.com/jgm/pandoc/releases/tag/3.10 (`jgm/pandoc@3.10`, `S4`)
- **Publisher-described observation:** Pandoc 3.10 adds --typst-input to pass sys.inputs parameters and changes the default ms PDF engine to groff; ODT style emission also changes.
- **Analytic implication:** Transformation receipts should distinguish explicit parameters, inferred defaults and output writer/backend revision.
- **Alternative / qualification:** A release note cannot establish that a particular document was regenerated, nor that old and new defaults yield equivalent output.
- **Research owner:** `J2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O3 / S3 (specification 1.7.1), O4 / S4 (pandoc 3.10) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. lineage != truth; hash identity != semantic equivalence; format support != fidelity; released specification != local conformance; packaging != independent reproduction.
No `auto-doc-engine` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
