# G3 — Pandoc 3.8: XML AST as a Structural Interchange Surface

## Question
What does Pandoc 3.8 change about how document structure can be represented and inspected across transformations?

## Object
- Research object: Pandoc 3.8 release family
- Main event: 2025-09-06 release of 3.8
- Same-lineage follow-up: 2025-09-29 release of 3.8.1
- Source family: Pandoc project release announcements
- Authority: official release notes for project behavior
- Accessed: 2026-09-26

## Primary sources
- https://github.com/jgm/pandoc/discussions/11116
- https://github.com/jgm/pandoc/discussions/11177

## Observed 3.8 change
Pandoc 3.8 introduced an `xml` input/output format described by the project as an exact representation of a Pandoc AST in a form intended to be more human-readable than JSON, with documented XML schemas.

The same release also changed syntax-highlighting controls and included many reader/writer changes.

Pandoc 3.8.1 later added/fixed output and parser behavior, including a Vim documentation writer and fixes/regressions in the same release family.

## Interpretation
For an artifact/document pipeline, the significant event is not "XML is better than JSON." It is the appearance of another explicit serialization surface for the converter's internal structural model.

```text
source bytes
-> parser
-> Pandoc AST
-> AST serialization (JSON/XML)
-> writer
-> derivative bytes
```

This makes two identities easier to keep separate:

```text
structural representation
!= rendered/output bytes

AST equivalence
!= semantic equivalence
```

An exact representation of the Pandoc AST is exact relative to that AST model and release semantics. It is not automatically a byte-preserving representation of the original source document, and later 3.8.x changes demonstrate that reader/writer behavior remains revision-sensitive.

## Negative space
No local Pandoc 3.8 conversion or round-trip was executed. No claim is made that XML round-trips every source format without loss, or that 3.8.1 invalidates the 3.8 point-in-time release state.

## Finding
`G3_FINDING`: Q3 2025 makes transformation identity more inspectable by exposing a schema-described serialization of the converter's structural model, while simultaneously reminding us that converter revision remains part of the evidence needed to interpret that structure.
