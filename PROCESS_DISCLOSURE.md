# Research Process Disclosure — auto-doc-engine

**Calibration:** 2026-08-26  
**Status:** implemented frontmatter sub-contract; project-owned vocabulary, not an external publishing standard

## 1. Purpose

Research artifacts increasingly pass through AI-assisted analysis, drafting, coding, retrieval, and communication workflows. A document should be able to preserve a small amount of process context without pretending that metadata can decide authorship, truth, originality, or policy compliance.

`auto-doc-engine` therefore supports four optional frontmatter fields:

```yaml
ai_assistance: used
ai_tools:
  - provider/model or tool identifier declared by the author
human_review: reviewed
disclosure_ref: path-or-URI-to-a-fuller-disclosure
```

These fields are deliberately bounded. They record what the document declares about its production process and allow that context to travel with downstream evidence packaging.

## 2. Field semantics

### `ai_assistance`

Allowed values:

```text
none
used
not_declared
```

- `none` means the artifact explicitly declares no AI assistance for the process being described.
- `used` means AI assistance was used and should normally be accompanied by at least one `ai_tools` entry.
- `not_declared` means the record intentionally makes no claim either way.

Absence of the field is different from an explicit `none` declaration.

### `ai_tools`

A list of human-readable identifiers supplied by the artifact author or producing system.

Examples may include a product, provider/model pair, local model identifier, or other tool name. The repository does not resolve or validate the identity against a vendor registry.

A tool identifier is process metadata, not evidence that the named system actually produced a specific statement.

### `human_review`

Allowed values:

```text
reviewed
partial
not_reviewed
not_declared
```

This field describes the declared review state of the artifact, not peer-review status.

`reviewed` must not be interpreted as journal peer review, expert validation, factual correctness, or scientific approval.

### `disclosure_ref`

Optional local path or URI pointing to a fuller process disclosure, methods note, run record, or institutional statement.

`auto-doc-engine` stores the reference as metadata. It does not dereference the target or certify its contents.

## 3. Validation behavior

The frontmatter validator treats invalid field types and invalid enum values as errors.

Cross-field incompleteness is a warning rather than an error:

- `ai_assistance: used` with no usable `ai_tools` entry -> warning;
- declared `ai_tools` while `ai_assistance` is absent, `none`, or `not_declared` -> warning.

This preserves historical-document compatibility while making incomplete disclosure visible to local diagnostics.

## 4. Scientific and authorship boundaries

```text
AI disclosure != authorship adjudication
AI tool identity != provenance proof
human review != peer review
human review != truth
process metadata != scientific validity
process metadata != publisher compliance
```

The repository intentionally does not infer whether an AI system qualifies for authorship, whether a disclosure is sufficient for a particular journal, or whether an artifact is scientifically correct.

## 5. Cross-repository handoff

When available, downstream systems may preserve:

```text
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

The intended chain is:

```text
auto-doc-engine
artifact-level declared process context
        ->
epistemic-pipeline
run/provider + claim/evidence audit context
        ->
sci-render-kit
figure/visual claim bindings + communication disclosure
```

The three repositories remain independently runnable; this vocabulary is an interoperability convention, not runtime coupling.

## 6. Why this exists now

Two 2026 research signals sharpen the requirement:

1. Nature Computational Science, **Responsible and transparent use of AI in scientific publishing** (20 Aug 2026), emphasizes transparency, accountability, and human oversight as AI becomes embedded across research and scientific communication.
2. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents** (arXiv:2608.18312, 18 Aug 2026) argues that model-call logs alone are insufficient and that scientific systems need portable artifact- and claim-aware audit relations.

These sources motivate inspectable process records. They do not define this repository's fields and do not certify this implementation.

## 7. References

- https://www.nature.com/articles/s43588-026-01043-4
- https://arxiv.org/abs/2608.18312
- https://www.nature.com/articles/s43588-026-01035-4
