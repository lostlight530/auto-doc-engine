# September 2025 Reconstruction — Structural Interchange Identity

## Monthly event
Pandoc 3.8 was released on 2025-09-06 and introduced XML input/output as an exact representation of the Pandoc AST with documented schemas. Pandoc 3.8.1 followed on 2025-09-29 as later same-project evidence.

## Historical interpretation
September adds another layer to the artifact story: the converter's internal structural representation can itself become an inspectable serialized artifact.

```text
source bytes
-> parser
-> Pandoc AST
-> JSON/XML AST serialization
-> writer
-> derivative bytes
```

This makes structural identity easier to exchange and inspect while preserving the distinction between AST identity, source bytes, output bytes, and semantic equivalence.

## Month boundary
No Pandoc 3.8/3.8.1 replay or round-trip was executed. The 3.8.1 release is retained as later same-lineage revision evidence, not independent corroboration.
