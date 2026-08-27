# Artifact Record Contract — 2026-08-27

**Profile:** `auto-doc-engine/artifact-record@1`  
**Status:** implemented project-owned handoff contract  
**Scope:** one source research document plus declared/generated derivative artifacts

## 1. Why this exists

`auto-doc-engine` already has two useful metadata layers:

1. bounded YAML frontmatter inside a document;
2. optional RO-Crate 1.3 packaging for a broader Research Object.

There is a practical gap between them. A downstream research tool often needs a
small machine-readable object answering:

- Which exact source bytes produced this handoff?
- Which derivative files were generated?
- Which source references were declared?
- Which process-disclosure fields were declared?
- What frontmatter/schema diagnostics were observed?
- Which configuration/provenance/validation references were supplied?
- What local reproducibility level is being claimed?

Creating a full RO-Crate for every single document transition is not always
necessary. `artifact-record@1` fills that gap.

## 2. Canonical relationship

```text
Markdown frontmatter
        |
        v
source document bytes
        |
        +--> frontmatter diagnostics
        +--> process disclosure
        +--> declared source refs
        +--> derivative file hashes
        +--> execution/config references
        |
        v
auto-doc-engine/artifact-record@1
        |
        +--> downstream epistemic/research tools
        |
        `--> optional RO-Crate 1.3 packaging as an ordinary payload
```

The artifact record is **not** a replacement for RO-Crate, W3C PROV, a workflow
run profile, a journal methods section, or peer review.

## 3. Record shape

A typical record contains:

```json
{
  "profile": "auto-doc-engine/artifact-record@1",
  "artifact_id": "analysis-042",
  "source_artifact": {
    "kind": "source-document",
    "path": "analysis.md",
    "file_sha256": "sha256:..."
  },
  "derivatives": [
    {
      "kind": "html",
      "path": "output/analysis.html",
      "file_sha256": "sha256:..."
    }
  ],
  "declared_sources": [],
  "process_disclosure": {},
  "validation": {},
  "lineage": {},
  "reproducibility": {"level": "R1"},
  "scientific_validity_claim": false
}
```

The record indexes identities and metadata. It does not embed document payload
text by default.

## 4. Identity semantics

The profile distinguishes two identities:

### Byte identity

`file_sha256` identifies the exact bytes of a recorded local file under SHA-256.

It does **not** prove:

- semantic equivalence;
- source credibility;
- authorship;
- correctness;
- novelty;
- scientific validity.

### Selected metadata identity

`metadata_canonical_sha256` identifies the canonical JSON serialization of the
selected bounded metadata mapping.

Changing the document while keeping the same selected metadata can therefore
change the file hash without changing the selected metadata hash. That is
intentional.

## 5. Process disclosure

The record carries the same bounded process-disclosure vocabulary as document
frontmatter:

```text
ai_assistance: none | used | not_declared
ai_tools[]
human_review: reviewed | partial | not_reviewed | not_declared
disclosure_ref
```

Interpretation boundary:

```text
AI disclosure != authorship adjudication
AI tool label != model provenance proof
human_review == reviewed != peer review
human review != scientific validation
```

The repository does not query a provider registry to verify model names.

## 6. Reference resolution

A source/provenance/configuration/disclosure reference is handled conservatively:

- an existing local file is hashed and marked `local-file`;
- a URI is retained as an opaque URI and is not dereferenced;
- another unresolved string is retained as an opaque unresolved reference.

The record therefore never turns network availability into a hidden dependency.

## 7. Frontmatter diagnostics

The embedded validation summary is derived from the bounded frontmatter
validator. It can report errors/warnings about field types, enums, unknown
fields and process-disclosure consistency.

A clean validation result means only that those implemented predicates passed.
It does not establish factual or scientific correctness.

## 8. Reproducibility levels

The shared local project vocabulary remains:

- **R0 Traceable** — source/artifact identity can be associated.
- **R1 Replay-addressable** — enough declared input/configuration/tool identity
  exists to address the intended replay.
- **R2 Environment-bounded** — important runtime/dependency assumptions are also
  bounded and recorded.
- **R3 Reproduced** — a separate rerun actually occurred and was compared under
  a declared criterion.

`artifact_record.py` accepts a caller-declared level but **does not perform a
rerun**. It therefore cannot self-award R3 from metadata generation alone.

## 9. Standalone use

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync@1 \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

## 10. SyncEngine use

Programmatically:

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

Or set:

```yaml
artifact_record:
  emit: true
  reproducibility_level: R1
```

in `sync/targets.yaml`.

The default remains opt-in to avoid silently adding new output files to existing
callers.

## 11. Relation to RO-Crate 1.3

RO-Crate 1.3 is the current external Research Object packaging target used by
this repository. The artifact record remains a project-owned JSON profile.

If both options are enabled, SyncEngine emits the artifact record first. The
later RO-Crate writer can include it in `hasPart` as an ordinary file payload.
This establishes packaging identity only; it does not assert that the custom
JSON object is defined by RO-Crate.

This separation follows an important research-engineering principle also visible
in Process/Workflow/Provenance Run RO-Crate work: the data products and the
execution/provenance records that describe their production are related but not
identical objects.

## 12. Cross-repository role

The intended three-repository handoff is now:

```text
auto-doc-engine/artifact-record@1
        |
        v
epistemic-pipeline
  upstream artifact reference
  claims / evidence / verification
        |
        v
sci-render-kit
  figure evidence / claim communication
```

No direct Python import between repositories is required.

## 13. Hard boundaries

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
