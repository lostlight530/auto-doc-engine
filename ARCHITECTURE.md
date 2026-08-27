# Architecture — auto-doc-engine

> Calibrated 2026-08-27. This document describes implemented behavior and bounded experimental surfaces. It does not define GitHub merge policy.

[简体中文](ARCHITECTURE_zh.md) · [README](README.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [Process Disclosure](PROCESS_DISCLOSURE.md) · [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md)

## 1. Thesis

Research-document automation is treated as a **compiler + artifact-evidence + research-object packaging problem**.

The repository separates concerns that are often collapsed into “generate a report”:

1. structured source binding;
2. typed document structure;
3. structural-change evidence;
4. document/reference diagnostics;
5. bounded research metadata and process disclosure;
6. findings interchange;
7. format conversion with explicit external dependencies;
8. a lightweight artifact handoff record;
9. optional external Research Object packaging.

The architecture optimizes for inspectability and honest failure, not for maximum automation, source-truth inference, authorship adjudication, peer review or scientific correctness.

## 2. Canonical architecture

```text
                 ┌──────────────────────────────┐
                 │ JSON / CSV / YAML data      │
                 └──────────────┬───────────────┘
                                │
                                ▼
                   core/renderer.py + Jinja2
                                │
                                ▼
                    normalized Markdown text
                                │
                                ▼
                      core/ast_engine.py
                                │
          ┌─────────────────────┼──────────────────────┐
          │                     │                      │
          ▼                     ▼                      ▼
  core/incremental.py   core/cross_ref.py      core/frontmatter.py
  structural changes   document/heading graph  metadata + disclosure
          │                     │                      │
          └──────────────┬──────┴──────────────┬───────┘
                         ▼                     ▼
                  core/doctor.py       core/readability.py
                         │
                 ┌───────┴─────────┐
                 ▼                 ▼
               JSON             core/sarif.py
                                   │
                                   ▼
                         SARIF 2.1.0 + Errata 01

Markdown ──> core/sync.py ──> Markdown / optional HTML/DOCX/PDF/EPUB
                                  │
                                  ├──> core/artifact_record.py
                                  │      artifact-record@1
                                  │
                                  └──> core/ro_crate.py
                                         RO-Crate 1.3
```

The modules remain independently callable. The diagram describes a composable architecture, not a mandatory facade.

## 3. Data-binding boundary

`core/renderer.py` supports:

- JSON mapping/list data;
- CSV rows;
- YAML/YML mapping/list data;
- Jinja2 templates;
- repository Markdown helper filters.

`strict=False` preserves permissive historical loading. `strict=True` makes missing files, unsupported suffixes and invalid top-level data explicit failures.

Not integrated:

- SQLite/database connections;
- network-backed data fetching;
- credential handling;
- automatic schema inference.

## 4. Typed Markdown boundary

`core/ast_engine.py` is the integrated structural Markdown boundary.

Supported structure includes:

- heading / paragraph / text;
- fenced and inline code;
- ordered/unordered lists;
- tables;
- blockquotes / thematic breaks;
- strong / emphasis / strikethrough;
- links / images;
- soft/hard line breaks.

### Identity semantics

`ASTNode.signature` uses SHA-256 over selected local fields. Incremental subtree identities use SHA-256 over normalized rendered structure.

These are representation identities, not universal semantic hashes.

Parse → render produces normalized Markdown. It does not promise byte-for-byte round-trip fidelity.

## 5. Structural-change plane

`core/incremental.py` computes:

```text
normalized subtree
      ↓
SHA-256 identity
      ↓
sibling SequenceMatcher
      ↓
add / modify / delete / unchanged
```

Generation history is bounded and atomically replaced.

What this establishes:

> an inspectable structural-change report

What it does not establish:

- automatic patch application;
- conflict ownership;
- CRDT/OT merge semantics;
- semantic equivalence;
- preservation of arbitrary concurrent human edits.

## 6. Document graph and diagnostics

`core/cross_ref.py` indexes document/heading nodes and local Markdown links.

Integrated behavior includes:

- percent-decoding;
- URL parsing before local-path interpretation;
- docs-root-relative Markdown paths;
- recursive heading text extraction;
- aliases;
- lexical near-miss hints;
- dangling/recurring-target diagnostics;
- directed document-level graph views.

`near_miss` is a lexical repair hint, not inferred author intent.

## 7. Metadata and process-disclosure plane

`core/frontmatter.py` provides a bounded metadata contract including:

```text
title
description
aliases
status
updated
tags
authors
sources
license
doi
language
artifact_id
ai_assistance
ai_tools
human_review
disclosure_ref
```

Process-disclosure fields answer only what the artifact declares about its own production/review process.

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Unknown fields remain warnings for forward compatibility. Invalid field types/enums are errors. Cross-field disclosure inconsistencies are warnings.

This layer is not:

- a bibliographic ontology;
- an authorship decision system;
- a provider/model identity registry;
- peer review;
- publisher-policy certification.

## 8. Doctor and SARIF planes

`core/doctor.py` exposes `auto-doc-engine/doctor@1`.

It composes:

- local-link diagnostics;
- orphan documents;
- selected directed cycles;
- frontmatter/process-disclosure issues;
- descriptive readability signals;
- graph statistics.

The command's exit code is a caller-facing local runtime signal only.

`core/sarif.py` exposes `auto-doc-engine/sarif@1` targeting OASIS SARIF 2.1.0 incorporating Approved Errata 01.

SARIF is an interchange container for findings. Downstream ingestion is not external certification.

## 9. Synchronization plane

`core/sync.py` distinguishes built-in behavior from optional external tools:

- Markdown: Python `shutil.copy2`;
- HTML: Pandoc if available, Mistune fallback otherwise;
- DOCX / EPUB: Pandoc;
- PDF: Pandoc + declared PDF engine.

External subprocesses use argument arrays rather than `shell=True`.

Two optional evidence/package outputs now exist:

```text
artifact_record.emit
research_object.emit_ro_crate
```

Both default to false.

## 10. Artifact-record plane

`core/artifact_record.py` implements:

```text
auto-doc-engine/artifact-record@1
```

The profile exists between document metadata and full Research Object packaging.

It can record:

- exact source-document SHA-256;
- successful derivative SHA-256 values;
- bounded selected metadata identity;
- declared authors/source refs;
- process disclosure;
- frontmatter validation summary;
- configuration/provenance/validation references;
- execution context;
- caller-declared R0–R3 level with explicit R3 limitation;
- hard scientific/authorship/peer-review boundary flags.

Payload text is not duplicated into the record.

### Reference resolution

A reference is handled conservatively:

```text
existing local file
  -> file identity recorded

URI
  -> retained as opaque URI, not dereferenced

other unresolved string
  -> retained as unresolved/opaque reference
```

The artifact record therefore does not introduce hidden network requirements.

### Validation semantics

The embedded validation section reflects the bounded frontmatter validator only.

```text
frontmatter clean != factual correctness
frontmatter clean != scientific validity
frontmatter clean != peer review
```

## 11. RO-Crate 1.3 plane

`core/ro_crate.py` implements the project's concrete RO-Crate 1.3 writer.

Standards-facing JSON-LD uses the selected RO-Crate/Schema.org context. Project profile names stay in project documentation rather than being injected as undefined standard properties.

Current graph shape:

```text
ro-crate-metadata.json : CreativeWork
        │ about
        ▼
./ : Dataset
        │ hasPart
        ├── artifact A : File ── identifier ──> SHA-256 PropertyValue
        └── artifact B : File ── identifier ──> SHA-256 PropertyValue

Dataset ── author ──> Person
```

If `artifact-record@1` is generated before crate emission, it may be included as an ordinary File payload.

That does **not** mean the project-owned JSON object becomes an RO-Crate standard profile.

No external RO-Crate validator is run by the canonical repository path.

## 12. Why artifact record and RO-Crate are distinct

The architecture deliberately uses two levels:

```text
artifact-record@1
  local/project interoperability object

RO-Crate 1.3
  external Research Object packaging
```

This is compatible with a broader Research Object separation-of-concerns pattern: resources, annotations and provenance/execution records can be linked while retaining their own scope, vocabulary and provenance.

The repository does not currently claim:

- Process Run Crate conformance;
- Workflow Run Crate conformance;
- Provenance Run Crate conformance.

## 13. Reproducibility semantics

Local R0–R3 terminology:

- **R0 Traceable** — source/artifact association exists.
- **R1 Replay-addressable** — declared inputs/config/tool identity address the intended replay.
- **R2 Environment-bounded** — important runtime/dependency boundaries are also recorded.
- **R3 Reproduced** — a separate rerun actually happened and was compared under a declared criterion.

A checksum, artifact record, SARIF report or RO-Crate file cannot self-award R3.

## 14. Cross-repository handoff

Day-4 conceptual chain:

```text
auto-doc-engine
  artifact-record@1
        ↓
epistemic-pipeline
  upstream artifact refs
  claim-verification@1
  evidence-envelope@2
        ↓
sci-render-kit
  claim_audit_ref
  figure-claim-audit@1
  figure-evidence@2
```

Interoperability is expressed through files/references, not hidden imports.

## 15. Experimental surfaces

Experimental modules remain outside the canonical composition:

| Module | Actual bounded semantics |
|---|---|
| `template_prewarm.py` | in-memory LRU cache for caller-produced results |
| `async_conduit.py` | bounded priority scheduling for caller handlers |
| `memory_lattice.py` | local node/link JSON store plus numeric bucket indexes |
| `restart_protocol.py` | event replay with result-hash checks; deterministic only under deterministic handlers |
| `self_observe.py` | explicit instrumentation events and descriptive timing summaries |

Historical names are compatibility surfaces, not capability proofs.

## 16. Global frontier calibration

The 2026-08-27 design is informed by several external directions:

- autonomous-science provenance as a re-openable corrective record;
- AI scientific-publishing transparency and human oversight;
- artifact-centered claim-aware observability;
- EarthVerse-style evidence-chain consistency failures;
- RO-Crate and Workflow Run Crate separation between research products and execution/provenance descriptions.

These are design signals, not endorsement or conformance evidence. See `FOUR_DAY_CONSOLIDATION.md` and `FRONTIER_ALIGNMENT.md`.

## 17. Non-goals

- GitHub Actions / CI / CodeQL / merge-gate architecture;
- automatic peer review;
- scientific truth inference;
- source-credibility adjudication;
- network data acquisition as a canonical dependency;
- universal Markdown byte fidelity;
- universal converter availability;
- external RO-Crate certification;
- fake Workflow Run Crate conformance;
- automatic promotion of Experimental modules.

## 18. Hard invariants

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
