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

Read `JULES_CORRECTION_RECORD.md` before using early Jules task/PR text as evidence of current behavior

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
historical agent PR narrative != current contract
```

### Recovery order

When rebuilding repository truth, use:

```text
current main implementation
> MANIFEST.yaml and current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active specialized contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> Architecture / README
> historical consolidation snapshots
> historical PR / task narratives
```

An agent-generated PR body is never a substitute for inspecting the actual current tree.

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
27. Jules/Codex/other agent task text, PR bodies, generated summaries, and completion claims are proposal/delivery metadata, not automatic repository authority
28. Historical `tests passed`, `100%`, `fully aligned`, `fixed`, or similar claims require current re-verification before they are reused as current facts
29. Correct historical agent overstatement forward in current records; do not silently edit or reinterpret old PR history as if the correction were contemporaneous

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

`MAINTENANCE_CADENCE.md`, `DOCUMENT_STATUS.md`, `JULES_CORRECTION_RECORD.md`, `STAGE_2026_08_MAINTENANCE.md`, and `maintenance/cadence.yaml` define the active maintenance/document-governance system

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
- read the latest dated repair/current maintenance record before older snapshots or PR narratives
- use `JULES_CORRECTION_RECORD.md` when early Jules work is relevant
- do not rewrite historical snapshots or historical PR prose
- do not manufacture work merely to produce a daily commit

Weekly maintenance

- reconcile implementation, Manifest, active contracts, README/Architecture, Agent/Contributor guidance, examples, Document Status, Frontier Alignment, current correction/maintenance records, and cross-repository profile names
- inventory prior stage snapshots without rewriting them
- audit whether coding-agent narratives are being treated as current authority without current evidence
- use canonical hashes when a deterministic baseline is useful

If the same pass performs Daily and Weekly maintenance, one branch and one final PR should carry the combined real work whenever practical. Do not create duplicate churn solely because two cadence labels apply.

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

Current Daily/Weekly governance reconciliation

```text
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
```

Read dated records after the active cadence contract and document-status map. They are time-scoped maintenance evidence, not automatic runtime proof.

```text
reference demonstration != runtime proof
maintenance clean != scientific validity
weekly consistency != proof of correctness
calendar-month close != reproduction
history inventory != deprecation decision
agent narrative != current verification
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
| maintenance cadence / agent provenance | `core/maintenance_cadence.py`, `maintenance/cadence.yaml`, `JULES_CORRECTION_RECORD.md` | Maintenance Cadence + Document Status + Agent Guide + current dated maintenance record; synchronize Manifest only when capability/profile semantics change |
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
