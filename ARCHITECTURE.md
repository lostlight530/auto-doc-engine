# Architecture — auto-doc-engine

> Calibrated 2026-08-27. This document describes implemented behavior and bounded experimental surfaces. It is not GitHub merge policy.

## Thesis

Research-document automation is treated as a compiler + artifact-evidence + Research Object packaging problem.

```text
structured data
  -> renderer / Jinja2
  -> normalized Markdown
  -> typed Markdown AST
  -> structural-change evidence
  -> document graph + frontmatter + readability
  -> Doctor / JSON / SARIF
  -> sync / rendered derivatives
  -> optional artifact-record
  -> optional RO-Crate 1.3
```

## Stable project identifiers

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
autoDocFinding
```

Project-owned identifiers do not carry decorative `@1/@2` or `/v1` suffixes. Real external/runtime versions remain provenance when known.

## Data-binding boundary

`core/renderer.py` supports JSON, CSV and YAML/YML through Jinja2. `strict=False` preserves permissive historical loading; `strict=True` makes missing/unsupported input and invalid top-level structures explicit failures.

Not integrated: SQLite/database connections, network-backed fetching, credentials or automatic schema inference.

## Typed Markdown boundary

`core/ast_engine.py` provides the integrated normalized Markdown structure. Supported nodes include headings, paragraphs/text, code, lists, tables, blockquotes, emphasis variants, links/images and line breaks.

AST/subtree SHA-256 values are representation identities, not universal semantic hashes. Parse/render normalizes supported Markdown and does not promise byte-for-byte round-trip fidelity.

## Structural-change plane

`core/incremental.py` computes `add / modify / delete / unchanged` with local structural identities and sibling alignment.

It is a change detector, not automatic patching, conflict resolution, ownership negotiation, CRDT/OT merge or semantic-equivalence proof.

## Document graph and metadata

`core/cross_ref.py` indexes local document/heading references and exposes dangling/near-miss/recurring diagnostics. Near-miss suggestions are lexical hints only.

`core/frontmatter.py` provides bounded research metadata and process disclosure. Missing provider/model/version/review information stays unknown/not-declared.

```text
process disclosure != authorship proof
human review != peer review
source ref != source credibility
```

## Doctor and SARIF

`core/doctor.py` emits `auto-doc-engine/doctor` diagnostics. Exit status is a local caller signal only.

`core/sarif.py` emits `auto-doc-engine/sarif` using SARIF 2.1.0 + Approved Errata 01. `autoDocFinding` is the stable project fingerprint namespace.

SARIF ingestion is interoperability, not scientific certification.

## Synchronization

`core/sync.py` keeps built-in behavior separate from optional tools:

- Markdown: Python `shutil.copy2`;
- HTML: Pandoc when available, Mistune fallback otherwise;
- DOCX/EPUB: Pandoc;
- PDF: Pandoc + declared PDF engine.

External processes use argument arrays rather than `shell=True`. Optional artifact-record and RO-Crate output remain opt-in.

## Artifact-record plane

`core/artifact_record.py` emits `auto-doc-engine/artifact-record`.

It can record source/derivative SHA-256 identities, selected metadata identity, declared source/author refs, process disclosure, bounded validation, lineage/config references, execution context and a local R0–R3 state.

Payload prose is not duplicated by default; local files may be hashed while URI/opaque references remain unresolved unless separately handled.

## RO-Crate plane

`core/ro_crate.py` targets the external RO-Crate 1.3 standard and uses standards-facing JSON-LD for the metadata descriptor, root Dataset, File/Person entities and SHA-256 PropertyValue records.

`auto-doc-engine/ro-crate` is only the stable project exporter identity. It is not an external RO-Crate profile version.

No external validator, Workflow/Process/Provenance Run Crate conformance or scientific reproducibility is claimed.

## Why artifact record and RO-Crate are distinct

```text
auto-doc-engine/artifact-record
  lightweight project handoff

RO-Crate 1.3
  external Research Object packaging
```

They can be linked without being collapsed into the same vocabulary or claim.

## Reproducibility semantics

- R0 Traceable
- R1 Replay-addressable
- R2 Environment-bounded
- R3 Reproduced only after an actual separate rerun plus declared comparison

A checksum, SARIF report, artifact record or crate cannot self-award R3.

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

References do not create hidden imports or inherited scientific validity.

## Experimental surfaces

- `template_prewarm.py`: bounded in-memory LRU cache
- `async_conduit.py`: bounded priority scheduler
- `memory_lattice.py`: local node/link store + numeric bucket index
- `restart_protocol.py`: event replay with result-hash verification
- `self_observe.py`: explicit instrumentation and descriptive timing

Historical metaphorical names are not capability claims.

## Hard invariants

```text
Provenance != Truth
Hash identity != semantic equivalence
Structure != meaning
Structural change != conflict resolution
Declared source != source credibility
Process disclosure != authorship proof
Human review != peer review
Artifact record != external standard
RO-Crate packaging != reproduction
Local diagnostics != scientific validation
```

GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions and merge-gate architecture remain outside the repository design.
