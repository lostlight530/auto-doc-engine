# auto-doc-engine

> AST-driven research-document compilation, structural-change evidence, bounded process metadata, portable artifact records, SARIF interchange, and optional RO-Crate 1.3 packaging.

[简体中文](README_zh.md) · [Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [Process Disclosure](PROCESS_DISCLOSURE.md) · [Examples](examples/README.md)

## Positioning

`auto-doc-engine` treats a research document as an inspectable artifact rather than an opaque string or merely a final PDF.

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
optional artifact-record
        ↓
optional RO-Crate 1.3 packaging
```

The repository optimizes for identity, inspectability, explicit failure and portable handoff.

It does not claim semantic truth, conflict-free merging, source-credibility adjudication, authorship adjudication, peer review, universal conversion, external RO-Crate certification, Run Crate conformance, publisher-policy compliance or independent reproduction from metadata alone.

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

Project-owned identifiers intentionally have no decorative `@1/@2` or `/v1` suffixes. Real external standards and observed runtime/software versions remain valid provenance, including RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01 and CFF 1.2.0.

## Capability map

| Capability | Status | Boundary |
|---|---|---|
| `core/renderer.py` | Implemented | Jinja2 rendering from JSON/CSV/YAML/YML; no integrated SQLite/network adapter |
| `core/ast_engine.py` | Implemented | typed normalized Markdown structure; not byte-preserving |
| `core/incremental.py` | Implemented | add/modify/delete/unchanged structural evidence; not a merge engine |
| `core/cross_ref.py` | Implemented | local Markdown graph and dangling/near-miss diagnostics |
| `core/frontmatter.py` | Implemented | bounded research metadata and process disclosure |
| `core/readability.py` | Implemented | descriptive heuristics only |
| `core/doctor.py` | Implemented | document-set diagnostics and local exit status |
| `core/sarif.py` | Implemented | SARIF 2.1.0 + Approved Errata 01 export |
| `core/sync.py` | Implemented / optional converters | Markdown copy; optional Pandoc/Mistune paths |
| `core/artifact_record.py` | Implemented project contract | source/derivative identity + declared context |
| `core/ro_crate.py` | Implemented core exporter | RO-Crate 1.3 JSON-LD; no external-validator claim |
| experimental modules | Experimental | bounded standalone references, not canonical pipeline |

## Data binding

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
```

Supported suffixes: `.json`, `.csv`, `.yaml`, `.yml`.

`strict=False` preserves permissive historical behavior. `strict=True` makes missing/unsupported input and invalid top-level structures explicit failures.

## Research metadata and process disclosure

Optional frontmatter may declare artifact ID, authors, sources, license, DOI, language, AI assistance, AI tool identifiers, human review and a disclosure reference.

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Unknown information remains unknown/not-declared.

```text
AI disclosure != authorship proof
AI tool label != verified provider provenance
human review != peer review
process metadata != scientific validity
```

## Portable artifact record

`auto-doc-engine/artifact-record` fills the gap between frontmatter and a full Research Object package.

It can preserve source/derivative byte identities, bounded metadata, declared source/author refs, process disclosure, frontmatter diagnostics, lineage references, execution context and a local R0–R3 reproducibility declaration.

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
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

Artifact-record output remains opt-in.

## Artifact record versus RO-Crate

```text
auto-doc-engine/artifact-record
  small project handoff for one source/derivative set

RO-Crate 1.3
  external linked-data packaging for a broader Research Object
```

If both are enabled, the artifact record may be included as an ordinary crate payload. It is not relabelled as an external RO-Crate profile.

## Diagnostics and SARIF

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/sarif.py path/to/docs -o output/doctor.sarif
```

Doctor reports structural/document metadata diagnostics. `--strict` changes only local command exit-status behavior.

SARIF is a standardized findings container; parsing it does not certify the findings or science.

## Format synchronization

Environment boundary:

- Markdown copy: Python stdlib;
- HTML: Pandoc when available, Mistune fallback otherwise;
- DOCX/EPUB: Pandoc;
- PDF: Pandoc plus declared PDF engine;
- converter availability is explicit rather than inferred.

## RO-Crate 1.3

```bash
python core/ro_crate.py output report.md report.html \
  --name "Research artifact set" \
  --description "Rendered report and interoperable metadata" \
  --author lostlight530 \
  --license MIT
```

The exporter emits conservative core RO-Crate metadata. It does not claim external validator success, Run Crate conformance, independent reproduction or scientific validity.

## Reproducibility semantics

Local project vocabulary:

- **R0 Traceable** — source/artifact association exists;
- **R1 Replay-addressable** — declared input/config/tool identity addresses intended replay;
- **R2 Environment-bounded** — relevant runtime/dependency assumptions are bounded;
- **R3 Reproduced** — an actual separate rerun occurred and was compared under a declared criterion.

Metadata generation cannot self-award R3.

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

No direct imports are required between repositories.

## Experimental modules

- `template_prewarm.py` — bounded in-memory LRU;
- `async_conduit.py` — bounded priority/concurrency scheduler;
- `memory_lattice.py` — local node/link store + numeric bucket index;
- `restart_protocol.py` — event replay with result-hash verification;
- `self_observe.py` — explicit instrumentation and descriptive timing.

Metaphorical filenames are not capability claims.

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

## Maintenance

Local checks may be used manually. They are not repository architecture, GitHub merge policy, peer review or scientific validation. This consolidation does not use test execution as completion evidence.

Citation metadata uses CFF 1.2.0. License: MIT.
