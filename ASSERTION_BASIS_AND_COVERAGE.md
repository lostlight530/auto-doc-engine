# Assertion Basis & Audit Coverage Contract — auto-doc-engine

**Calibration:** 2026-08-31  
**Status:** implemented companion contract for `auto-doc-engine/artifact-record`

## Purpose

A machine-readable research artifact should not only say what a field contains. It should also make clear where that value came from and which evidence dimensions are actually present

This repository distinguishes

```text
asserted value
      !=
assertion basis
      !=
scientific validity
```

and

```text
coverage of recorded metadata
      !=
quality / correctness / probability
```

## Assertion basis

Current artifact-record bases are deliberately small and concrete

| Surface | Basis |
|---|---|
| source/derivative SHA-256 | `runtime-observed-local-bytes` |
| document metadata | `document-frontmatter` |
| declared authors | `document-frontmatter` |
| declared sources | `document-frontmatter-with-optional-local-resolution` |
| process disclosure | `document-frontmatter` |
| `generated_with` | `caller-declared` when supplied |
| configuration/provenance/validation refs | caller-declared, with optional local resolution |

A basis records how the repository obtained the value. It does not prove the value is correct

```text
document-frontmatter
  means the document declared it
  does not mean an external party verified it

runtime-observed-local-bytes
  means the repository hashed bytes available locally
  does not mean those bytes are scientifically correct
```

## AI-use disclosure boundary

The artifact record explicitly emits

```json
{
  "automatic_ai_detection_used": false
}
```

The repository does not inspect prose and infer whether AI was used. `ai_assistance`, `ai_tools`, and `human_review` are declaration-backed process metadata

```text
AI disclosure != AI detection
AI detection != authorship adjudication
AI disclosure != output validity
human review != peer review
```

## Dimensional artifact coverage

`artifact-record` emits `audit_coverage` with separate dimensions

- derivative artifact count
- declared-source reference count and resolution states
- lineage reference count and resolution states
- process-disclosure fields actually declared
- frontmatter error/warning counts

For local-reference dimensions a local-file ratio may be reported

```text
local_file_ratio
```

Its meaning is narrow: fraction of declared references that resolved to local files at record-generation time

It is not source credibility, citation validity, evidence sufficiency, network availability, completeness of the research process, or probability of correctness

## No aggregate quality score

The record intentionally emits

```json
{
  "aggregate_score": null
}
```

A derivative count, reference-resolution ratio, metadata declaration, and validation warning are different kinds of facts. Collapsing them into one score would create an unsupported ordering of research quality

## Relation to artifact lineage

Artifact lineage has its own descriptive relation/reference coverage

```text
artifact-record coverage != lineage coverage
lineage coverage != provenance soundness
```

Neither surface becomes a scientific-quality score

## Relation to maintenance coverage

The maintenance scanner can inventory canonical paths, historical snapshots, and hashes, but that is repository-maintenance structure rather than artifact evidence quality

```text
maintenance completeness != artifact correctness
calendar-month close != reproduction
```

## Relation to current research-agent work

The design is informed by external directions without claiming endorsement or conformance

- claim-level auditability emphasizes provenance coverage and contradiction transparency
- artifact-centered scientific-agent observability argues for portable artifact/claim relations beyond model-call logs
- trajectory-to-evidence work distinguishes completed execution from qualified evidence
- evidence-bounded research agents emphasize explicit qualification
- end-to-end scientific-agent evaluations show strong local task performance can coexist with weak global consistency
- scientific-publishing guidance emphasizes transparency, accountability, and human oversight
- AI-text detector research/reports reinforce that detection and disclosure are different problems

The repository response remains narrower: record artifact identity, assertion basis, dimensional coverage, and explicit scientific-integrity boundaries

## Document / stage status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`

The August stage closed on 2026-08-31. Stage closure changes maintenance status only and does not change the meaning of assertion basis or coverage

## Hard boundaries

```text
Assertion basis != truth
Declaration != external verification
Local resolution != source credibility
Coverage != correctness
Coverage ratio != probability
Process disclosure != authorship adjudication
Human review != peer review
Artifact record != external Research Object standard
RO-Crate packaging != independent reproduction
Maintenance clean != scientific validity
Calendar-month close != reproduction
```
