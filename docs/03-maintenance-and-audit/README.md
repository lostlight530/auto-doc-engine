# 03 — Maintenance and Audit

This class answers: **what maintenance/governance rule applied, what was inspected at a given time, what was concluded, who owned the maintenance surface, and what historical evidence must remain reviewable?**

It does **not** define scientific or runtime semantics merely because a maintenance record is newer than an active implementation or subject contract.

## Current maintenance / governance surfaces

- [`DOCUMENT_STATUS.md`](DOCUMENT_STATUS.md) — current document-governance router and authority classifier
- [`MAINTENANCE_CADENCE.md`](MAINTENANCE_CADENCE.md) — active human-readable repository-maintenance contract
- root `maintenance/cadence.yaml` — machine-readable local maintenance/scanner configuration and maintenance-control identity rules
- [`independent-gpt/README.md`](independent-gpt/README.md) — public cold-start recovery/delivery kernel for a memoryless independent maintainer
- root `AGENTS.md` — operational agent guidance
- root `CONTRIBUTING.md` plus `.github/pull_request_template.md` and `.github/ISSUE_TEMPLATE/governance.md` — public collaboration/delivery entry points

`core/maintenance_cadence.py` remains **Class 01 executable source**. Its presence, source review, or configuration review is not equivalent to an executed scan.

## Coordinated research-infrastructure context

This repository participates in a coordinated set with:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Coordination permits shared inspection windows and cross-repository checks for profile names, contract names, and handoff vocabulary. It does not create cross-repository authority. Each repository recovers from its own current `main` and native contracts.

## Maintenance-control recovery

For maintenance ownership and delivery, recover in this order:

```text
current merged main implementation
> MANIFEST.yaml / current machine-readable configuration
> latest relevant dated repair or current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

For a scientific/capability claim, continue to use the most specific implementation and active machine/subject contract. The two questions are related but not interchangeable.

## Idempotent maintenance ownership

A maintenance attempt should retain, when applicable:

```text
repository + owning surface/task + logical period/evidence window
+ producer/maintainer + exact base revision + run identity when available
```

Before writing, inspect open PRs and live branches for an overlapping owner. Overlap means `COORDINATE`, not a parallel repair.

Periodic maintenance is an inspection opportunity, not a requirement to manufacture changes. `NO_CHANGE_REQUIRED` is valid after real inspection; in that case do not create an activity-only branch or PR.

**Write never probes.** Do not create repository objects merely to test permissions.

## Dated maintenance / calibration evidence

Point-in-time records include:

- root `maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md`
- root `maintenance/POST_STAGE_REPAIR_2026_09_01.md`
- root `maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md`
- root `maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md`
- root `maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md`

These remain time-scoped evidence. A later dated record may report a newer observation or correction, but it does not silently override implementation, machine contracts, or active scientific/specialized contracts.

The August 2026 research stage remains closed historical evidence. September stays month-to-date until natural month close.

## Stage / historical evidence

- [`history/STAGE_2026_08_MAINTENANCE.md`](history/STAGE_2026_08_MAINTENANCE.md)
- [`history/FRONTIER_ALIGNMENT.md`](history/FRONTIER_ALIGNMENT.md)
- [`history/FOUR_DAY_CONSOLIDATION.md`](history/FOUR_DAY_CONSOLIDATION.md)
- [`history/FIVE_DAY_CONSOLIDATION.md`](history/FIVE_DAY_CONSOLIDATION.md)
- [`history/SIX_DAY_CONSOLIDATION.md`](history/SIX_DAY_CONSOLIDATION.md)
- [`history/JULES_CORRECTION_RECORD.md`](history/JULES_CORRECTION_RECORD.md) — retained at its dated correction boundary, not current top-level authority
- `history/superpowers/` — superseded/historical design and planning evidence

Historical records remain reviewable at their original time boundary. Physical relocation or later terminology does not rewrite their claims.

## Validation and delivery boundary

Keep these separate:

```text
checker available != checker executed
checker executed != checker passed
checker passed != scientific validity
historical pass != current pass
contract inspection != runtime verification
Draft PR != merge approval or validation success
```

Record an unrun check as `NOT_EXECUTED`; use `EXECUTION_NOT_OBSERVED` when execution itself was not observed.

When a real repair exists, verify the aggregate branch diff, refresh current-main/overlap state, open one bounded **Draft PR**, and stop for maintainer review. Do not auto-merge or write maintenance repairs directly to `main`.

## Interpretation rules

```text
maintenance record != current implementation semantics
latest date != highest semantic authority
file presence != runtime evidence
later success != earlier success
correction != history rewrite
historical snapshot != invalid evidence
NO_CHANGE_REQUIRED != missing inspection
maintenance freshness != capability transition
```

When current state conflicts with a dated record, preserve the dated record and correct forward in current governance or a later reconciliation record.
