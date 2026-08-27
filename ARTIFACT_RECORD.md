# Artifact Record Contract — auto-doc-engine

**Profile:** `auto-doc-engine/artifact-record`  
**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-08-27

## 1. Purpose

The artifact record fills the practical gap between bounded document frontmatter and broader RO-Crate 1.3 packaging. It provides a small machine-readable object for one source research document plus declared/generated derivatives.

It can answer:

- which source bytes were recorded;
- which derivative files were recorded;
- which source references were declared;
- which process-disclosure fields were declared;
- which bounded frontmatter diagnostics were observed;
- which configuration/provenance/validation references were supplied;
- which local reproducibility level was declared.

## 2. Stable identifier

```text
auto-doc-engine/artifact-record
```

Do not append `@1`, `@2` or `/v1` to this project-owned profile. Compatibility is defined by documented fields and semantics.

This does not affect real external versions such as RO-Crate 1.3.

## 3. Relationship

```text
Markdown frontmatter
        ↓
source document bytes
        ├─ frontmatter diagnostics
        ├─ process disclosure
        ├─ declared source refs
        ├─ derivative file hashes
        └─ execution/config references
        ↓
auto-doc-engine/artifact-record
        ├─ optional downstream research handoff
        └─ optional RO-Crate 1.3 packaging as ordinary payload
```

The artifact record is not a replacement for RO-Crate, W3C PROV, a workflow-run profile, a methods section or peer review.

## 4. Example shape

```json
{
  "profile": "auto-doc-engine/artifact-record",
  "artifact_id": "analysis-042",
  "source_artifact": {
    "kind": "source-document",
    "path": "analysis.md",
    "file_sha256": "sha256:..."
  },
  "derivatives": [],
  "declared_sources": [],
  "process_disclosure": {},
  "validation": {},
  "lineage": {},
  "reproducibility": {"level": "R1"},
  "scientific_validity_claim": false
}
```

The record indexes identities and metadata; it does not embed source prose by default.

## 5. Identity semantics

`file_sha256` identifies recorded local file bytes. `metadata_canonical_sha256` identifies the selected normalized metadata mapping.

Neither proves semantic equivalence, source credibility, authorship, correctness, novelty or scientific validity.

## 6. Process disclosure

The record preserves the bounded vocabulary:

```text
ai_assistance: none | used | not_declared
ai_tools[]
human_review: reviewed | partial | not_reviewed | not_declared
disclosure_ref
```

Unknown values remain unknown/not-declared.

```text
AI disclosure != authorship adjudication
AI tool label != verified model provenance
human review != peer review
human review != scientific validation
```

## 7. Reference handling

- existing local files can be hashed and marked as local files;
- URIs are retained as opaque references without automatic dereferencing;
- unresolved strings remain explicit unresolved/opaque references.

Record generation therefore does not hide network access as a dependency.

## 8. Diagnostics boundary

Embedded validation reflects only the bounded frontmatter validator.

```text
frontmatter clean != factual correctness
frontmatter clean != source credibility
frontmatter clean != scientific validity
```

## 9. Reproducibility levels

Local project terms:

- **R0 Traceable** — source/artifact association is recorded;
- **R1 Replay-addressable** — declared input/configuration/tool identity addresses intended replay;
- **R2 Environment-bounded** — important runtime/dependency assumptions are also bounded;
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

`artifact_record.py` may carry a caller-declared level but does not perform a rerun and cannot self-award R3.

## 10. Standalone use

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

## 11. SyncEngine use

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

Artifact-record output remains opt-in.

## 12. Relation to RO-Crate 1.3

RO-Crate 1.3 is the external Research Object packaging target. The artifact record is project-owned JSON.

If both are emitted, the artifact record may be included in the crate as an ordinary File payload. Packaging identity does not make the custom JSON object an RO-Crate standard profile.

## 13. Cross-repository role

```text
auto-doc-engine/artifact-record
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-evidence
```

No direct Python import between repositories is required.

## 14. Hard boundaries

```text
Artifact record != Research Object standard
Artifact record != W3C PROV graph
Artifact record != workflow-run provenance profile
Hash identity != semantic equivalence
Declared source != credible source by definition
Process disclosure != authorship proof
Human review != peer review
Metadata != independent reproduction
Provenance != truth
```
