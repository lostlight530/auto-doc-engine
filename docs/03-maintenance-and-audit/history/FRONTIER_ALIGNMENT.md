# Frontier Alignment — auto-doc-engine

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-31  
**Closed stage:** 2026-08-24 through 2026-08-31

`auto-doc-engine` occupies the research-artifact / document-evidence plane. It is not a scientific agent and does not infer scientific truth

## Current engineering thesis

A completed document or model-call trace is not automatically a durable research record. Before downstream reasoning, research material benefits from explicit identity, declared process context, assertion basis, dimensional audit coverage, diagnostics, portable handoff, explicit artifact lineage, and a maintenance model that preserves current-vs-historical document roles

```text
source material
  -> structured binding
  -> typed document structure
  -> structural-change evidence
  -> metadata/reference diagnostics
  -> declared process context
  -> rendered derivatives
  -> artifact-record
       ├─ assertion basis
       └─ dimensional audit coverage
  -> artifact-lineage
       ├─ typed declared relations
       └─ non-inheritance boundaries
  -> optional RO-Crate 1.3 package

repository state
  -> phase-aware maintenance
       ├─ daily local drift
       ├─ weekly current-document reconciliation
       └─ monthly / phase-close baseline
```

## Distinct objects

```text
frontmatter
  what the document declares about itself

auto-doc-engine/artifact-record
  bounded project handoff for one source/derivative set

auto-doc-engine/artifact-lineage
  typed relationship layer across artifact generations

RO-Crate 1.3
  external Research Object packaging

maintenance-report
  local structural maintenance evidence
```

These layers are related but intentionally not collapsed

## Basis before interpretation

Current artifact-side bases include `document-frontmatter`, `caller-declared`, `runtime-observed-local-bytes`, and `runtime-observed-local-filesystem`

The repository does not infer AI use from text and records `automatic_ai_detection_used: false` in artifact-record process disclosure

```text
assertion basis != truth
explicit disclosure != AI detection
AI detection != authorship adjudication
```

## Coverage without fake quality scores

The repository implements descriptive coverage and local-reference resolution only where it can compute them directly

It does not claim provenance soundness and does not produce an aggregate research-quality score

```text
coverage != correctness
coverage ratio != probability
local resolution != source credibility
```

## Explicit lineage without inherited authority

`core/artifact_lineage.py` supports a bounded caller-declared relation vocabulary

```text
derived-from
revision-of
supersedes
uses
related-to
```

Every relation keeps `scientific_validity_inherited: false` and `reproducibility_inherited: false`

```text
supersedes != history deletion
revision-of != semantic equivalence
uses != evidence sufficiency
lineage != truth
```

## Phase-aware maintenance and document authority

Long-horizon research increasingly makes a distinction between final output quality and the process by which a long run progresses, stalls, recovers, or reuses prior experience

Current relevant signals include

- long-horizon autonomous architecture research reporting phase structure and motivating regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery from dead ends
- process-level long-horizon evaluation arguing that final scores alone hide where progress/regression occurs
- provenance work emphasizing complete re-openable records that can be audited and corrected
- research-software work treating software as a living research object that needs maintenance and reusable metadata

Borrowed principle

```text
maintenance horizon should match the kind of drift being reviewed
and current authority should remain distinguishable from historical evidence
```

The repository therefore distinguishes

```text
daily
  local drift / new facts / bounded correction

weekly
  full current-document / contract reconciliation
  historical inventory without rewrite

monthly / explicit phase-close
  canonical baseline / document-status review / deprecation candidates
```

This is implemented through `MAINTENANCE_CADENCE.md`, `DOCUMENT_STATUS.md`, `maintenance/cadence.yaml`, `core/maintenance_cadence.py`, and `STAGE_2026_08_MAINTENANCE.md`

The scanner is local and read-only. It does not schedule itself, call GitHub, delete history, run tests, or validate science

For the closed August stage

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

```text
maintenance clean != scientific validity
weekly consistency != proof of correctness
calendar-month close != reproduction
history inventory != deprecation decision
```

## Global signals used for calibration

Current calibration includes

- Nature Computational Science on provenance as a complete, re-openable record for autonomous science
- scientific-publishing guidance on transparent AI use and human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- EarthVerse-style end-to-end consistency gaps
- claim-level auditability separating coverage from soundness
- Praxist solution/evidence lineages
- ReproAgent persistent implementation contracts
- long-horizon autonomous architecture research with phase-aware re-validation
- ScienceFlow segmented long-horizon research and recovery
- Beyond Final Scores-style process evaluation beyond terminal metrics
- research-software work emphasizing living software, maintenance, and reusable metadata

These sources are architecture calibration only. They do not validate, certify, endorse, or prove novelty for this repository

## Relation to neighboring infrastructure

- Jupyter Book / MyST / publication systems: broader executable/structured publishing
- RO-Crate: external packaging/interoperability target
- W3C PROV / Run Crate profiles: richer execution-lineage neighbors
- scientific agents: potential producers/consumers of artifact and lineage records
- long-horizon research runtimes: neighbors for durable state, stage segmentation, and recovery, not direct equivalents

## Cross-repository position

```text
auto-doc-engine/artifact-record
        ↓
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
        ↓
epistemic-pipeline/claim-transfer
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
        ↓
sci-render-kit/figure-evidence
        ↓
sci-render-kit/communication-transfer
```

The system-level goal is to preserve research semantics across artifact, epistemic process, and scientific communication layers while preventing unsupported authority from propagating with references

## Document-history boundary

Current authority is mapped in `DOCUMENT_STATUS.md`

Historical Day-N consolidation files remain evidence of earlier repository states and are not current contracts

```text
historical snapshot != current contract
later architecture != permission to rewrite history
```

## Hard boundaries

```text
provenance != truth
metadata != evidence credibility
hash identity != semantic equivalence
assertion basis != correctness
coverage != quality
coverage ratio != probability
lineage != inherited scientific validity
supersedes != history deletion
maintenance clean != scientific validity
calendar-month close != reproduction
RO-Crate != independent reproduction
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```
