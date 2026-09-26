# Longitudinal Frontier Synthesis — 2024 through 2025-Q3

## Identity
- Repository: `lostlight530/auto-doc-engine`
- Range: `2024-Q1 through 2025-Q3`
- Stages: A, B, C, D, E, F, G
- Synthesis date: `2026-09-26`
- Historical rewrite: NO

## Longitudinal narrative
Across seven Stages, the artifact story moves from basic research-object identity toward an increasingly explicit chain of **selection, environment, composition, transformation, publication, and relationship identity**.

```text
source / research object
-> dependency intent
-> lock
-> realized environment
-> composition / SBOM evidence
-> software/source/role/review metadata relations
-> converter revision + AST representation
-> derivative artifact
-> Research Object package
-> release asset + provenance attestation
-> mutable / immutable publication state
-> archive / citation identity
```

This is not a ladder of truth. It is a decomposition of questions that earlier workflows often collapsed.

## Stage-G delta
Stage G adds three distinctions:
1. a metadata graph can describe richer relations without verifying them;
2. publication immutability is separate from asset correctness;
3. a converter's structural interchange model is separate from source bytes, derivative bytes, and semantic equivalence.

## Durable boundaries
```text
metadata != truth
lock != SBOM
SBOM != correctness
attestation != security
immutable publication != correct publication
AST identity != source-byte identity
converter version != semantic equivalence
RO-Crate/package != independent reproduction
handoff != authority transfer
```

## Current repository relation
`NO_CURRENT_REPOSITORY_DRIFT / NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE`

Earlier longitudinal syntheses remain preserved; this file is an additive A→G extension.
