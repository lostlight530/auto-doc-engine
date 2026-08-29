# August 2026 Research-Maintenance Stage — auto-doc-engine

**Window represented:** 2026-08-24 through 2026-08-30  
**Calendar-month status:** month-to-date, not final August close  
**Role:** current stage index plus weekly/monthly maintenance baseline

## Stage progression

```text
Day 1
frontier positioning and evidence-aware artifact-plane clarification

Day 2
process disclosure and claim-aware downstream handoff alignment

Day 3 / 4
portable artifact-record and runtime-consumed contracts

Day 5
assertion basis and dimensional audit coverage

Day 6
explicit artifact lineage and non-inheritance boundaries

Day 7 / stage maintenance
formal daily / weekly / monthly maintenance cadence
```

Historical `*_DAY_CONSOLIDATION.md` files remain historical snapshots

This file does not replace or rewrite them

## Current canonical artifact stack

```text
frontmatter
      ↓
auto-doc-engine/artifact-record
  identity
  process disclosure
  assertion basis
  dimensional audit coverage
      ↓
auto-doc-engine/artifact-lineage
  typed declared relations
  non-inheritance boundaries
      ↓
optional RO-Crate 1.3 packaging
      ↓
reference handoff to epistemic-pipeline
```

## Weekly consolidation — 2026-08-24 → 2026-08-30

The week's merged work establishes six durable rules

1. project-owned profiles use stable semantic names without decorative internal versions
2. unknown provider/model/version/source/review values remain unknown rather than guessed
3. process disclosure is explicit declaration, not AI-content detection
4. coverage is dimensional and `aggregate_score` remains null
5. lineage is typed and caller-declared, not inferred from filenames or prose
6. references and lineage never inherit scientific validity or reproducibility

## Daily maintenance baseline

A normal daily pass should primarily inspect

```text
MANIFEST.yaml
AGENTS.md
RESEARCH_CONTRACT.md
FRONTIER_ALIGNMENT.md
ARTIFACT_RECORD.md
ARTIFACT_LINEAGE_CONTRACT.md
core/artifact_record.py
core/artifact_lineage.py
```

Daily work should remain bounded unless source truth demonstrates a broader architecture drift

## Weekly maintenance baseline

Weekly review should reconcile

```text
implementation
↔ machine Manifest
↔ active Research Contract
↔ Agent maintenance rules
↔ Frontier Alignment
↔ cross-repository profile names
```

Historical consolidation files are inputs to review, not rewrite targets

## Monthly / phase-close baseline

At month close or explicit phase close

- inventory all historical stage snapshots
- hash the canonical paths using `core/maintenance_cadence.py monthly`
- review current / experimental / proposed / not-integrated labels
- review obsolete-document candidates manually
- confirm current cross-repository handoff names
- record whether the phase is actually closed

No automatic deletion is permitted

## Current cross-repository handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

## Current external calibration

The current stage is informed by 2026 work on

- re-openable provenance for autonomous science
- transparent AI use and human oversight in scientific publishing
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- claim-level auditability
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style segmented recovery
- Praxist solution/evidence lineage
- ReproAgent persistent implementation contracts
- reusable research-software metadata and maintenance

External work is calibration only

```text
external research != repository validation
adjacent architecture != endorsement
recent publication != reason to change code automatically
```

## Stage boundaries

```text
artifact identity != truth
assertion basis != correctness
coverage != quality
lineage != scientific inheritance
weekly reconciliation != scientific verification
monthly baseline != reproduction
```
