# Architecture — auto-doc-engine

> Calibrated 2026-08-23. This document describes implemented behavior and bounded experimental surfaces. It does not define GitHub merge policy.

[简体中文](ARCHITECTURE_zh.md) · [README](README.md) · [Research Contract](RESEARCH_CONTRACT.md)

## 1. Thesis

Research-document automation is treated as a **compiler + evidence-packaging problem**:

1. structured source data is bound into a document;
2. Markdown is parsed into a typed AST;
3. structural changes are reported with byte-identity evidence;
4. local references and metadata are inspected across the document set;
5. findings can be serialized as human text, JSON or SARIF;
6. artifacts can be converted when optional tools exist;
7. a successful artifact set can optionally receive RO-Crate 1.3 metadata.

The architecture optimizes for inspectability and honest failure, not for maximum automation or claims of scientific correctness.

## 2. Canonical flow

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
  structural changes   document/heading graph  research metadata
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
                                  ▼
                           core/ro_crate.py
                                  │
                                  ▼
                         RO-Crate 1.3 metadata
```

The modules remain independently callable. The diagram describes a composable architecture, not a mandatory all-or-nothing facade.

## 3. Data-binding boundary

`core/renderer.py` currently supports:

- JSON mapping/list data;
- CSV rows;
- YAML/YML mapping/list data;
- Jinja2 templates and the repository `table` / `bullet_list` filters.

`strict=False` preserves permissive historical loading. `strict=True` makes missing files, unsupported suffixes and invalid top-level structured data explicit failures.

Not integrated: SQLite, remote APIs, database credentials, network fetching, or schema inference.

## 4. AST boundary

`core/ast_engine.py` is the single Markdown-structure boundary for integrated modules.

### Implemented subset

- headings, paragraphs, text;
- fenced code / inline code;
- ordered and unordered lists;
- tables;
- blockquotes / thematic breaks;
- strong / emphasis / strikethrough;
- links / images;
- soft and hard line breaks.

Mistune plugins are not counted as capability unless their emitted nodes are mapped. This refresh closes the prior inconsistency where the strikethrough plugin was enabled but its node type was unsupported.

### Identity semantics

`ASTNode.signature` uses SHA-256 over shallow node fields. It is an identity/equality aid, not a semantic content hash. Rendering is normalized Markdown and does not promise byte-for-byte preservation of source formatting.

## 5. Structural-change boundary

`core/incremental.py` computes SHA-256 identities over normalized rendered subtrees and aligns sibling sequences with `difflib.SequenceMatcher`.

The output vocabulary is:

```text
add | modify | delete | unchanged
```

The refresh consolidates subtree add/delete handling and atomically replaces the bounded YAML generation history.

What this establishes: **a structural change report**.

What it does not establish:

- safe application of a patch;
- conflict ownership;
- CRDT/OT merge semantics;
- semantic equivalence;
- preservation of every arbitrary manual edit.

## 6. Document graph and diagnostics

`core/cross_ref.py` indexes document files and headings, resolves local `.md` links, and creates explicit bidirectional graph edges for resolved references. It also maintains a directed document-level link view for diagnostics.

The refresh normalizes URL parsing, percent-decoding and docs-root-relative Markdown paths. Heading text extraction is recursive, so formatting nodes no longer erase heading text from the index.

`near_miss` is a lexical repair hint based on `difflib`; `dangling` means no close indexed target was found. Neither label is a semantic conclusion about author intent.

## 7. Research metadata

`core/frontmatter.py` provides a bounded YAML metadata contract:

```text
title, description, aliases, status, updated, tags,
authors, sources, license, doi, language, artifact_id
```

Unknown fields are warnings to retain forward compatibility. This is deliberately smaller than a publication ontology. It is designed to carry enough stable metadata for documents, evidence handoffs and research-object packaging.

## 8. Doctor profile

`core/doctor.py` composes the graph, frontmatter and readability layers into `auto-doc-engine/doctor@1`.

The report contains:

- unresolved local links;
- orphan documents;
- selected directed cycles;
- frontmatter issues;
- descriptive readability signals;
- graph statistics;
- explicit error/warning arrays.

Its exit code is a **runtime caller signal**. It is not a GitHub policy and does not determine scientific validity.

## 9. SARIF profile

`core/sarif.py` emits `auto-doc-engine/sarif@1` targeting OASIS SARIF 2.1.0 incorporating Approved Errata 01.

Stable identity surfaces:

- namespaced `ruleId` values;
- `autoDocFinding/v1` partial fingerprints based on logical finding identity;
- source profile metadata linking the result back to `doctor@1`.

SARIF is an interchange format for findings; downstream ingestion is not evidence that the downstream consumer certifies this repository.

## 10. Synchronization boundary

`core/sync.py` separates built-in behavior from external tools:

- Markdown: Python `shutil.copy2`, cross-platform;
- HTML: Pandoc when available, Mistune fallback otherwise;
- DOCX / EPUB: Pandoc;
- PDF: Pandoc + declared PDF engine (`xelatex` in the current target command).

`sync/targets.yaml.custom.pandoc_path` is now an actual runtime setting rather than documentation-only configuration.

Every subprocess invocation uses argument lists, never `shell=True`.

## 11. RO-Crate 1.3 profile

`core/ro_crate.py` implements the repository's first concrete research-object metadata writer.

Its standards-facing JSON-LD surface contains only RO-Crate/Schema.org terms from the selected 1.3 context. Repository profile names stay in project documentation/manifest instead of being injected as undefined JSON-LD properties.

Generated graph:

```text
ro-crate-metadata.json : CreativeWork
        │ about
        ▼
./ : Dataset
        │ hasPart
        ├── artifact A : File ── identifier ──> SHA-256 PropertyValue
        └── artifact B : File ── identifier ──> SHA-256 PropertyValue

Dataset ── author ──> Person contextual entities
```

The writer can be called directly or by `SyncEngine` after successful output generation.

External RO-Crate validator execution is not built into the repository and must not be inferred from file generation.

## 12. Experimental surfaces

Experimental files are intentionally **not** part of the canonical composition:

| Module | Actual bounded semantics |
|---|---|
| `template_prewarm.py` | in-memory LRU cache for caller-produced values keyed by template-text hash |
| `async_conduit.py` | bounded priority scheduling for caller-provided handlers |
| `memory_lattice.py` | local node/link JSON store plus rounded numeric indexes |
| `restart_protocol.py` | event replay with result-hash checks; deterministic only under deterministic handlers |
| `self_observe.py` | explicit instrumentation events and descriptive timing summaries |

Historical names are preserved for compatibility; documentation no longer promotes metaphorical names into capability claims.

## 13. Cross-repository handoff

The repository remains loosely coupled to `epistemic-pipeline` and `sci-render-kit`. A preferred handoff object is data, not an import dependency:

```text
artifact_id
content_sha256
source_refs[]
document_status
generated_with
provenance_ref
validation_status
```

The consuming repository owns the interpretation of its own fields. For example, a confidence value imported from an epistemic process must carry its semantics rather than being silently re-labelled as probability.

## 14. Reproducibility semantics

R0–R3 are local project levels:

- R0 Traceable
- R1 Replay-addressable
- R2 Environment-bounded
- R3 Reproduced

Only an actual separate rerun plus a declared comparison criterion establishes R3. Research-object metadata, checksums and diagnostic files improve evidence quality but do not collapse those levels.

## 15. Dependency / standards observations

Observed on 2026-08-23:

- RO-Crate 1.3 — current long-term release, published 2026-06-22;
- SARIF 2.1.0 + Approved Errata 01 — current target;
- Mistune 3.3.4 — observed current, repository floor remains `>=3.2.1`;
- Pandoc 3.10.2 — observed current, optional environment dependency;
- Citation File Format 1.2.0 — repository citation format.

Observation is not compatibility evidence. Compatibility claims remain bounded by actual repository behavior.

## 16. Non-goals

- GitHub Actions / merge gating as repository architecture;
- automatic peer review;
- semantic truth inference;
- network-backed data acquisition;
- universal Markdown round-trip fidelity;
- universal converter availability;
- external RO-Crate certification;
- automatic promotion of Experimental modules.
