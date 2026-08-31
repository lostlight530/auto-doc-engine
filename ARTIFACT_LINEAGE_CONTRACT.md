# Artifact Lineage Contract — auto-doc-engine

**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-09-01  
**Implementation:** `core/artifact_lineage.py`

## Purpose

`auto-doc-engine/artifact-lineage` records how one existing artifact record is declared to relate to predecessor or related artifacts.

Long-lived research needs to preserve whether a later artifact derives from, revises, supersedes, uses, or is merely related to another artifact.

This is a lineage contract, not a scientific-validity or semantic-equivalence engine.

## Stable profile

```text
auto-doc-engine/artifact-lineage
```

Project-owned identifiers remain unversioned. Real external standard/runtime versions remain explicit when actually relevant.

## Allowed relations

```text
derived-from
revision-of
supersedes
uses
related-to
```

Semantics are deliberately bounded:

- `derived-from`: caller declares a derivation relationship; this is not proof of complete provenance;
- `revision-of`: caller declares revision history; this is not semantic equivalence;
- `supersedes`: caller declares replacement intent; history is not deleted and the predecessor is not automatically invalidated;
- `uses`: caller declares a dependency/use relationship; this is not evidence sufficiency;
- `related-to`: caller declares a weak relationship with no stronger implication.

## Input-type boundary

The source JSON must carry the expected `auto-doc-engine/artifact-record` profile.

A parseable but wrong-profile JSON input fails explicitly rather than being guessed into an artifact record.

The exact source artifact-record sidecar bytes are bound through SHA-256 in the emitted lineage record.

## Self-reference boundary

As of 2026-09-01, a local lineage target that resolves to the source artifact-record sidecar itself fails explicitly.

```text
source artifact-record -> revision-of -> same source artifact-record
```

is not a meaningful lineage edge and is rejected rather than silently recorded as a self-loop.

This check is deliberately narrow. It does **not** infer whether two different files are semantically identical, duplicated, or revisions of one another.

## Reference handling

Local target files may be hashed with SHA-256. URI/opaque references are retained without network dereference.

```text
local-file resolution != source credibility
hash match != semantic equivalence
reference existence != scientific validity
```

## Assertion basis

Artifact identity is runtime-observed from local bytes. Relation labels and targets are caller-declared.

```text
artifact_identity: runtime-observed-local-bytes
relations: caller-declared-with-optional-local-resolution
basis_inferred: false
```

The repository does not infer relationships from filenames, timestamps, prose similarity, Git history, or model output.

## Coverage

The lineage sidecar records relation counts, relation-vocabulary counts, reference-resolution counts, and a local-file ratio.

```text
aggregate_score: null
```

Coverage is descriptive only. It is not provenance soundness, novelty, reproducibility, correctness, or probability of validity.

## Non-inheritance rule

Every relation explicitly carries:

```text
scientific_validity_inherited: false
reproducibility_inherited: false
```

A successor artifact does not become scientifically valid because it references a predecessor, and a reproduced predecessor does not automatically make a modified successor reproduced.

## CLI

```bash
python core/artifact_lineage.py output/report.artifact.json \
  --relation revision-of=archive/report-v1.artifact.json \
  --relation uses=data/input-dataset.json \
  --output output/report.lineage.json
```

## Cross-repository role

Artifact lineage may travel with artifact-record references into the downstream evidence stack, but downstream repositories do not inherit scientific validity or reproduction status.

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/claim-transfer
  -> epistemic-pipeline/evidence-envelope
```

## Research calibration

Current design is informed by work such as Praxist on solution/evidence lineage, ReproAgent on persistent contracts across long research trajectories, and scientific-agent evaluation showing that terminal success can hide intermediate structural defects.

The borrowed principle is narrow: identity, inheritance boundaries, and invalid structural relationships should remain explicit and inspectable.

These works do not certify this repository, define this contract, or establish scientific correctness.

## Document / stage status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`.

The August research-infrastructure stage remains closed as of 2026-08-31. The 2026-09-01 repair hardens the closed-stage implementation and does not reopen or rewrite that stage.

## Hard boundaries

```text
Lineage != Truth
Reference != Inheritance of validity
Self-reference rejection != Complete cycle detection
Supersedes != History deletion
Revision != Semantic equivalence
Uses != Evidence sufficiency
Hash != Reproduction
Coverage != Quality score
Calendar-month close != Reproduction
```
