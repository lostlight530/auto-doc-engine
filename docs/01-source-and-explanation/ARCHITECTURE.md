# Architecture — auto-doc-engine

> Calibrated 2026-08-31. This document describes implemented behavior, active maintenance surfaces, and bounded experimental modules. It is not GitHub merge policy.

## Thesis

Research-document automation is treated as a **compiler + artifact-evidence + lineage + Research Object packaging + maintenance** problem

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
       ├─ assertion basis
       ├─ reference-resolution states
       └─ dimensional audit coverage
  -> optional artifact-lineage
       ├─ typed caller-declared relations
       └─ non-inheritance boundaries
  -> optional RO-Crate 1.3

repository state
  -> daily / weekly / monthly maintenance scanner
       ├─ canonical document/path inventory
       ├─ stable-profile checks
       ├─ calendar/stage status
       └─ optional SHA-256 baseline
```

The architecture optimizes for inspectability, stable identity, explicit failure, portable handoff, and preservation of research context across artifact generations

It does not turn document automation or repository maintenance into scientific truth inference

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

Project-owned identifiers do not carry decorative `@1/@2` or `/v1` suffixes

Real external/runtime versions remain provenance when genuinely known

## Data-binding boundary

`core/renderer.py` supports JSON, CSV and YAML/YML through Jinja2

`strict=False` preserves permissive historical loading

`strict=True` makes missing/unsupported input and invalid top-level structures explicit failures

Not integrated: SQLite/database connections, network-backed fetching, credentials, or automatic schema inference

## Typed Markdown boundary

`core/ast_engine.py` provides the integrated normalized Markdown structure

Supported nodes include headings, paragraphs/text, code, lists, tables, blockquotes, emphasis variants, links/images, and line breaks

AST/subtree SHA-256 values are representation identities, not universal semantic hashes

Parse/render normalizes supported Markdown and does not promise byte-for-byte round-trip fidelity

## Structural-change plane

`core/incremental.py` computes `add / modify / delete / unchanged` with local structural identities and sibling alignment

It is a change detector, not automatic patching, conflict resolution, ownership negotiation, CRDT/OT merge, or semantic-equivalence proof

## Document graph and metadata

`core/cross_ref.py` indexes local document/heading references and exposes dangling/near-miss/recurring diagnostics

Near-miss suggestions are lexical hints only

`core/frontmatter.py` provides bounded research metadata and declarative process disclosure

Missing provider/model/version/review information stays unknown/not-declared

```text
process disclosure != authorship proof
human review != peer review
source ref != source credibility
```

The canonical path does not perform automatic AI-text detection

## Doctor and SARIF

`core/doctor.py` emits `auto-doc-engine/doctor` diagnostics

Exit status is a local caller signal only

`core/sarif.py` emits `auto-doc-engine/sarif` using SARIF 2.1.0 + Approved Errata 01

`autoDocFinding` is the stable project fingerprint namespace

SARIF ingestion is interoperability, not scientific certification

## Synchronization

`core/sync.py` keeps built-in behavior separate from optional tools

- Markdown: Python `shutil.copy2`
- HTML: Pandoc when available, Mistune fallback otherwise
- DOCX/EPUB: Pandoc
- PDF: Pandoc + declared PDF engine

External processes use argument arrays rather than `shell=True`

Optional artifact-record and RO-Crate output remain opt-in

## Artifact-record plane

`core/artifact_record.py` emits `auto-doc-engine/artifact-record`

It can record

- source/derivative SHA-256 identities
- selected metadata identity
- declared source/author refs
- process disclosure
- bounded frontmatter validation
- lineage/configuration/validation refs
- execution context
- local R0–R3 state
- assertion basis
- dimensional audit coverage

Payload prose is not duplicated by default

Local files may be hashed while URI/opaque references remain unresolved unless separately handled

## Assertion-basis plane

Important fields carry explicit acquisition basis such as

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
```

Examples

| Field | Basis |
|---|---|
| source/derivative SHA-256 | runtime-observed local bytes |
| bounded document metadata | document frontmatter |
| declared authors/sources | document frontmatter |
| process disclosure | document frontmatter |
| `generated_with` | caller-declared when supplied |
| lineage references | caller-declared, optionally resolved locally |

```text
assertion basis != truth
```

A field can have precise provenance and still be wrong

## Audit-coverage plane

The artifact record computes descriptive dimensions rather than a synthetic quality score

```text
derivative_count
declared-source resolution counts + local_file_ratio
lineage-reference resolution counts + local_file_ratio
process-disclosure declared fields
frontmatter error/warning counts
```

No aggregate quality score is computed

```text
coverage != correctness
coverage ratio != probability
local-file resolution != source credibility
reference presence != evidence sufficiency
```

The repository does not implement provenance soundness or scientific evidence verification

## Artifact-lineage plane

`core/artifact_lineage.py` emits `auto-doc-engine/artifact-lineage`

Bounded relation vocabulary

```text
derived-from
revision-of
supersedes
uses
related-to
```

Relations are caller-declared

Local targets may be hashed; URI/opaque references remain offline

The module does not infer lineage from filenames, timestamps, prose similarity, Git history, or model output

Every relation preserves

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

## RO-Crate plane

`core/ro_crate.py` targets external RO-Crate 1.3 and uses standards-facing JSON-LD for the metadata descriptor, root Dataset, File/Person entities, and SHA-256 PropertyValue records

`auto-doc-engine/ro-crate` is only the stable project exporter identity

No external validator, Workflow/Process/Provenance Run Crate conformance, or scientific reproducibility is claimed

## Why artifact record, lineage, and RO-Crate are distinct

```text
auto-doc-engine/artifact-record
  one artifact/derivative handoff
        ↓ optional relationship
auto-doc-engine/artifact-lineage
  project history/dependency relation layer
        ↓ optional packaging
RO-Crate 1.3
  external Research Object packaging
```

They can be linked without collapsing vocabularies or scientific claims

## Reproducibility semantics

- R0 Traceable
- R1 Replay-addressable
- R2 Environment-bounded
- R3 Reproduced only after an actual separate rerun plus declared comparison

A checksum, SARIF report, artifact record, lineage record, maintenance baseline, or crate cannot self-award R3

## Maintenance plane

`core/maintenance_cadence.py` emits `auto-doc-engine/maintenance-report`

`maintenance/cadence.yaml` defines canonical paths, scan paths, the current stage, cadence behavior, and governance exclusions

Daily / weekly / monthly responsibilities are defined in `MAINTENANCE_CADENCE.md`

Document authority and historical roles are defined in `DOCUMENT_STATUS.md`

The scanner can report

```text
canonical path presence
decorative project profile versions
Manifest calibration age
historical snapshot inventory
canonical SHA-256 baseline
calendar month status
configured stage status
```

For 2026-08-31

```text
calendar_month: calendar-month-close
stage: closed
```

The scanner is read-only and does not run tests, call GitHub, dereference remote resources, delete history, or establish scientific validity

## Document-governance plane

Current contracts, examples, external metadata, and historical snapshots are explicitly classified in `DOCUMENT_STATUS.md`

Historical

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

remain time-scoped snapshots rather than current architecture contracts

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

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

References do not create hidden imports or inherited scientific validity

## Stage-close global calibration

The 2026-08-24 → 2026-08-31 stage is informed by

- autonomous-science provenance as a complete, re-openable corrective record
- transparent AI-use and human-oversight requirements in scientific publishing
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency
- claim-level auditability and contradiction transparency
- long-horizon phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments / recovery
- process-level long-horizon evaluation beyond final scores
- Praxist solution/evidence lineage
- ReproAgent persistent contracts
- living research-software metadata and maintenance

These are design signals, not validation, endorsement, novelty proof, or conformance evidence

## Experimental surfaces

- `template_prewarm.py`: bounded in-memory LRU cache
- `async_conduit.py`: bounded priority scheduler
- `memory_lattice.py`: local node/link store + numeric bucket index
- `restart_protocol.py`: event replay with result-hash verification
- `self_observe.py`: explicit instrumentation and descriptive timing

Historical metaphorical names are not capability claims

## Hard invariants

```text
Provenance != Truth
Hash identity != semantic equivalence
Structure != meaning
Structural change != conflict resolution
Assertion basis != correctness
Audit coverage != quality
Coverage ratio != probability
Artifact lineage != inherited scientific validity
Declared source != source credibility
Process disclosure != authorship proof
Human review != peer review
Artifact record != external standard
RO-Crate packaging != reproduction
Maintenance clean != scientific validation
Calendar-month close != reproduction
Local diagnostics != scientific validation
```

GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, and merge-gate architecture remain outside the repository design
