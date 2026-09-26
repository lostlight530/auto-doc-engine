# H3 — Pandoc 3.8.3: Broader Input Surface and Transformation Identity

## Source identity
- Object: Pandoc 3.8.3
- Release date: 2025-12-01
- Primary source: https://pandoc.org/releases.html

## Frontier observation
Pandoc 3.8.3 adds AsciiDoc, XLSX, and PPTX as input formats and BBCode variants as outputs. This materially broadens the kinds of source artifacts that can enter one conversion graph.

The provenance problem therefore gains another dimension:

```text
source file format
+ source-format semantics
+ parser revision
+ AST/intermediate representation
+ writer revision
+ target format
= transformation identity
```

A spreadsheet worksheet becoming a document section/table or a slide deck becoming a document representation is a transformation rule, not a claim of semantic equivalence to the source application's rendering or behavior.

## Boundary
- readable input != faithful interpretation
- parse success != semantic equivalence
- common AST != identical source semantics
- converter release note != local replay

## Repository interpretation
No XLSX/PPTX/AsciiDoc conversion was replayed here. Stage H records the identity consequence of a broader input surface.
