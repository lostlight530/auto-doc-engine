# Frontier Research Stage K / 2026-Q3 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| K-O1 / 0.12.0 | uv changes new uv init projects to packaged-by-default using uv_build; existing projects are not automatically converted. | Project bootstrap and packaging intent change which source/build objects are represented by a new project. | The change is scoped to newly initialized projects; no repo migration proved. |
| K-O2 / 3.11 | Pandoc introduces --math-method and MathML default, RTL improvements and a template-fetch fix. | Equation transformation and language/layout semantics depend on effective method, renderer revision and locale context. | Deprecated methods may still work; no semantic comparison executed. |
| K-O3 / 0.12.20 | uv reports reuse of lockfiles for semantically equivalent declarations and repeated-requirement hash-check fixes. | Dependency-declaration equivalence is not artifact-byte equality, document equivalence or evidence that an environment was executed. | No lockfile equivalence or hash-negative test was performed. |
| K-O4 / 3.12 | Pandoc reports performance changes and XML writer respect for --standalone, controlling fragment output. | Structural AST/XML identity needs effective flags; upstream performance claims are workload-specific. | No local XML replay or benchmark was run. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.
