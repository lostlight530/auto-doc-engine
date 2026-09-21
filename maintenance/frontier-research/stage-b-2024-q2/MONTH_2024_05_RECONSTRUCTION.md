# Stage B Month Reconstruction — 2024-05

## Scope

May 2024 within the auto-doc research-artifact lens

## Evidence anchors

- JupyterLab 4.2.0 released 2024-05-06
- Pandoc 3.2 released 2024-05-11
- Notebook 7.2.0 released 2024-05-16
- Typst 0.11.1 released 2024-05-17

## Interpretation

May brings several previously implicit artifact dimensions into direct view

JupyterLab makes workspace export/import and partial rendering behavior explicit

Pandoc changes file-scope behavior to avoid structural interference with chapter chunking

Typst fixes an out-of-project image inclusion vulnerability and bibliography/citation behavior

Notebook 7.2 carries the JupyterLab 4.2 generation into the notebook application line

The combined story is not “documents got better”

It is that artifact state now visibly depends on:

```text
workspace
+ source structure
+ converter semantics
+ renderer/compiler
+ path boundary
+ citation transformation
```

## Boundary

No selected release proves reproducibility, scientific validity, or universal accessibility
