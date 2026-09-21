# Evidence Chart — Stage B / 2024-Q2

## Identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Coverage:** `SEARCH_BOUNDED`
- **Charted:** `2026-09-22`

## Variables

- object/version state
- event/release date
- presentation/workspace state
- transformation semantics
- input/security boundary
- citation/structural binding
- source family
- reproduction state
- correction mode

## Findings

| ID | Observation | Objects | Evidence | Independence | Boundary |
|---|---|---|---|---|---|
| F1 | JupyterLab 4.2 exposes exportable workspace state and partial rendered-state behavior | O1 | S1-S3 | one family | workspace != reproduction |
| F2 | Notebook 7.2 carries the JupyterLab 4.2 generation into Notebook | O2 | S4 | same Jupyter family | compatibility != identical behavior |
| F3 | Pandoc 3.1.13 adapts conversion semantics to Typst 0.11 table structure | O3 | S5 | Pandoc family | support != semantic equivalence |
| F4 | Pandoc 3.2 changes file-scope behavior because prior wrapping could interfere with chunking | O4 | S5 | Pandoc family | implementation identity is version-bound |
| F5 | Typst 0.11.1 fixes out-of-project image inclusion and bibliography/citation behavior | O5 | S6 | Typst family | fix != evidence all prior artifacts affected |
| F6 | Pandoc 3.2.1 improves caption association and template semantics | O4 | S5 | Pandoc family | later repair != earlier state rewrite |

## Cross-object analysis

Three different project families converge on a common artifact-engineering problem:

```text
final bytes
do not fully encode
how state was selected, transformed, authorized, rendered and corrected
```

Jupyter contributes workspace/materialization state

Pandoc contributes transformation/target structure

Typst contributes compiler/security/citation state

## Counterevidence

No source establishes that one universal provenance schema can capture every relevant state

No cross-tool execution was performed

## Amendment

`NONE`
