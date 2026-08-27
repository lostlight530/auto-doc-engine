# auto-doc-engine

> AST-driven research-document compilation, structural-change evidence, process-aware metadata, portable artifact records, diagnostics, SARIF interchange, and optional RO-Crate 1.3 packaging.

[简体中文](README_zh.md) · [Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [Process Disclosure](PROCESS_DISCLOSURE.md) · [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Examples](examples/README.md)

## Positioning

`auto-doc-engine` treats a research document as an **inspectable artifact**, not an opaque string and not merely a final PDF.

The canonical path is:

```text
JSON / CSV / YAML
        ↓
Jinja2 document binding
        ↓
Typed Markdown AST
        ↓
Structural change evidence
        ↓
Cross-document graph + bounded metadata diagnostics
        ↓
Declared AI / human-review process context
        ↓
Text / JSON / SARIF findings
        ↓
Markdown / optional Pandoc formats
        ↓
optional artifact-record@1
        ↓
optional RO-Crate 1.3 packaging
```

The repository optimizes for **identity, inspectability, explicit failure and portable handoff**.

It does **not** claim:

- semantic truth;
- automatic conflict-free merging;
- source-credibility adjudication;
- authorship adjudication;
- peer review;
- universal format conversion;
- external RO-Crate validator certification;
- Workflow Run Crate conformance;
- publisher-policy compliance;
- independent reproducibility from metadata alone.

## Capability map

| Capability | Status | Current boundary |
|---|---|---|
| `core/renderer.py` | **Implemented** | Jinja2 rendering from JSON, CSV, YAML/YML. SQLite/network adapters are not integrated. |
| `core/ast_engine.py` | **Implemented** | Mistune 3.x typed AST for the declared Markdown subset; normalized rendering, not byte-preserving round trip. |
| `core/incremental.py` | **Implemented** | SHA-256-backed add/modify/delete/unchanged structural reports with bounded atomic history. Not a merge engine. |
| `core/cross_ref.py` | **Implemented** | Local Markdown document/heading graph, aliases, dangling/near-miss diagnostics and recurring-target backlog. |
| `core/frontmatter.py` | **Implemented** | Bounded research metadata plus optional AI-assistance / tool / human-review disclosure. |
| `core/readability.py` | **Implemented** | Descriptive Latin/CJK heuristics with fenced-code exclusion. Not writing-quality or peer-review scoring. |
| `core/doctor.py` | **Implemented** | Aggregated local document diagnostics with Text/JSON output and explicit local exit status. |
| `core/sarif.py` | **Implemented** | Conservative SARIF 2.1.0 + Approved Errata 01 findings profile. |
| `core/sync.py` | **Implemented / optional converters** | Cross-platform Markdown copy; optional Pandoc HTML/DOCX/PDF/EPUB; Mistune HTML fallback. |
| `core/artifact_record.py` | **Implemented profile** | `auto-doc-engine/artifact-record@1`: one source document + derivative identities + metadata/process/diagnostic context. Project-owned, not an external standard. |
| `core/ro_crate.py` | **Implemented profile** | Core RO-Crate 1.3 JSON-LD for local artifact sets. No external-validator certification claim. |
| `template_prewarm`, `async_conduit`, `memory_lattice`, `restart_protocol`, `self_observe` | **Experimental** | Standalone bounded reference modules; not wired into the canonical pipeline. |

## Data binding

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
assert markdown
```

Supported suffixes:

```text
.json
.csv
.yaml
.yml
```

`strict=False` preserves historical permissive behavior. `strict=True` makes missing/unsupported input and invalid top-level structures explicit failures.

## Research metadata and process disclosure

Optional frontmatter:

```yaml
---
title: Evidence synthesis
description: Structured summary of declared sources
status: draft
updated: 2026-08-27
authors: [lostlight530]
sources:
  - https://www.researchobject.org/ro-crate/specification/1.3/
license: MIT
language: en
artifact_id: summary-2026-08-27
ai_assistance: used
ai_tools:
  - declared provider/model/tool identifier
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

Bounded disclosure vocabulary:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Cross-field inconsistencies are warning-level. For example, `ai_assistance: used` with no usable `ai_tools` remains visible without making an old document unreadable.

Hard boundary:

```text
AI disclosure != authorship proof
AI tool label != provider provenance proof
human_review=reviewed != peer review
process metadata != scientific validity
```

See [PROCESS_DISCLOSURE.md](PROCESS_DISCLOSURE.md).

## Portable artifact record

The 2026-08-27 consolidation adds:

```text
auto-doc-engine/artifact-record@1
```

It fills the gap between frontmatter and a full Research Object package.

A record can preserve:

- source document byte identity;
- successful derivative byte identities;
- selected bounded metadata;
- declared authors and source references;
- process disclosure;
- frontmatter/schema diagnostics;
- configuration/provenance/validation references;
- execution context;
- local R0–R3 reproducibility declaration;
- explicit scientific/authorship/peer-review boundary flags.

Standalone:

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync@1 \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

Programmatically:

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

Or opt in through `sync/targets.yaml`:

```yaml
artifact_record:
  emit: true
  reproducibility_level: R1
```

The default is `emit: false` for backwards-compatible output behavior.

See [ARTIFACT_RECORD.md](ARTIFACT_RECORD.md).

## Artifact record versus RO-Crate

These are complementary layers:

```text
artifact-record@1
  small project handoff for one source/derivative set

RO-Crate 1.3
  external linked-data packaging for a broader Research Object
```

If both are enabled, SyncEngine emits the artifact record first. The RO-Crate writer can then include that JSON file as an ordinary payload.

The project does **not** relabel `artifact-record@1` as a standard RO-Crate entity/profile and does not claim Workflow/Process/Provenance Run Crate conformance.

This follows a useful separation-of-concerns principle visible in Research Object and Workflow Run Crate work: **data products and execution/provenance records are related objects, not the same semantic object**.

## Diagnostics and SARIF

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/doctor.py path/to/docs --strict
python core/sarif.py path/to/docs -o output/doctor.sarif
```

Doctor currently reports:

- unresolved local Markdown links;
- orphan documents;
- selected directed cycles;
- bounded frontmatter/process-disclosure issues;
- descriptive readability signals;
- document-graph statistics.

`--strict` changes only the local command exit-status policy. It does not create a GitHub merge gate or scientific validity check.

SARIF is used as a standardized findings container. A SARIF consumer parsing the file does not certify the findings or the science.

## Format synchronization

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
```

Environment boundary:

- Markdown copy: Python stdlib;
- HTML: Pandoc when available, Mistune fallback otherwise;
- DOCX/EPUB: Pandoc;
- PDF: Pandoc + declared PDF engine;
- external converter availability is explicit rather than inferred.

No `shell=True` path is required.

## RO-Crate 1.3

RO-Crate 1.3 is the current external Research Object packaging target used by this repository.

```bash
python core/ro_crate.py output report.md report.html \
  --name "Research artifact set" \
  --description "Rendered report and interoperable metadata" \
  --author lostlight530 \
  --license MIT
```

Current implementation emits:

- `ro-crate-metadata.json` metadata descriptor as `CreativeWork`;
- `./` root `Dataset`;
- local payload `File` entities;
- `contentSize` / `encodingFormat`;
- contextual `Person` entities;
- SHA-256 byte identities through Schema.org `PropertyValue`.

Boundary:

```text
RO-Crate file generated != external validator passed
RO-Crate metadata != independent reproduction
RO-Crate packaging != scientific validity
```

## Reproducibility semantics

Local project vocabulary:

- **R0 Traceable** — source/artifact association and identity metadata exist.
- **R1 Replay-addressable** — declared input/config/tool identity addresses the intended replay.
- **R2 Environment-bounded** — relevant runtime/dependency boundaries are also recorded.
- **R3 Reproduced** — an actual separate rerun occurred and was compared under a declared criterion.

`artifact_record.py` may carry a caller-declared level, but generating metadata does not itself execute or prove R3.

## Cross-repository handoff

Day-4 chain:

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

No direct imports are required between repositories.

## 2026-08-27 global research calibration

The repository's current design is informed by, but does not claim endorsement or equivalence with:

- Nature Computational Science, **Provenance grounds trust in autonomous science** (20 Aug 2026): complete, re-openable provenance as corrective infrastructure;
- Nature Computational Science, **Responsible and transparent use of AI in scientific publishing** (20 Aug 2026): transparency, accountability and human oversight;
- **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents** (arXiv:2608.18312): artifacts/claims/relations need first-class audit structure beyond model-call logs;
- **EarthVerse** (arXiv:2608.23525): local task competence does not guarantee end-to-end scientific-chain consistency;
- RO-Crate 1.3 and Workflow Run Crate family: data products and execution/provenance descriptions benefit from explicit linked but distinct representations.

See [FOUR_DAY_CONSOLIDATION.md](FOUR_DAY_CONSOLIDATION.md) and [FRONTIER_ALIGNMENT.md](FRONTIER_ALIGNMENT.md).

## Experimental modules

Still outside the canonical pipeline:

- `template_prewarm.py` — bounded in-memory LRU cache;
- `async_conduit.py` — bounded priority/concurrency scheduler for caller handlers;
- `memory_lattice.py` — local node/link store + rounded numeric index;
- `restart_protocol.py` — event replay with result-hash checks; determinism depends on caller handlers;
- `self_observe.py` — explicit instrumentation and descriptive timing.

Historical metaphorical names are not capability claims.

## Local maintenance

Optional:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

These are local maintenance aids, not repository architecture, GitHub Actions, branch protection, merge gates, peer review or scientific validation.

The 2026-08-27 consolidation does **not** use test execution as completion evidence; completion is based on static interface/profile/document consistency and branch diff auditing.

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
│   ├── artifact_record.py
│   ├── ro_crate.py
│   └── experimental modules
├── templates/jinja2/
├── sync/targets.yaml
├── examples/
├── tests/                  # optional local maintenance checks
├── RESEARCH_CONTRACT.md
├── ARTIFACT_RECORD.md
├── PROCESS_DISCLOSURE.md
├── FOUR_DAY_CONSOLIDATION.md
├── FRONTIER_ALIGNMENT.md
├── MANIFEST.yaml
└── CITATION.cff
```

## Scientific-integrity boundaries

```text
Provenance != Truth
Digest != semantic equivalence
Structural diff != conflict resolution
Declared source != credible source by definition
Artifact record != external Research Object standard
Process disclosure != authorship adjudication
Human review != peer review
RO-Crate metadata != reproduction
Standard alignment != external certification
Experimental source != integrated capability
```

## Citation and license

Citation metadata: `CITATION.cff` using CFF 1.2.0.  
License: MIT.
