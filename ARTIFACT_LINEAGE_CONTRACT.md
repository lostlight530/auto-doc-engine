# Artifact Lineage Contract — auto-doc-engine

**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-08-29  
**Implementation:** `core/artifact_lineage.py`

## Purpose

`auto-doc-engine/artifact-lineage` records how one existing artifact record is declared to relate to predecessor or related artifacts.

The problem is not only whether an artifact can be identified. Long-lived research also needs to preserve which artifact a later artifact derives from, revises, supersedes, uses, or is merely related to.

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

- `derived-from`: caller declares a derivation relationship; this is not proof of complete provenance.
- `revision-of`: caller declares revision history; this is not semantic equivalence.
- `supersedes`: caller declares replacement intent; history is not deleted and the predecessor is not automatically invalidated.
- `uses`: caller declares a dependency/use relationship; this is not evidence sufficiency.
- `related-to`: caller declares a weak relationship with no stronger implication.

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

The lineage sidecar records relation counts, relation vocabulary counts, reference-resolution counts and a local-file ratio.

```text
aggregate_score: null
```

Coverage is descriptive only. It is not provenance soundness, novelty, reproducibility, correctness, or a probability of validity.

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

## Global calibration

Two recent systems sharpen this need:

- **Praxist: From Experimental Artifacts to Solution Lineages** (arXiv:2608.25955, 26 Aug 2026) organizes long-running autonomous R&D around typed evidence/solution lineage rather than isolated attempts.
- **ReproAgent: Contract-Guided Paper-to-Code Reproduction** (arXiv:2608.24291, 25 Aug 2026) uses persistent contracts so implementation requirements and reference evidence survive across generation/repair stages.

We borrow only the architectural lesson that inheritance must be explicit and inspectable. These works do not certify this repository, define this contract, or establish scientific correctness.

## Hard boundaries

```text
Lineage != Truth
Reference != Inheritance of validity
Supersedes != History deletion
Revision != Semantic equivalence
Uses != Evidence sufficiency
Hash != Reproduction
Coverage != Quality score
```
