# Agent Guide — auto-doc-engine

This is the operational contract for agents modifying the repository.

Keep code, machine-readable contracts, maintenance control, current documentation, and historical-document status aligned without turning agent narrative into repository truth.

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
     -> document authority + stage/calendar status + delivery provenance
```

Integrated core includes `renderer.py`, `ast_engine.py`, `incremental.py`, `cross_ref.py`, `frontmatter.py`, `readability.py`, `doctor.py`, `sarif.py`, `sync.py`, `artifact_record.py`, `artifact_lineage.py`, `maintenance_cadence.py`, and `ro_crate.py`.

Experimental and not integrated: `template_prewarm.py`, `async_conduit.py`, `memory_lattice.py`, `restart_protocol.py`, `self_observe.py`.

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

Do not invent decorative `@1`, `@2`, `/v1`, or similar internal counters. Preserve real external/runtime versions when known, including RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01, and CFF 1.2.0.

## Document authority

Read `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` before broad documentation or governance maintenance.

Use `docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md` only when interpreting early Jules task/PR text. It is dated correction evidence, not a current authority layer.

Current authoritative documents may change when current source truth changes. Historical snapshots remain point-in-time evidence and must not be silently rewritten into current contracts.

Historical files include:

```text
docs/03-maintenance-and-audit/history/FOUR_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/FIVE_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/SIX_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/STAGE_2026_08_MAINTENANCE.md
docs/03-maintenance-and-audit/history/FRONTIER_ALIGNMENT.md
docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md
```

```text
historical snapshot != current contract
current contract != permission to rewrite history
historical agent PR narrative != current contract
```

## Recovery orders

Do not collapse maintenance-control recovery and subject-specific semantic authority.

### Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / current machine-readable maintenance or capability configuration
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

### Subject-specific behavior / scientific semantics

```text
current implementation
> current machine-readable capability contract / schema / configuration for the subject
> active subject-specific contract
> executable/operational evidence for supported use
> current explanatory documentation
> maintenance evidence
> historical snapshots / superseded plans / PR-task narratives
```

A maintenance record may be the latest maintenance observation without outranking implementation for a scientific or runtime claim.

## Maintenance task identity

Record, when applicable:

```text
repository
+ owning surface / task
+ logical period or evidence window
+ producer / maintainer
+ exact base revision
+ run identity when available
```

Before any write, inspect open PRs and live branches for the same owning surface and logical period.

```text
overlap -> COORDINATE
no confirmed defect -> NO_CHANGE_REQUIRED
confirmed drift -> REPAIR
unsafe or unrecoverable evidence/access -> BLOCKED
```

Do not create repository objects to test write access. **Write never probes.**

## Hard rules

1. Structural Markdown changes go through the typed AST rather than regex mutation.
2. Keep SHA-256 on document/artifact identity surfaces and do not reintroduce MD5.
3. External converters use argument lists and must not introduce `shell=True`.
4. Optional dependencies and unavailable states stay explicit.
5. Normalized Markdown is not byte-preserving round-trip fidelity.
6. Structural diff is not merge or conflict resolution.
7. Near-miss/readability values are heuristics, not semantic truth.
8. Process disclosure is declarative and human review is not peer review.
9. The canonical path does not perform AI-text detection.
10. `artifact-record` is project-owned and is not RO-Crate/PROV/Run Crate conformance.
11. Artifact records do not embed complete document payloads by default.
12. Local files may be hashed while URI/opaque refs remain offline references unless a separate resolver exists.
13. Assertion basis records how a value entered the record and never upgrades it to truth.
14. Coverage remains dimensional and must not become a synthetic research-quality score.
15. Coverage ratio must never be relabelled probability, evidence sufficiency, or source credibility.
16. Artifact-lineage relations are caller-declared and must not be inferred from filenames, timestamps, prose similarity, Git history, or model output.
17. `supersedes` never authorizes deletion or rewrite of predecessor history.
18. `revision-of` does not establish semantic equivalence and `uses` does not establish evidence sufficiency.
19. Artifact-lineage references never inherit scientific validity or reproducibility.
20. Metadata generation never self-awards R3 reproduction.
21. Standards-facing RO-Crate JSON-LD must not be polluted with invented project vocabulary.
22. Experimental modules remain Experimental until intentionally integrated.
23. Unknown provider/model/version/source/review state remains unknown and must never be guessed.
24. Calendar/month/stage status must come from actual date/configuration, not agent assumption.
25. A worked maintenance demonstration must never be presented as a clean runtime result unless the scanner was actually executed and the output is preserved.
26. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture as routine maintenance.
27. Jules/Codex/other agent task text, PR bodies, generated summaries, and completion claims are proposal/delivery metadata, not automatic repository authority.
28. Historical `tests passed`, `100%`, `fully aligned`, `fixed`, or similar claims require current re-verification before reuse as current facts.
29. Correct historical agent overstatement forward in current records; do not silently edit or reinterpret old PR history as if the correction were contemporaneous.
30. Path relocation does not change semantic status; update current path consumers without rewriting historical bodies.
31. Checker source/configuration inspection is not checker execution.
32. An unrun check is `NOT_EXECUTED`; unobserved scheduler/workflow execution is `EXECUTION_NOT_OBSERVED` when material.
33. A Draft PR is a review boundary, not proof of test, CI, scientific, or merge success.
34. No confirmed maintenance defect means no activity-only branch or PR.

## Artifact-record invariants

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

`auto-doc-engine/artifact-record` may index source/derivative byte identities, selected metadata identity, declared sources/authors, process disclosure, bounded frontmatter validation, lineage/config refs, execution context, assertion basis, dimensional audit coverage, and a local reproducibility state. It does not inherit external scientific authority.

## Artifact-lineage invariants

Allowed caller-declared relations remain:

```text
derived-from
revision-of
supersedes
uses
related-to
```

```text
lineage != truth
reference != inherited validity
supersedes != history deletion
revision != semantic equivalence
uses != evidence sufficiency
lineage coverage != provenance soundness
```

If artifact records or lineage records are packaged into RO-Crate, keep them as normal project files and do not relabel them as standard RO-Crate profiles.

## Maintenance cadence

The active maintenance system is jointly owned by:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
core/maintenance_cadence.py
```

The first five define control/routing/configuration; `core/maintenance_cadence.py` implements the deterministic local scanner. Historical Jules correction and closed-stage records remain evidence inputs, not current contracts.

Local scanner:

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

A clean scanner result is only configured structural maintenance evidence.

```text
scanner source present != scanner executed
scanner executed != scientific validation
reference demonstration != runtime proof
maintenance clean != scientific validity
weekly consistency != proof of correctness
calendar-month close != reproduction
history inventory != deprecation decision
agent narrative != current verification
```

Daily maintenance starts from current `main`, corrects demonstrated drift only, preserves historical snapshots, and permits `NO_CHANGE_REQUIRED` without a branch/PR when no repair exists.

Weekly maintenance reconciles implementation, Manifest, active contracts, README/Architecture, operator guidance, examples, document status, maintenance config/records, checker ownership, and cross-repository profile names.

Monthly/phase-close maintenance derives calendar/phase state from the actual date, inventories history non-destructively, and never converts calendar closure into scientific reproduction.

If Daily and Weekly own the same real correction, one branch and one final Draft PR should carry it whenever practical.

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
| maintenance cadence / agent provenance | `core/maintenance_cadence.py`, `maintenance/cadence.yaml` | Maintenance Cadence + Document Status + maintenance README + Independent GPT router + Agent Guide + current dated maintenance record; synchronize Manifest only for real capability/profile-semantic or machine-path changes |
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

These are optional references/handoffs, not direct imports or inherited scientific validity.

## Delivery boundary

For a confirmed maintenance repair:

1. branch from the exact observed current `main`;
2. synchronize only owning control surfaces and true dependencies;
3. inspect the aggregate branch diff;
4. refresh current-main/open-PR overlap;
5. record executed and unexecuted checks separately;
6. open one bounded **Draft PR**;
7. stop for maintainer review.

Do not auto-merge, force-push, or write maintenance repairs directly to `main`. Final doctrine and merge authority remains with the maintainer.
