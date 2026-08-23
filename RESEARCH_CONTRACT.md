# Research Contract — 2026-08-23

Status: active architecture contract for repository claims and research-artifact boundaries.

This document defines how `auto-doc-engine` describes evidence, provenance, reproducibility, and interoperability. Documentation does not create an implementation by itself: every capability claim must still be backed by repository code, a declared optional dependency, or an explicit `proposed` / `experimental` status.

## 1. Role in the research toolchain

`auto-doc-engine` is the **document and evidence-packaging plane** of the three-repository research toolchain:

`source data -> document structure -> structural change records -> reference/health checks -> rendered artifact -> optional format conversion`

Its job is to make research documents inspectable and traceable. It does **not** determine scientific truth, merge arbitrary human edits safely, or prove that an output is reproducible in another environment.

## 2. Evidence contract

A claim about an artifact SHOULD identify, when available:

- source path or source identifier;
- content digest;
- transformation or renderer used;
- relevant configuration and dependency versions;
- output path and output digest;
- validation status and known untested boundaries.

A digest establishes identity for bytes under a declared canonicalization rule. It does not establish semantic equivalence, correctness, authorship, or scientific validity.

## 3. Current implementation boundary

### Implemented within tested interfaces

- Jinja2 rendering from the currently supported JSON/CSV bindings;
- Mistune-based Markdown AST parsing and rendering for supported node types;
- structural add/modify/delete/unchanged classification;
- Markdown cross-reference indexing and classified broken-link diagnostics;
- frontmatter validation, readability reporting, and document-set health checks;
- optional format synchronization through declared external tools.

### Explicitly not established

- automatic conflict-free preservation of arbitrary human edits;
- semantic diffing or semantic equivalence;
- immutable event sourcing or tamper-proof provenance history;
- SQLite/API source adapters;
- one validated end-to-end production pipeline for every declared output format;
- RO-Crate generation or validation.

## 4. Structural-diff semantics

The current incremental engine hashes rendered node text with SHA-256 and uses a shortened digest for matching. `difflib.SequenceMatcher` is then used to classify structural changes between sibling sequences.

This is a **change detector**, not a merge engine. A result that marks a subtree unchanged does not prove that every human edit is preserved under a later application workflow. Conflict resolution, patch application, ownership rules, and collaborative-edit semantics belong to an upper layer until executable contracts exist.

## 5. Provenance and reproducibility levels

The following levels are local project terminology, not an external standard:

- **R0 — Traceable**: artifact metadata and source references are recorded.
- **R1 — Replay-addressable**: input/configuration identifiers, digests, tool revision, and commands are sufficient to address the intended replay.
- **R2 — Environment-bounded**: runtime/dependency versions and external-tool assumptions are also recorded.
- **R3 — Reproduced**: an independent rerun has actually been performed and compared under a declared acceptance criterion.

The repository must not label an artifact `R3` merely because metadata or a manifest exists.

## 6. Cross-repository handoff contract

When an upper-layer workflow connects this repository with `epistemic-pipeline` or `sci-render-kit`, the preferred handoff record is a small structured object containing:

```text
artifact_id
content_sha256
source_refs[]
document_status
generated_with
provenance_ref
validation_status
```

This is an interoperability contract, not a claim that the repositories currently call each other directly.

## 7. RO-Crate interoperability target

RO-Crate 1.3 was published as a Recommendation on 2026-06-22. It is a useful current target for packaging research objects and machine-readable contextual metadata.

For this repository, **RO-Crate 1.3 is a proposed mapping target only**. No README, manifest, or provenance file may be described as an RO-Crate unless a conforming writer/validator and executable tests are added.

Candidate future mappings include:

- document or rendered output -> `File` / data entity;
- source/configuration relationships -> contextual entities and provenance links;
- repository/tool/version -> software/context entities;
- run or generation event -> action/provenance description.

## 8. Dependency evidence observed on 2026-08-23

External version observations are evidence about the ecosystem, not proof of compatibility with this repository:

- Mistune: repository security floor remains `>=3.2.1`; PyPI latest observed version is 3.3.4. The floor is retained because 3.2.1 contains the relevant security fixes; compatibility with every newer release is not implied without tests.
- Pandoc: latest observed release is 3.10.2 (2026-08-11). It remains optional and environment-dependent here; this repository does not claim validation against that release merely by recording it.

## 9. Shared scientific-integrity rules

1. Provenance is not truth.
2. A digest is not semantic equivalence.
3. A passing document-health check is not peer review.
4. Optional dependencies that are absent must produce an explicit unsupported/error state, never fabricated success.
5. Experimental modules do not become integrated capabilities through documentation wording.
6. External standards are cited with version/date and a local implementation status.

## 10. Primary references

Retrieved 2026-08-23:

- RO-Crate 1.3 Specification: https://www.researchobject.org/ro-crate/1.3/
- FAIR Principle R1.2: https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
- Mistune PyPI: https://pypi.org/project/mistune/
- Pandoc releases: https://github.com/jgm/pandoc/releases
