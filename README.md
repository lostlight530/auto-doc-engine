# auto-doc-engine

> AST-driven research-document compilation, structural-change evidence, bounded process metadata, portable artifact records, explicit artifact lineage, dimensional audit coverage, SARIF interchange, optional RO-Crate 1.3 packaging, and phase-aware repository maintenance

[简体中文](README_zh.md) · [Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [Artifact Lineage](ARTIFACT_LINEAGE_CONTRACT.md) · [Assertion Basis & Coverage](ASSERTION_BASIS_AND_COVERAGE.md) · [Process Disclosure](PROCESS_DISCLOSURE.md) · [Maintenance](MAINTENANCE_CADENCE.md) · [Document Status](DOCUMENT_STATUS.md) · [August Stage Close](STAGE_2026_08_MAINTENANCE.md) · [Examples](examples/README.md)

## Positioning

`auto-doc-engine` treats a research document as an inspectable artifact rather than an opaque string or merely a final PDF

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
  ├─ assertion basis
  └─ dimensional audit coverage
        ↓
optional artifact-lineage
  ├─ typed caller-declared relations
  └─ explicit non-inheritance boundaries
        ↓
optional RO-Crate 1.3 packaging
```

The repository optimizes for identity, inspectability, explicit failure, portable handoff, and preservation of research context across artifact generations

It does not claim semantic truth, conflict-free merging, source-credibility adjudication, authorship adjudication, peer review, universal conversion, external RO-Crate certification, Run Crate conformance, publisher-policy compliance, or independent reproduction from metadata alone

## Stable project identifiers

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
auto-doc-engine/maintenance-cadence
auto-doc-engine/maintenance-report
autoDocFinding
```

Project-owned identifiers intentionally have no decorative `@1/@2` or `/v1` suffixes

Real external standards and observed runtime/software versions remain valid provenance, including RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01, and CFF 1.2.0

## Capability map

| Capability | Status | Boundary |
|---|---|---|
| `core/renderer.py` | Implemented | Jinja2 rendering from JSON/CSV/YAML/YML; no integrated SQLite/network adapter |
| `core/ast_engine.py` | Implemented | typed normalized Markdown structure; not byte-preserving |
| `core/incremental.py` | Implemented | add/modify/delete/unchanged structural evidence; not a merge engine |
| `core/cross_ref.py` | Implemented | local Markdown graph and dangling/near-miss diagnostics |
| `core/frontmatter.py` | Implemented | bounded research metadata and declarative process disclosure |
| `core/readability.py` | Implemented | descriptive heuristics only |
| `core/doctor.py` | Implemented | document-set diagnostics and local exit status |
| `core/sarif.py` | Implemented | SARIF 2.1.0 + Approved Errata 01 export |
| `core/sync.py` | Implemented / optional converters | Markdown copy; optional Pandoc/Mistune paths |
| `core/artifact_record.py` | Implemented project contract | source/derivative identity + assertion basis + dimensional audit coverage |
| `core/artifact_lineage.py` | Implemented project contract | typed declared artifact relations + explicit non-inheritance |
| `core/ro_crate.py` | Implemented core exporter | RO-Crate 1.3 JSON-LD; no external-validator claim |
| `core/maintenance_cadence.py` | Implemented maintenance scanner | read-only local daily/weekly/monthly structural maintenance evidence |
| experimental modules | Experimental | bounded standalone references, not canonical pipeline |

## Data binding

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
```

Supported suffixes: `.json`, `.csv`, `.yaml`, `.yml`

`strict=False` preserves permissive historical behavior

`strict=True` makes missing/unsupported input and invalid top-level structures explicit failures

## Research metadata and process disclosure

Optional frontmatter may declare artifact ID, authors, sources, license, DOI, language, AI assistance, AI tool identifiers, human review, and a disclosure reference

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Unknown information remains unknown/not-declared

```text
AI disclosure != authorship proof
AI tool label != verified provider provenance
human review != peer review
process metadata != scientific validity
```

The repository does not inspect prose and infer AI use

Artifact records explicitly state `automatic_ai_detection_used: false` for this path

## Assertion basis

A recorded value is separated from the way it entered the artifact record

Current bases include

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
```

Examples

```text
document metadata
  -> document-frontmatter

source/derivative SHA-256
  -> runtime-observed-local-bytes

generated_with
  -> caller-declared when supplied
```

A basis is provenance for the assertion process, not proof that the value is correct

See [ASSERTION_BASIS_AND_COVERAGE.md](ASSERTION_BASIS_AND_COVERAGE.md)

## Portable artifact record

`auto-doc-engine/artifact-record` fills the gap between frontmatter and a broader Research Object package

It can preserve source/derivative byte identities, bounded metadata, declared source/author refs, process disclosure, frontmatter diagnostics, lineage references, execution context, assertion basis, dimensional audit coverage, and a local R0–R3 reproducibility declaration

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

Programmatically

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

Artifact-record output remains opt-in

## Dimensional audit coverage

Artifact records expose separate coverage dimensions instead of an opaque total quality score

```text
derivative_count
declared_source_references.total / by_resolution / local_file_ratio
lineage_references.total / by_resolution / local_file_ratio
process_disclosure_declared_fields
frontmatter_error_count
frontmatter_warning_count
```

The record deliberately emits

```json
{
  "aggregate_score": null
}
```

Interpretation boundary

```text
local_file_ratio != source credibility
reference presence != citation validity
coverage != correctness
coverage ratio != probability
frontmatter clean != scientific validity
```

## Typed artifact lineage

`auto-doc-engine/artifact-lineage` records declared relationships across artifact generations

Allowed relations

```text
derived-from
revision-of
supersedes
uses
related-to
```

Relations are caller-declared and local targets may be hashed when present

The module does not infer lineage from filenames, timestamps, prose similarity, Git history, or model output

Every edge preserves non-inheritance boundaries

```text
scientific_validity_inherited: false
reproducibility_inherited: false
```

```text
lineage != truth
revision-of != semantic equivalence
supersedes != history deletion
uses != evidence sufficiency
```

See [ARTIFACT_LINEAGE_CONTRACT.md](ARTIFACT_LINEAGE_CONTRACT.md)

## Artifact record, lineage, and RO-Crate

```text
auto-doc-engine/artifact-record
  one source/derivative set
        ↓ optional relationship
auto-doc-engine/artifact-lineage
  typed history/dependency handoff
        ↓ optional packaging
RO-Crate 1.3
  external linked-data Research Object packaging
```

If project records are included in a crate they remain ordinary project payloads and are not relabelled as external standard profiles

## Diagnostics and SARIF

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/sarif.py path/to/docs -o output/doctor.sarif
```

Doctor reports structural/document metadata diagnostics

`--strict` changes only local command exit-status behavior

SARIF is a standardized findings container; parsing it does not certify the findings or science

## Format synchronization

Environment boundary

- Markdown copy: Python stdlib
- HTML: Pandoc when available, Mistune fallback otherwise
- DOCX/EPUB: Pandoc
- PDF: Pandoc plus declared PDF engine
- converter availability is explicit rather than inferred

## RO-Crate 1.3

```bash
python core/ro_crate.py output report.md report.html \
  --name "Research artifact set" \
  --description "Rendered report and interoperable metadata" \
  --author lostlight530 \
  --license MIT
```

The exporter emits conservative core RO-Crate metadata

It does not claim external validator success, Run Crate conformance, independent reproduction, or scientific validity

## Reproducibility semantics

Local project vocabulary

- **R0 Traceable** — source/artifact association exists
- **R1 Replay-addressable** — declared input/config/tool identity addresses intended replay
- **R2 Environment-bounded** — relevant runtime/dependency assumptions are bounded
- **R3 Reproduced** — an actual separate rerun occurred and was compared under a declared criterion

Metadata generation cannot self-award R3

## Maintenance and document authority

Daily / weekly / monthly maintenance is defined in [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md)

Current-vs-historical document authority is defined in [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md)

The closed August stage baseline is [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

The scanner reports local structural maintenance evidence and date-derived calendar/stage status

It does not mutate the repository, run tests, call GitHub, dereference remote references, or establish scientific validity

Current stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

`FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` remain historical snapshots rather than current contracts

## Stage-close research calibration

The 2026-08-24 → 2026-08-31 stage was informed by, but not certified by, work on

- provenance-complete and re-openable autonomous science
- transparent AI use / human oversight in scientific publishing
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency
- claim-level auditability and contradiction transparency
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- long-horizon evaluation beyond final scores
- Praxist solution/evidence lineages
- ReproAgent persistent implementation contracts
- reusable research-software metadata and maintenance

The repository borrows structural audit and maintenance ideas only where it can implement them honestly

It does not claim provenance soundness, source credibility scoring, scientific-review authority, AI-content detection, or external validation from these sources

See [FRONTIER_ALIGNMENT.md](FRONTIER_ALIGNMENT.md) and [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

No direct imports are required between repositories

## Experimental modules

- `template_prewarm.py` — bounded in-memory LRU
- `async_conduit.py` — bounded priority/concurrency scheduler
- `memory_lattice.py` — local node/link store + numeric bucket index
- `restart_protocol.py` — event replay with result-hash verification
- `self_observe.py` — explicit instrumentation and descriptive timing

Metaphorical filenames are not capability claims

## Scientific-integrity boundaries

```text
Provenance != Truth
Digest != semantic equivalence
Structural diff != conflict resolution
Assertion basis != correctness
Coverage != quality
Coverage ratio != probability
Declared source != credible source by definition
Artifact lineage != inherited validity
Artifact record != external Research Object standard
Process disclosure != authorship adjudication
Human review != peer review
RO-Crate metadata != reproduction
Maintenance clean != scientific validity
Calendar-month close != reproduction
Standard alignment != external certification
Experimental source != integrated capability
```

Citation metadata uses CFF 1.2.0

License: MIT
