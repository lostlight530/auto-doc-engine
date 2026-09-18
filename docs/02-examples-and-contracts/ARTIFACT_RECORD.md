> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `CONTRACT`
> - **Role:** Current contract for artifact identity, derivative identity, declared context, and bounded reproducibility state
> - **Authority:** Current repository-native authority for the semantics explicitly owned by this file; current implementation and machine contracts remain the factual boundary for executable behavior
> - **Current meaning:** Read this subject as part of the `artifact identity → lineage/assertion basis → downstream claim/evidence handoff` architecture. It defines inspectable structure and provenance semantics without elevating generated documentation into scientific truth
> - **Evidence / implementation boundary:** Artifact identity is not semantic equivalence; lineage is caller-declared and does not inherit validity; assertion basis is not correctness; coverage is not quality or probability; process disclosure is not authorship proof; RO-Crate packaging is not reproduction
> - **Cross-document relation:** Architecture explains the integrated system; specialized contracts own their exact handoff vocabularies; current code and machine contracts bound implementation; `DOCUMENT_STATUS.md` routes current versus historical documentation
> - **Update trigger:** Update only when the owned architecture/contract semantics or implemented mechanics materially change, or when a confirmed current-authority conflict appears
> - **Preservation rule:** Existing technical explanation and stage-calibration material remains in place. Dated stage-close statements retain their historical scope and are not rewritten into current execution claims

# Artifact Record Contract — auto-doc-engine

**Profile:** `auto-doc-engine/artifact-record`  
**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-08-31

## Purpose

The artifact record fills the gap between bounded document frontmatter and broader RO-Crate 1.3 packaging. It indexes one source research document plus declared/generated derivatives without pretending to be a truth, authorship, peer-review, source-credibility, or reproduction certificate

Current implemented surfaces include

```text
assertion_basis
audit_coverage
```

They answer how a value entered the record and which handoff dimensions are present. They do not answer whether the research is correct

## Stable identifier

```text
auto-doc-engine/artifact-record
```

Project-owned identifiers remain unversioned. This does not remove real external versions such as RO-Crate 1.3

## Canonical relationship

```text
Markdown frontmatter
        ↓
source document bytes
        ├─ frontmatter diagnostics
        ├─ process disclosure
        ├─ declared source refs
        ├─ derivative identities
        └─ execution/config references
        ↓
auto-doc-engine/artifact-record
        ├─ assertion basis
        ├─ reference-resolution states
        ├─ dimensional audit coverage
        ├─ optional artifact-lineage
        ├─ optional downstream handoff
        └─ optional RO-Crate 1.3 packaging as ordinary payload
```

## Example shape

```json
{
  "profile": "auto-doc-engine/artifact-record",
  "artifact_id": "analysis-042",
  "source_artifact": {
    "path": "analysis.md",
    "file_sha256": "sha256:...",
    "identity_basis": "runtime-observed-local-bytes"
  },
  "process_disclosure": {
    "basis": "document-frontmatter",
    "automatic_ai_detection_used": false
  },
  "assertion_basis": {},
  "audit_coverage": {
    "dimensions": {},
    "aggregate_score": null
  },
  "reproducibility": {"level": "R1"},
  "scientific_validity_claim": false
}
```

The record indexes identities/context; source prose is not embedded by default

## Identity semantics

`file_sha256` identifies recorded local bytes. `metadata_canonical_sha256` identifies the selected normalized metadata mapping

```text
byte identity != semantic equivalence
metadata identity != factual correctness
```

## Assertion-basis semantics

Implemented bases include

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
not_declared
```

Typical mapping

| Surface | Basis |
|---|---|
| source/derivative SHA-256 | runtime-observed local bytes |
| document metadata/authors/sources | document frontmatter |
| process disclosure | document frontmatter |
| `generated_with` | caller-declared when supplied |
| lineage refs | caller-declared with optional local resolution |

```text
assertion basis != external verification
assertion basis != truth
```

## Process disclosure

The record preserves

```text
ai_assistance: none | used | not_declared
ai_tools[]
human_review: reviewed | partial | not_reviewed | not_declared
disclosure_ref
```

The current path explicitly records

```json
{"automatic_ai_detection_used": false}
```

The repository does not infer AI use from prose

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
AI tool label != verified model provenance
human review != peer review
```

## Reference handling

- existing local files may be hashed and marked `local-file`
- URIs remain opaque and are not dereferenced
- unresolved strings remain explicit unresolved/opaque references

Local resolution is an observation about the current environment, not source credibility

## Dimensional audit coverage

The record may summarize

```text
derivative_count
declared_source_references: total / by_resolution / local_file_ratio
lineage_references: total / by_resolution / local_file_ratio
process_disclosure_declared_fields
frontmatter_error_count
frontmatter_warning_count
```

No aggregate quality score is computed

```json
{"aggregate_score": null}
```

```text
coverage != correctness
coverage ratio != probability
local_file_ratio != source credibility
reference presence != citation validity
```

## Diagnostics boundary

Embedded validation reflects only the bounded frontmatter validator

```text
frontmatter clean != factual correctness
frontmatter clean != source credibility
frontmatter clean != scientific validity
```

## Reproducibility levels

- **R0 Traceable** — source/artifact association recorded
- **R1 Replay-addressable** — declared input/config/tool identity addresses intended replay
- **R2 Environment-bounded** — important runtime/dependency assumptions bounded
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion

`artifact_record.py` can carry a caller-declared level but cannot self-award R3

## Standalone use

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

## Relation to artifact lineage and RO-Crate

```text
auto-doc-engine/artifact-record
        ↓ optional relation
auto-doc-engine/artifact-lineage
        ↓ optional packaging
RO-Crate 1.3
```

RO-Crate 1.3 is the external Research Object packaging target. Project records may be packaged as ordinary File payloads but remain project-owned contracts

## Cross-repository role

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

No direct Python import is required and no scientific authority is inherited through a reference

## Document / stage status

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`

The August stage is closed as of 2026-08-31, but calendar/stage closure does not alter artifact-record scientific semantics or establish reproduction

## Hard boundaries

```text
Artifact record != Research Object standard
Artifact record != W3C PROV graph
Assertion basis != correctness
Coverage != quality
Coverage ratio != probability
Hash identity != semantic equivalence
Declared source != credible source by definition
Process disclosure != AI detection
Process disclosure != authorship proof
Human review != peer review
Metadata != independent reproduction
Calendar-month close != reproduction
Provenance != truth
```
