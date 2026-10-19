# Frontier Research Stage K / 2026-Q3 — 2026-09 monthly research reconstruction
- Source period: 2026-09; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Packaging and conversion-semantic identity. Evidence-object count: 2; **not** a measure of field-wide activity.
## 2026-09-28 — Semantic lock reuse (`K-O3`)
**Publisher source:** [astral-sh/uv 0.12.20](https://github.com/astral-sh/uv/releases/tag/0.12.20) (`K-S3`).
**Observed release note:** uv reports reuse of lockfiles for semantically equivalent declarations and repeated-requirement hash-check fixes.
**Analysis:** Dependency-declaration equivalence is not artifact-byte equality, document equivalence or evidence that an environment was executed.
**Alternative / caution:** No lockfile equivalence or hash-negative test was performed.

## 2026-09-29 — XML fragment versus standalone (`K-O4`)
**Publisher source:** [jgm/pandoc 3.12](https://github.com/jgm/pandoc/releases/tag/3.12) (`K-S4`).
**Observed release note:** Pandoc reports performance changes and XML writer respect for --standalone, controlling fragment output.
**Analysis:** Structural AST/XML identity needs effective flags; upstream performance claims are workload-specific.
**Alternative / caution:** No local XML replay or benchmark was run.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.
