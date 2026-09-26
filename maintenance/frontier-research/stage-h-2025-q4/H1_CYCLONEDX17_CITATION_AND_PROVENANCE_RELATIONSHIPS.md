# H1 — CycloneDX 1.7: Citation, Provenance, and BOM Relationship Identity

## Source identity
- Object: CycloneDX 1.7
- Release date: 2025-10-21
- Primary source: https://cyclonedx.org/news/cyclonedx-v1.7-released/
- Specification overview: https://cyclonedx.org/specification/overview/
- Historical summary: https://cyclonedx.org/about/history/

## Frontier observation
CycloneDX 1.7 expands a BOM from inventory toward richer traceability. The project describes v1.7 as the first CycloneDX specification supporting citations and highlights stronger provenance traceability, attribution, and auditability.

For auto-doc-engine, the useful relation is not “CycloneDX makes documents trustworthy.” It is narrower: a documentary evidence package can represent where a statement or enrichment came from with more explicit source relationships.

```text
artifact
-> BOM object
-> citation/reference
-> provenance relation
-> attributable evidence path
```

## Boundary
- citation present != cited proposition true
- provenance trace != semantic equivalence
- auditability != audit performed
- standard support != repository implementation

## Repository interpretation
This is a documentary frontier calibration only. No CycloneDX 1.7 parser, emitter, validator, or conformance run was executed in this repository.
