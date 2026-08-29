# Frontier Alignment — auto-doc-engine

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-30

`auto-doc-engine` occupies the research-artifact / document-evidence plane. It is not a scientific agent and does not infer scientific truth.

## Current engineering thesis

A completed document or model-call trace is not automatically a durable research record. Before downstream reasoning, research material benefits from explicit identity, declared process context, assertion basis, dimensional audit coverage, diagnostics, portable handoff and explicit artifact lineage.

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
```

These layers are related but intentionally not collapsed.

## Basis before interpretation

Current artifact-side bases include `document-frontmatter`, `caller-declared`, `runtime-observed-local-bytes`, and `runtime-observed-local-filesystem`.

The repository does not infer AI use from text and records `automatic_ai_detection_used: false` in the artifact-record process disclosure.

```text
assertion basis != truth
explicit disclosure != AI detection
AI detection != authorship adjudication
```

## Coverage without fake quality scores

The repository implements descriptive coverage and local reference resolution only where it can compute them directly.

It does not claim provenance soundness and does not produce an aggregate research-quality score.

```text
coverage != correctness
coverage ratio != probability
local resolution != source credibility
```

## Day-6 lineage without inherited authority

`core/artifact_lineage.py` supports a bounded caller-declared relation vocabulary:

```text
derived-from
revision-of
supersedes
uses
related-to
```

Every relation keeps `scientific_validity_inherited: false` and `reproducibility_inherited: false`.

```text
supersedes != history deletion
revision-of != semantic equivalence
uses != evidence sufficiency
lineage != truth
```

## Day-7 phase-aware maintenance

Long-horizon research work increasingly shows that workflow phase and recovery structure matter independently of model capability. A behavioural study of long-horizon autonomous architecture research reports clear research phases and argues for regime-aware re-validation, while ScienceFlow organizes long-horizon research into persistent segments for continuity and recovery. Current provenance work likewise emphasizes records that can be reopened, audited and corrected.

Borrowed principle:

```text
maintenance horizon should match the type of drift being reviewed
```

The repository therefore distinguishes:

```text
daily
  local drift / new facts / bounded corrections

weekly
  cross-day contract reconciliation / history inventory / profile consistency

monthly or explicit phase-close
  canonical hash baseline / deprecation review / current-vs-history separation
```

This is implemented as `MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `core/maintenance_cadence.py`, and `STAGE_2026_08_MAINTENANCE.md`.

The scanner is deliberately read-only and local. It does not schedule itself, call GitHub, delete history, run tests, or validate science.

On 2026-08-30 the August snapshot is month-to-date, not a final calendar-month close.

```text
maintenance clean != scientific validity
weekly consistency != proof of correctness
monthly baseline != reproduction
history inventory != deprecation decision
```

## Global signals used for calibration

Current calibration includes:

- Nature Computational Science on provenance as a complete, re-openable record for autonomous science
- scientific-publishing guidance on transparent AI use and human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- Brain Researcher evidence-bounded claims
- EarthVerse end-to-end consistency gaps
- claim-level auditability separating coverage from soundness
- Praxist solution/evidence lineages
- ReproAgent persistent implementation contracts
- long-horizon autonomous architecture research with phase-aware re-validation
- ScienceFlow segmented long-horizon research and recovery
- research-software work emphasizing that software is a living research object requiring maintenance and reusable metadata

These sources are architecture calibration only. They do not validate, certify, endorse, or prove novelty for this repository.

## Relation to neighboring infrastructure

- Jupyter Book / MyST / publication systems: broader executable/structured publishing
- RO-Crate: external packaging/interoperability target
- W3C PROV / Run Crate profiles: richer execution-lineage neighbors
- scientific agents: potential producers/consumers of artifact and lineage records

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

The system-level goal is to preserve research semantics across artifact, epistemic process and scientific communication layers while preventing unsupported authority from propagating with references.

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
monthly baseline != reproduction
RO-Crate != independent reproduction
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```
