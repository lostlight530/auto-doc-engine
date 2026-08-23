# auto-doc-engine

> AST-driven research-document compilation, structural change evidence, document-graph diagnostics, SARIF interchange, and optional RO-Crate 1.3 packaging.

[简体中文](README_zh.md) · [Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Examples](examples/README.md)

## Positioning

`auto-doc-engine` treats Markdown as a typed research artifact rather than an opaque string. Its canonical path is deliberately inspectable:

```text
JSON / CSV / YAML
        ↓
Jinja2 document binding
        ↓
Typed Markdown AST
        ↓
Structural change report
        ↓
Cross-document graph + metadata diagnostics
        ↓
Text / JSON / SARIF evidence
        ↓
Markdown / optional Pandoc formats
        ↓
optional RO-Crate 1.3 metadata package
```

The repository does **not** claim semantic truth, automatic conflict-free merging, universal format conversion, external-validator certification, or independent reproducibility from metadata alone.

## Capability map

| Capability | Status | Current boundary |
|---|---|---|
| `core/renderer.py` | **Implemented** | Jinja2 rendering from JSON, CSV, YAML/YML. SQLite/network adapters are not integrated. |
| `core/ast_engine.py` | **Implemented** | Mistune 3.x AST mapping for the declared Markdown subset, including tables, strikethrough, images, ordered lists and explicit unsupported-node failure. |
| `core/incremental.py` | **Implemented** | SHA-256-backed structural add/modify/delete/unchanged reporting with atomic bounded history persistence. Not a merge engine. |
| `core/cross_ref.py` | **Implemented** | Local Markdown reference graph, heading indexing, aliases, near-miss/dangling diagnostics and recurring-target backlog. |
| `core/frontmatter.py` | **Implemented** | Bounded YAML research metadata for title/description/authors/sources/license/DOI/language/artifact identity plus document fields. |
| `core/readability.py` | **Implemented** | Descriptive Latin/CJK heuristics with fenced-code exclusion. Not a writing-quality score. |
| `core/doctor.py` | **Implemented** | Aggregated runtime diagnostics with Text/JSON output and explicit local exit status. Not a GitHub merge policy. |
| `core/sarif.py` | **Implemented** | Conservative OASIS SARIF 2.1.0 + Approved Errata 01 result profile. |
| `core/sync.py` | **Implemented / Optional converters** | Cross-platform Markdown copy; Pandoc-backed HTML/DOCX/PDF/EPUB when the declared tools exist; Mistune HTML fallback. |
| `core/ro_crate.py` | **Implemented profile** | Writes the core RO-Crate 1.3 JSON-LD structure for local artifact sets. No external-validator certification claim. |
| `template_prewarm`, `async_conduit`, `memory_lattice`, `restart_protocol`, `self_observe` | **Experimental** | Standalone reference modules with corrected bounded semantics; not wired into the canonical path. |

## Data binding

The renderer accepts small structured sources:

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
assert markdown
```

Supported source suffixes are `.json`, `.csv`, `.yaml`, and `.yml`. `strict=False` preserves the historical permissive behavior; `strict=True` turns missing/unsupported sources into explicit exceptions for callers that need fail-fast execution.

## Research metadata

Optional YAML frontmatter can carry a compact, portable research-document contract:

```yaml
---
title: Evidence synthesis
description: Structured summary of declared sources
status: draft
updated: 2026-08-23
authors: [lostlight530]
sources:
  - https://www.researchobject.org/ro-crate/specification/1.3/
license: MIT
language: en
artifact_id: summary-2026-08-23
---
```

Unknown fields remain warnings for forward compatibility. This schema is intentionally small; it is not a complete bibliographic ontology.

## Diagnostics and SARIF

Human or JSON inspection:

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/doctor.py path/to/docs --strict
```

SARIF interchange:

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
```

`doctor` reports unresolved links, orphans, selected directed cycles, frontmatter issues, readability signals and graph statistics. `--strict` only changes the command's local exit-status policy; it does not create a repository or GitHub merge gate.

SARIF uses stable namespaced rule IDs and `autoDocFinding/v1` partial fingerprints. The project uses SARIF as a standards-based findings container, not as a claim that document diagnostics are source-code static analysis.

## Format synchronization

`core/sync.py` keeps environment-dependent conversion explicit:

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
```

Markdown copying uses Python's standard library and is cross-platform. Pandoc is optional. `sync/targets.yaml` can point to a specific Pandoc executable and reference document; missing converters are reported rather than represented as success.

## RO-Crate 1.3 packaging

RO-Crate 1.3 was released on 2026-06-22 and is the current long-term release observed for this refresh. The repository now has a concrete writer instead of a documentation-only proposal.

Standalone CLI:

```bash
python core/ro_crate.py output report.md report.html \
  --name "Research artifact set" \
  --description "Rendered report and interoperable metadata" \
  --author lostlight530 \
  --license MIT
```

Or opt in through `SyncEngine(..., emit_ro_crate=True)` / `sync/targets.yaml`.

The writer emits:

- `ro-crate-metadata.json` as a `CreativeWork` metadata descriptor;
- `./` as the root `Dataset`;
- payload `File` entities with `contentSize` and `encodingFormat`;
- contextual `Person` entities for declared authors;
- SHA-256 byte-identity evidence as Schema.org `PropertyValue` entities.

**Boundary:** `auto-doc-engine/ro-crate@1` describes the repository's implementation profile in documentation/manifest. Generated JSON-LD is not labelled externally validator-certified unless an external validator is actually run and recorded.

## Reproducibility semantics

The shared research contract uses local project terminology:

- **R0 Traceable** — source and artifact identity metadata exist.
- **R1 Replay-addressable** — inputs/configuration/tool revision identify the intended replay.
- **R2 Environment-bounded** — relevant runtime/dependency assumptions are also recorded.
- **R3 Reproduced** — a separate rerun was actually performed and compared under a declared criterion.

A checksum, SARIF file, manifest, or RO-Crate metadata file alone does not establish R3.

## Experimental modules

The experimental files remain intentionally separate from the canonical pipeline:

- `template_prewarm.py` — bounded in-memory LRU cache for caller-produced render results;
- `async_conduit.py` — priority scheduling with bounded queue/concurrency for caller handlers;
- `memory_lattice.py` — local JSON node/link store with rounded numeric indexes;
- `restart_protocol.py` — event replay whose determinism depends on deterministic caller handlers;
- `self_observe.py` — descriptive event instrumentation and timing summaries.

The historical names are retained for API continuity. They are not evidence of autonomous optimization, semantic memory, mathematical lattices, or universal deterministic recovery.

## Current external observations — 2026-08-23

These are ecosystem observations, **not automatic compatibility claims**:

- RO-Crate: 1.3 current long-term release, published 2026-06-22;
- SARIF: 2.1.0 with Approved Errata 01 remains the target interchange standard;
- Mistune: 3.3.4 observed current; repository floor remains `>=3.2.1`;
- Pandoc: 3.10.2 observed current and remains optional/environment-dependent;
- Citation File Format: 1.2.0 remains the repository citation metadata format.

## Local maintenance tools

When useful, contributors can run the existing local checks:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

They are manual maintenance aids, **not GitHub Actions, branch protection, or merge gates**. Optional converter availability and external standards validation remain separate evidence.

## Repository map

```text
auto-doc-engine/
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── cross_ref.py
│   ├── frontmatter.py
│   ├── readability.py
│   ├── doctor.py
│   ├── sarif.py
│   ├── sync.py
│   ├── ro_crate.py
│   └── experimental modules
├── templates/jinja2/
├── sync/targets.yaml
├── examples/
├── tests/                  # optional local maintenance checks
├── RESEARCH_CONTRACT.md
├── MANIFEST.yaml
└── CITATION.cff
```

## Scientific-integrity boundaries

- Provenance is not truth.
- A digest is byte identity under a declared algorithm, not semantic equivalence.
- Structural diff is not conflict resolution.
- Readability heuristics are not peer review or accessibility conformance.
- RO-Crate metadata improves research-object interoperability but does not prove reproducibility.
- Optional tools that are absent produce explicit unsupported/error states.
- Experimental modules remain experimental until they are deliberately integrated into the canonical architecture.

## Citation and license

Citation metadata is provided in `CITATION.cff` using CFF 1.2.0. License: MIT.
