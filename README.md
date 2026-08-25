# auto-doc-engine

> AST-driven research-document compilation, structural change evidence, process-aware metadata, document-graph diagnostics, SARIF interchange, and optional RO-Crate 1.3 packaging.

[简体中文](README_zh.md) · [Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Process Disclosure](PROCESS_DISCLOSURE.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Examples](examples/README.md)

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
Artifact process disclosure metadata
        ↓
Text / JSON / SARIF evidence
        ↓
Markdown / optional Pandoc formats
        ↓
optional RO-Crate 1.3 metadata package
```

The repository does **not** claim semantic truth, automatic conflict-free merging, authorship adjudication, universal format conversion, external-validator certification, publisher-policy compliance, or independent reproducibility from metadata alone.

## Capability map

| Capability | Status | Current boundary |
|---|---|---|
| `core/renderer.py` | **Implemented** | Jinja2 rendering from JSON, CSV, YAML/YML. SQLite/network adapters are not integrated. |
| `core/ast_engine.py` | **Implemented** | Mistune 3.x AST mapping for the declared Markdown subset, including tables, strikethrough, images, ordered lists and explicit unsupported-node failure. |
| `core/incremental.py` | **Implemented** | SHA-256-backed structural add/modify/delete/unchanged reporting with atomic bounded history persistence. Not a merge engine. |
| `core/cross_ref.py` | **Implemented** | Local Markdown reference graph, heading indexing, aliases, near-miss/dangling diagnostics and recurring-target backlog. |
| `core/frontmatter.py` | **Implemented** | Bounded YAML research metadata plus optional `ai_assistance`, `ai_tools`, `human_review`, and `disclosure_ref`. Process metadata is not authorship/peer-review/scientific validation. |
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

## Research metadata and process disclosure

Optional YAML frontmatter can carry a compact, portable research-document contract:

```yaml
---
title: Evidence synthesis
description: Structured summary of declared sources
status: draft
updated: 2026-08-26
authors: [lostlight530]
sources:
  - https://www.researchobject.org/ro-crate/specification/1.3/
license: MIT
language: en
artifact_id: summary-2026-08-26
ai_assistance: used
ai_tools:
  - provider/model or tool identifier declared by the author
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

Core process-disclosure vocabulary:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

`ai_tools` is a list of human-readable identifiers supplied by the artifact author/producer. The repository does not verify those identifiers against a vendor registry. `disclosure_ref` can point to a fuller methods/process record and is not automatically dereferenced.

Invalid types/enums are errors. Cross-field incompleteness is warning-level—for example, `ai_assistance: used` with no usable `ai_tools` value—so historical documents remain readable while incomplete disclosure stays visible.

These fields answer a narrow question:

> What does this artifact declare about its production and review process?

They do **not** answer:

```text
Who legally/scientifically qualifies as an author?
Was the content peer reviewed?
Is the named model/tool identity independently proven?
Is the document scientifically correct?
Does it satisfy a publisher's AI policy?
```

Unknown fields remain warnings for forward compatibility. The schema is intentionally small; it is not a complete bibliographic or publishing-policy ontology. See [PROCESS_DISCLOSURE.md](PROCESS_DISCLOSURE.md).

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

`doctor` reports unresolved links, orphans, selected directed cycles, frontmatter issues—including invalid process-disclosure metadata—readability signals and graph statistics. `--strict` only changes the command's local exit-status policy; it does not create a repository or GitHub merge gate.

SARIF uses stable namespaced rule IDs and `autoDocFinding/v1` partial fingerprints. The project uses SARIF as a standards-based findings container, not as a claim that document diagnostics are source-code static analysis or scientific review.

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

RO-Crate 1.3 was released on 2026-06-22 and is the current long-term release observed for this refresh. The repository has a concrete writer rather than a documentation-only proposal.

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

**Boundary:** `auto-doc-engine/ro-crate@1` describes the repository's implementation profile in documentation/manifest. Generated JSON-LD is not labelled external-validator-certified unless an external validator is actually run and recorded.

The new `ai_assistance` / `ai_tools` / `human_review` / `disclosure_ref` fields are project frontmatter metadata. The current RO-Crate writer does **not** automatically assert them as RO-Crate standard properties.

## Reproducibility semantics

The shared research contract uses local project terminology:

- **R0 Traceable** — source and artifact identity metadata exist.
- **R1 Replay-addressable** — inputs/configuration/tool revision identify the intended replay.
- **R2 Environment-bounded** — relevant runtime/dependency assumptions are also recorded.
- **R3 Reproduced** — a separate rerun was actually performed and compared under a declared criterion.

A checksum, SARIF file, process disclosure, manifest, or RO-Crate metadata file alone does not establish R3.

## Cross-repository handoff

The intended loose chain is:

```text
auto-doc-engine
artifact identity + declared AI/human-review context
        ↓
epistemic-pipeline
claim-index@1 + evidence-envelope@2 + provider/review disclosure
        ↓
sci-render-kit
figure-claim-binding@1 + figure-evidence@2
```

Preferred Auto Doc handoff fields now include:

```text
artifact_id
content_sha256
source_refs[]
document_status
generated_with
provenance_ref
validation_status
reproducibility_level
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

This is an interoperability convention, not direct runtime coupling.

## Experimental modules

The experimental files remain intentionally separate from the canonical pipeline:

- `template_prewarm.py` — bounded in-memory LRU cache for caller-produced render results;
- `async_conduit.py` — priority scheduling with bounded queue/concurrency for caller handlers;
- `memory_lattice.py` — local JSON node/link store with rounded numeric indexes;
- `restart_protocol.py` — event replay whose determinism depends on deterministic caller handlers;
- `self_observe.py` — descriptive event instrumentation and timing summaries.

The historical names are retained for API continuity. They are not evidence of autonomous optimization, semantic memory, mathematical lattices, or universal deterministic recovery.

## Current external observations

Standards/dependency observations retained from the 2026-08-23 calibration:

- RO-Crate: 1.3 current long-term release, published 2026-06-22;
- SARIF: 2.1.0 with Approved Errata 01 remains the target interchange standard;
- Mistune: 3.3.4 observed current; repository floor remains `>=3.2.1`;
- Pandoc: 3.10.2 observed current and remains optional/environment-dependent;
- Citation File Format: 1.2.0 remains the repository citation metadata format.

The 2026-08-26 research calibration additionally tracks the growing emphasis on re-openable provenance, claim-aware artifact observability, transparency and human oversight in AI-assisted science. Those external signals motivate inspectable metadata; they do not certify this repository.

## Local maintenance tools

When useful, contributors can run the existing local checks:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

They are manual maintenance aids, **not GitHub Actions, branch protection, or merge gates**. Optional converter availability and external standards validation remain separate evidence. No test suite is used as a completion gate for this 2026-08-26 maintenance pass.

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
├── PROCESS_DISCLOSURE.md
├── FRONTIER_ALIGNMENT.md
├── MANIFEST.yaml
└── CITATION.cff
```

## Scientific-integrity boundaries

- Provenance is not truth.
- A digest is byte identity under a declared algorithm, not semantic equivalence.
- Structural diff is not conflict resolution.
- AI/process disclosure is not authorship adjudication or output-validity proof.
- Human review is not peer review or scientific validation.
- Readability heuristics are not peer review or accessibility conformance.
- RO-Crate metadata improves research-object interoperability but does not prove reproducibility.
- Optional tools that are absent produce explicit unsupported/error states.
- Experimental modules remain experimental until they are deliberately integrated into the canonical architecture.

## Citation and license

Citation metadata is provided in `CITATION.cff` using CFF 1.2.0. License: MIT.
