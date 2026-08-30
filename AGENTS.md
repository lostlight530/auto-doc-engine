# Agent Guide — auto-doc-engine

This is the operational contract for agents modifying the repository

Keep code, machine-readable contracts, maintenance records, current documentation, and historical-document status aligned

## Canonical architecture

```text
structured data
  -> renderer
  -> typed Markdown AST
  -> structural diff / document graph / frontmatter
  -> Doctor / JSON / SARIF
  -> sync
     -> rendered derivatives
     -> optional artifact-record
          ├─ assertion basis
          └─ dimensional audit coverage
     -> optional artifact-lineage
          ├─ typed caller-declared relations
          └─ explicit non-inheritance boundaries
     -> optional RO-Crate 1.3

repository state
  -> daily / weekly / monthly maintenance
     -> document authority + stage/calendar status
```

Integrated core includes `renderer.py`, `ast_engine.py`, `incremental.py`, `cross_ref.py`, `frontmatter.py`, `readability.py`, `doctor.py`, `sarif.py`, `sync.py`, `artifact_record.py`, `artifact_lineage.py`, `maintenance_cadence.py`, and `ro_crate.py`

Experimental and not integrated: `template_prewarm.py`, `async_conduit.py`, `memory_lattice.py`, `restart_protocol.py`, `self_observe.py`

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

Do not invent `@1`, `@2`, `/v1`, or similar internal counters

Preserve real external/runtime versions when known, including RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01, and CFF 1.2.0

## Document authority

Read `DOCUMENT_STATUS.md` before broad documentation maintenance

Current authoritative documents may be updated when current source truth changes

Historical consolidation snapshots must not be treated as current contracts

Historical files currently include

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## Hard rules

1. Structural Markdown changes go through the typed AST rather than regex mutation
2. Keep SHA-256 on document/artifact identity surfaces and do not reintroduce MD5
3. External converters use argument lists and must not introduce `shell=True`
4. Optional dependencies and unavailable states stay explicit
5. Normalized Markdown is not byte-preserving round-trip fidelity
6. Structural diff is not merge or conflict resolution
7. Near-miss/readability values are heuristics, not semantic truth
8. Process disclosure is declarative and human review is not peer review
9. The canonical path does not perform AI-text detection
10. `artifact-record` is project-owned and is not RO-Crate/PROV/Run Crate conformance
11. Artifact records do not embed complete document payloads by default
12. Local files may be hashed while URI/opaque refs remain offline references unless a separate resolver exists
13. Assertion basis records how a value entered the record and never upgrades it to truth
14. Coverage remains dimensional and must not become a synthetic research-quality score
15. Coverage ratio must never be relabelled probability, evidence sufficiency, or source credibility
16. Artifact-lineage relations are caller-declared and must not be inferred from filenames, timestamps, prose similarity, Git history, or model output
17. `supersedes` never authorizes deletion or rewrite of predecessor history
18. `revision-of` does not establish semantic equivalence and `uses` does not establish evidence sufficiency
19. Artifact-lineage references never inherit scientific validity or reproducibility
20. Metadata generation never self-awards R3 reproduction
21. Standards-facing RO-Crate JSON-LD must not be polluted with invented project vocabulary
22. Experimental modules remain Experimental until intentionally integrated
23. Unknown provider/model/version/source/review state remains unknown and must never be guessed
24. Calendar/month/stage status must come from actual date/configuration, not agent assumption
25. A worked maintenance demonstration must never be presented as a clean runtime result unless the scanner was actually executed and the output is preserved
26. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture

## Artifact-record invariants

`auto-doc-engine/artifact-record` may index source/derivative byte identities, selected metadata identity, declared sources/authors, process disclosure, bounded frontmatter validation, lineage/config refs, execution context, assertion basis, dimensional audit coverage, and a local reproducibility state

```text
hash != semantic equivalence
assertion basis != correctness
coverage != quality
coverage ratio != probability
source ref != source credibility
validation clean != factual correctness
human review != peer review
artifact record != external standard
```

## Artifact-lineage invariants

`auto-doc-engine/artifact-lineage` may carry only

```text
derived-from
revision-of
supersedes
uses
related-to
```

Every relation is caller-declared and may optionally resolve/hash a local target

```text
lineage != truth
reference != inherited validity
supersedes != history deletion
revision != semantic equivalence
uses != evidence sufficiency
lineage coverage != provenance soundness
```

If artifact records or lineage records are packaged into RO-Crate, keep them as normal project files and do not relabel them as standard RO-Crate profiles

## Maintenance cadence

`MAINTENANCE_CADENCE.md`, `DOCUMENT_STATUS.md`, `STAGE_2026_08_MAINTENANCE.md`, and `maintenance/cadence.yaml` define the active maintenance/document-governance system

Local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Daily maintenance

- start from current `main`
- correct local factual/profile/contract drift only
- use `DOCUMENT_STATUS.md` to distinguish current vs historical files
- do not rewrite historical snapshots
- do not manufacture work merely to produce a daily commit

Weekly maintenance

- reconcile implementation, Manifest, active contracts, README/Architecture, Agent/Contributor guidance, examples, Document Status, Frontier Alignment, and cross-repository profile names
- inventory prior stage snapshots without rewriting them
- use canonical hashes when a deterministic baseline is useful

Monthly or explicit phase-close maintenance

- determine month-close status from the actual date
- reconcile the complete current document set
- inventory history and review deprecation candidates manually
- never automatically delete or rewrite historical evidence
- record whether the calendar month and research phase are actually closed

For the current closed stage

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

First complete worked example

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

Read it after the active cadence contract and document-status map
It is a dated reference demonstration, not a clean scanner log
If future cadence semantics materially change, create a new dated demonstration rather than rewriting this one into a different historical state

```text
reference demonstration != runtime proof
maintenance clean != scientific validity
weekly consistency != proof of correctness
calendar-month close != reproduction
history inventory != deprecation decision
```

## Change ownership

| Goal | Primary files | Synchronize |
|---|---|---|
| data source | `core/renderer.py` | README pair + Architecture pair + Manifest |
| Markdown node | `core/ast_engine.py` | incremental/cross-ref compatibility + docs |
| diff semantics | `core/incremental.py` | Research Contract + docs |
| graph/link semantics | `core/cross_ref.py` | Doctor/SARIF semantics + docs |
| metadata/process field | `core/frontmatter.py` | Process Disclosure + Artifact Record + docs |
| assertion basis / coverage | `core/artifact_record.py` | Assertion Basis contract + Artifact Record + Manifest + examples |
| artifact lineage | `core/artifact_lineage.py` | Artifact Lineage Contract + Manifest + examples + frontier notes |
| maintenance cadence | `core/maintenance_cadence.py`, `maintenance/cadence.yaml` | Maintenance Cadence + Document Status + Stage index + Manifest + Agent Guide; create a new dated demonstration only when a new reference example is required |
| conversion target | `core/sync.py`, `sync/targets.yaml` | dependency docs + artifact record semantics |
| RO-Crate entity/relation | `core/ro_crate.py` | Research Contract + Manifest + examples |
| public capability | README / Architecture / Contracts / Manifest | update together when semantics change |

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  -> auto-doc-engine/artifact-lineage
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/claim-transfer
  -> epistemic-pipeline/evidence-envelope
  -> sci-render-kit/figure-claim-audit
  -> sci-render-kit/figure-evidence
  -> sci-render-kit/communication-transfer
```

These are optional references/handoffs, not direct imports or inherited scientific validity

## Local maintenance boundary

Manual checks may be used when useful

Their success is not evidence of external converter availability, standards certification, peer review, scientific truth, or independent reproduction
