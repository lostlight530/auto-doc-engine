# H2 — SLSA 1.2: Source Track and Policy-Verifiable Provenance

## Source identity
- Object: SLSA v1.2
- Release date: 2025-11-24
- Primary source: https://slsa.dev/blog/2025/11/announce-slsa-v1.2

## Frontier observation
SLSA 1.2 introduces the Source Track, extending the model beyond build provenance into source authoring, review, and source-management threats.

For documentary lineage this adds a distinct evidence surface:

```text
source repository state
-> source-management controls
-> source provenance / history
-> build provenance
-> published artifact
```

The Source Track does not collapse source history into artifact correctness. It makes source-side controls and provenance inspectable as their own layer.

## Boundary
- SLSA track/level != source truth
- source-control evidence != scientific validity
- provenance policy != policy enforcement proof
- approved specification != local conformance

## Repository interpretation
No SLSA conformance test or source-policy enforcement was executed. The value is a sharper vocabulary for separating source identity from build/release identity.
