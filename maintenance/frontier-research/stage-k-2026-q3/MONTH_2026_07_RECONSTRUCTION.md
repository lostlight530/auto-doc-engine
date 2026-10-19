# Frontier Research Stage K / 2026-Q3 — 2026-07 monthly research reconstruction
- Source period: 2026-07; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Packaging and conversion-semantic identity. Evidence-object count: 1; **not** a measure of field-wide activity.
## 2026-07-28 — Packaged project initialization (`K-O1`)
**Publisher source:** [astral-sh/uv 0.12.0](https://github.com/astral-sh/uv/releases/tag/0.12.0) (`K-S1`).
**Observed release note:** uv changes new uv init projects to packaged-by-default using uv_build; existing projects are not automatically converted.
**Analysis:** Project bootstrap and packaging intent change which source/build objects are represented by a new project.
**Alternative / caution:** The change is scoped to newly initialized projects; no repo migration proved.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.
