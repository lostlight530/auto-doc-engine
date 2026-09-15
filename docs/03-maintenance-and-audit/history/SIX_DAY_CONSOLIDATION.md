# Six-Day Consolidation — auto-doc-engine

**Date:** 2026-08-29  
**Status:** research-engineering consolidation note

## Day-6 change

The first five days established artifact identity, bounded process disclosure, assertion basis and dimensional audit coverage. Day 6 adds an explicit **artifact lineage / inheritance plane**.

```text
source / derivative identity
        ↓
auto-doc-engine/artifact-record
        ↓
auto-doc-engine/artifact-lineage
        ↓
optional downstream claim/evidence workflows
```

The new `core/artifact_lineage.py` preserves caller-declared typed relations to predecessor/related artifacts while refusing to inherit scientific validity or reproducibility automatically.

## Why this layer exists

A portable artifact can still lose research history if a later system only sees the latest file. Long-running research needs a small inspectable statement of:

```text
what this artifact derives from
what it revises
what it supersedes
what it uses
what it is merely related to
```

Without those semantics, downstream agents may reconstruct history from filenames or prose and silently invent inheritance.

## Implemented relation vocabulary

```text
derived-from
revision-of
supersedes
uses
related-to
```

Each relation has caller-declared basis and optional local-file resolution/hash.

## Explicit non-inheritance

```text
scientific_validity_inherited: false
reproducibility_inherited: false
```

This keeps lineage separate from truth and reproduction.

## Global research calibration

Day 6 was rechecked against:

- Praxist (arXiv:2608.25955, 26 Aug 2026), which materializes solution lineages across research generations;
- ReproAgent (arXiv:2608.24291, 25 Aug 2026), which preserves implementation requirements and reference evidence through a persistent contract;
- provenance-grounded autonomous science and claim-level auditability work already referenced by the repository.

The repository implements only a bounded artifact-lineage handoff. It does not reproduce Praxist's generational research system or ReproAgent's paper-to-code workflow.

## Six-day architecture position

```text
identity
+ disclosure
+ assertion basis
+ audit coverage
+ typed artifact lineage
        ↓
research artifact handoff
```

## Boundaries

```text
lineage != truth
inheritance != validation
supersedes != deletion
revision != semantic equivalence
coverage != quality
metadata != reproduction
```

No GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge gates are part of this consolidation. Test execution is not used as completion evidence.
