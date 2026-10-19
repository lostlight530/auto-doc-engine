# Versioned Evidence Chart — Stage J / 2026-Q2

- Repository: `lostlight530/auto-doc-engine`
- Source window: `2026-04-01 through 2026-06-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
The chart compares different primary-release events, not a quantitative time-series. Observed source text and research inference stay in separate columns.

| Object/source | Publisher statement | Interpretation | Strongest scope limit | Execution/reproduction |
|---|---|---|---|---|
| O1 / [S1](https://github.com/astral-sh/uv/releases/tag/0.11.3) | Workspace metadata now includes lock dependency information | Lock descriptions and realized runtime remain separate | No native workspace was installed or checked | `NOT_RUN` |
| O2 / [S2](https://github.com/astral-sh/uv/releases/tag/0.11.17) | Fixes Git archive lock handling and preserves repository URLs in direct URL metadata | Source location and archive resolution are evidence separate from content identity | Preserved URL is not authenticated content | `NOT_RUN` |
| O3 / [S3](https://github.com/CycloneDX/specification/releases/tag/1.7.1) | Aligns model-card properties in XML/Protobuf and adds schema tests | Schema revision and serialization must be identified | Publisher tests are not local cross-format conformance | `NOT_RUN` |
| O4 / [S4](https://github.com/jgm/pandoc/releases/tag/3.10) | Adds --typst-input and changes ODT styles and ms PDF engine default | Writer parameters, default engine and output style are transform identity | No particular document was reproduced | `NOT_RUN` |

## Counterevidence, negative space, review
All included sources are publisher release artifacts; no independent technical reproduction or independent contradiction search was performed. These versions do not share a common task, result variable or evaluator. Same-producer extraction and review; field-wide change or current repo behavior cannot be inferred from source counts.
