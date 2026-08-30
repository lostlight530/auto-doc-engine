# Research Process Disclosure — auto-doc-engine

**Calibration:** 2026-08-31  
**Status:** implemented frontmatter sub-contract; project-owned vocabulary, not an external publishing standard

## Purpose

A research artifact should be able to preserve explicit process context without pretending that metadata can decide authorship, truth, originality, peer review, or publisher compliance

Supported optional frontmatter

```yaml
ai_assistance: used
ai_tools:
  - provider/model or tool identifier declared by the author
human_review: reviewed
disclosure_ref: path-or-URI-to-a-fuller-disclosure
```

These fields are declarations. They are not inferred from document prose

## Assertion basis

When these fields enter an artifact record, their basis is

```text
document-frontmatter
```

The record also states

```json
{"automatic_ai_detection_used": false}
```

```text
explicit disclosure != AI-content detection
AI-content detection != authorship adjudication
assertion basis != truth
```

The repository does not run an AI-text detector, guess a provider/model from writing style, or infer that missing disclosure means no AI was used

## Field semantics

### `ai_assistance`

```text
none
used
not_declared
```

- `none`: the artifact explicitly declares no AI assistance for the described process
- `used`: AI assistance was declared
- `not_declared`: no claim is made either way

Absence is not converted to `none`

### `ai_tools`

Human-readable tool/model/provider identifiers supplied by the artifact author or producing system. The repository does not verify them against a vendor registry

### `human_review`

```text
reviewed
partial
not_reviewed
not_declared
```

This is declared artifact review state only

```text
reviewed != peer reviewed
reviewed != expert validation
reviewed != scientific approval
```

### `disclosure_ref`

Optional local path or URI to a fuller disclosure/methods/run record. The artifact-record layer may hash a local file; remote/opaque references are not automatically dereferenced or certified

## Validation behavior

Invalid field types/enums are errors. Cross-field incompleteness is warning-level for compatibility

- `ai_assistance: used` without usable `ai_tools` -> warning
- declared `ai_tools` while `ai_assistance` is absent/`none`/`not_declared` -> warning

A warning or clean frontmatter result is not a scientific judgment

## Cross-repository process handoff

```text
auto-doc-engine
  document-frontmatter process disclosure
        ↓
epistemic-pipeline
  provider-adapter + caller-declared process context
        ↓
sci-render-kit
  recipe-declared communication/process context
```

Each repository preserves how process metadata entered its own evidence object

None inherits authorship, peer-review, or scientific-validity claims from another

## Maintenance and document authority

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`

Daily/weekly/monthly maintenance may reconcile vocabulary and cross-repository names, but it must not infer missing disclosure or rewrite historical process declarations merely because later policy wording changes

The August stage closed on 2026-08-31. Calendar/stage closure does not convert process disclosure into authorship, peer review, or publisher compliance

## Scientific and authorship boundaries

```text
AI disclosure != authorship adjudication
AI tool identity != model provenance proof
AI disclosure != AI-text detection
human review != peer review
human review != truth
process metadata != scientific validity
process metadata != publisher compliance
maintenance clean != publisher compliance
```

## External calibration

Current scientific-publishing discussions increasingly ask for transparent disclosure and accountability. Separately, AI-content detection remains an inference/classification problem with its own uncertainty and failure modes

This repository chooses the narrower mechanism it can represent honestly: explicit declarations plus their assertion basis

Calibration signals include work on responsible/transparent AI use in scientific publishing, provenance-grounded autonomous science, artifact-centered claim-aware observability, and reporting on AI-detection limitations

These sources motivate transparency and auditability. They do not define or certify this project-owned vocabulary
