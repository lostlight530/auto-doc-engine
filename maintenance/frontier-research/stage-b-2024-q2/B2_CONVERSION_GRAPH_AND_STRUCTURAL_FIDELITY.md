# Frontier Research Part B2 — Conversion Graph and Structural Fidelity

## Identity

- **Stage:** `B / 2024-Q2`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## Research question

What did Q2 Pandoc and Typst releases reveal about structural fidelity across evolving source/target formats?

## Objects and sources

- O3 Pandoc 3.1.13, released 2024-04-07
- O4 Pandoc 3.2 / 3.2.1 release line, 2024-05-11 and 2024-06-24
- O5 Typst 0.11.1, released 2024-05-17
- S5 Pandoc release history: https://www.pandoc.org/releases.html
- S6 Typst 0.11.1 changelog: https://typst.app/docs/changelog/0.11.1/

## Observations

Pandoc 3.1.13 added support for Typst 0.11 table features including row/column spans, headers/footers and alignment semantics

Pandoc 3.2 changed `--file-scope` behavior because the previous filename-derived wrapping could interfere with chunking files into chapters such as EPUB

Pandoc 3.2.1 improved DOCX caption association, task-list handling, column/cell alignment and OpenXML template customization

Typst 0.11.1 fixed bibliography handling, citation behavior, right-to-left/raw-text layout issues and other rendering details

## Analysis

The conversion graph is not a neutral byte pipe

A structural feature can require different target encodings, and conversion logic can change even when the source document remains unchanged

Q2 therefore strengthens a Stage A model:

```text
artifact output
= f(
  source revision,
  converter revision,
  target-format semantics,
  template/configuration,
  compiler/renderer revision
)
```

The function is conceptual, not complete

Pandoc's `--file-scope` change is especially useful because it shows that an implementation designed to preserve identity can itself distort higher-level structure in another target workflow

## Counterevidence and limits

No local Pandoc/Typst conversion matrix was run

Release notes establish project-described behavior, not semantic equivalence across generated formats

## Repository relation

`PARALLEL_CONVERGENCE`

Typed lineage should carry transformation identity and target semantics without turning common origin into equivalence

## Conclusion

`SUPPORTED_OBSERVATION`

Q2 continues the move from document-as-file toward document-as-versioned transformation graph

```text
same source
!= same target semantics
successful conversion
!= structurally equivalent artifact
```
