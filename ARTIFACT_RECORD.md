# Artifact Record Contract — auto-doc-engine

**Profile:** `auto-doc-engine/artifact-record`  
**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-08-28

## Purpose

The artifact record fills the gap between bounded document frontmatter and broader RO-Crate 1.3 packaging. It indexes one source research document plus declared/generated derivatives without pretending to be a truth, authorship, peer-review, source-credibility or reproduction certificate.

Day 5 adds two implemented surfaces:

```text
assertion_basis
audit_coverage
```

They answer **how a value entered the record** and **which handoff dimensions are present**. They do not answer whether the research is correct.

## Stable identifier

```text
auto-doc-engine/artifact-record
```

Project-owned identifiers remain unversioned. This does not remove real external versions such as RO-Crate 1.3.

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

The record indexes identities/context; source prose is not embedded by default.

## Identity semantics

`file_sha256` identifies recorded local bytes. `metadata_canonical_sha256` identifies the selected normalized metadata mapping.

```text
byte identity != semantic equivalence
metadata identity != factual correctness
```

## Assertion-basis semantics

Implemented bases include:

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
not_declared
```

Typical mapping:

| Surface | Basis |
|---|---|
| source/derivative SHA-256 | runtime-observed local bytes |
| document metadata/authors/sources | document frontmatter |
| process disclosure | document frontmatter |
| `generated_with` | caller-declared when supplied |
| lineage refs | caller-declared with optional local resolution |

A basis records the acquisition path only:

```text
assertion basis != external verification
assertion basis != truth
```

## Process disclosure

The record preserves:

```text
ai_assistance: none | used | not_declared
ai_tools[]
human_review: reviewed | partial | not_reviewed | not_declared
disclosure_ref
```

The current path explicitly records:

```json
{"automatic_ai_detection_used": false}
```

The repository does not infer AI use from prose.

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
AI tool label != verified model provenance
human review != peer review
```

## Reference handling

- existing local files may be hashed and marked `local-file`;
- URIs remain opaque and are not dereferenced;
- unresolved strings remain explicit unresolved/opaque references.

Local resolution is an observation about the current environment, not source credibility.

## Dimensional audit coverage

The record may summarize:

```text
derivative_count
declared_source_references: total / by_resolution / local_file_ratio
lineage_references: total / by_resolution / local_file_ratio
process_disclosure_declared_fields
frontmatter_error_count
frontmatter_warning_count
```

No aggregate quality score is computed:

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

Embedded validation reflects only the bounded frontmatter validator.

```text
frontmatter clean != factual correctness
frontmatter clean != source credibility
frontmatter clean != scientific validity
```

## Reproducibility levels

- **R0 Traceable** — source/artifact association recorded;
- **R1 Replay-addressable** — declared input/config/tool identity addresses intended replay;
- **R2 Environment-bounded** — important runtime/dependency assumptions bounded;
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

`artifact_record.py` can carry a caller-declared level but cannot self-award R3.

## Standalone use

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

## Relation to RO-Crate 1.3

RO-Crate 1.3 is the external Research Object packaging target. An artifact record can be packaged as an ordinary File payload, but remains a project-owned JSON contract.

## Cross-repository role

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

No direct Python import is required.

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
Provenance != truth
```
