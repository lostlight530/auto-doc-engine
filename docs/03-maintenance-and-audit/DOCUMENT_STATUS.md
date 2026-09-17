# Document Status — auto-doc-engine

**Status:** active document-governance router  
**Calibrated:** 2026-09-17  
**Stage:** August 2026 research-infrastructure phase closed on 2026-08-31

This file routes repository materials by current role and authority. It is a classifier/router, not an independent source of runtime or scientific truth.

See `docs/README.md` for the three-class taxonomy.

## Class 01 — source and explanation

Primary implementation and explanatory surfaces include:

```text
core/
templates/
sync/
tests/
Makefile
README.md
README_zh.md
docs/01-source-and-explanation/ARCHITECTURE.md
docs/01-source-and-explanation/ARCHITECTURE_zh.md
```

Implementation determines actual behavior. README/Architecture explain current behavior and must follow implemented and contracted boundaries.

`core/maintenance_cadence.py` is executable source in this class. Scanner source presence is not scanner execution.

## Class 02 — examples and contracts

Current capability/usage constraints include:

```text
MANIFEST.yaml
docs/02-examples-and-contracts/RESEARCH_CONTRACT.md
docs/02-examples-and-contracts/ARTIFACT_RECORD.md
docs/02-examples-and-contracts/ARTIFACT_LINEAGE_CONTRACT.md
docs/02-examples-and-contracts/ASSERTION_BASIS_AND_COVERAGE.md
docs/02-examples-and-contracts/PROCESS_DISCLOSURE.md
sync/targets.yaml
examples/
AGENTS.md
CONTRIBUTING.md
CITATION.cff
LICENSE
```

`MANIFEST.yaml` is the machine-readable capability map. The Research Contract and specialized contracts define their named scientific/integrity surfaces. Examples and operator guidance demonstrate supported use but do not create capabilities absent from implementation or active contracts.

## Class 03 — maintenance and audit

Current maintenance/governance surfaces:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/governance.md
```

The Independent GPT file is a public cold-start recovery router inside Class 03. It does not create a fourth document class and does not outrank implementation, machine contracts, or active subject-specific contracts.

Dated maintenance records remain point-in-time evidence, including:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
maintenance/POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md
```

Closed-stage / historical evidence includes:

```text
docs/03-maintenance-and-audit/history/STAGE_2026_08_MAINTENANCE.md
docs/03-maintenance-and-audit/history/FRONTIER_ALIGNMENT.md
docs/03-maintenance-and-audit/history/FOUR_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/FIVE_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/SIX_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md
docs/03-maintenance-and-audit/history/superpowers/
```

The Jules correction record remains a dated correction boundary, not current top-level authority.

## Two authority questions must not be collapsed

### Capability / scientific semantics

For a named implementation or scientific claim:

```text
current implementation
> current machine-readable contract/configuration for the subject
> active subject-specific contract
> executable/operational evidence for the claimed behavior
> current explanatory documentation
> maintenance evidence
> historical records
```

### Maintenance-control recovery

For deciding what a maintenance agent should inspect, own, repair, or deliver:

```text
current merged main implementation
> MANIFEST.yaml / machine-readable maintenance or capability configuration
> latest relevant dated repair or current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

A maintenance record can therefore be the latest maintenance observation without becoming stronger scientific authority than implementation.

## Maintenance task ownership

A maintenance attempt should preserve, where applicable:

```text
repository
+ owning surface/task
+ logical period/evidence window
+ producer/maintainer
+ exact base revision
+ run identity when available
```

Before a write, inspect current open PRs/live branches for overlapping ownership. Same owning surface and period with another live owner means `COORDINATE`, not a parallel repair.

No confirmed defect means `NO_CHANGE_REQUIRED`; do not create activity-only branch/PR churn.

## Dated evidence interpretation

The 2026-08-31 cadence demonstration is a worked historical/reference example, not an automatically preserved clean scanner run.

The 2026-09-01 repair records post-stage hardening without reopening August.

The 2026-09-06 reconciliation records governance/cadence correction.

The 2026-09-13 reconciliation remains valid point-in-time evidence that the pass found `NO_CHANGE_REQUIRED` for implementation/capability semantics, refreshed maintenance observation through 2026-09-13, kept September month-to-date, and did not fabricate absent scanner runs. It does not mechanically advance `MANIFEST.yaml` capability calibration.

```text
maintenance freshness != capability calibration
latest observation != highest semantic authority
NO_CHANGE_REQUIRED != skipped inspection
```

## Execution evidence boundary

```text
implementation presence != execution evidence
scanner source != scanner execution
checker definition != checker execution
contract inspection != checker PASS
historical PASS != current PASS
```

Unrun checks are `NOT_EXECUTED`. Unobserved scheduler/workflow execution is `EXECUTION_NOT_OBSERVED` when material.

## Historical preservation

Historical files remain reviewable at their original time boundary. Do not rewrite their bodies merely because current terminology, paths, or behavior changed.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
agent completion claim != current verification
path relocation != semantic change
```

Correct forward in a current owning file or later dated reconciliation.

## Stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
September 2026: month-to-date until natural month close
```

Post-stage repairs, reconciliations, taxonomy work, and frontier refreshes do not reopen August.

## Hard boundaries

```text
document current != scientific truth
maintenance clean != scientific validity
artifact lineage != inherited validity
frontier calibration != runtime capability
reference demonstration != runtime proof
calendar close != independent reproduction
historical agent narrative != current repository truth
classification != deletion authority
Draft PR != validation success
```
