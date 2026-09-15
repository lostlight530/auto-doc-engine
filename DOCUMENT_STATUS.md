# Document Status — auto-doc-engine

**Status:** active document-governance router  
**Calibrated:** 2026-09-15  
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
ARCHITECTURE.md
ARCHITECTURE_zh.md
```

Implementation determines actual behavior. README/Architecture explain current behavior and must follow implemented and contracted boundaries.

`core/maintenance_cadence.py` is executable source in this class. It is not itself a preserved scanner run or an external governance audit.

## Class 02 — examples and contracts

Current capability/usage constraints include:

```text
MANIFEST.yaml
RESEARCH_CONTRACT.md
ARTIFACT_RECORD.md
ARTIFACT_LINEAGE_CONTRACT.md
ASSERTION_BASIS_AND_COVERAGE.md
PROCESS_DISCLOSURE.md
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
DOCUMENT_STATUS.md
MAINTENANCE_CADENCE.md
maintenance/cadence.yaml
JULES_CORRECTION_RECORD.md
```

Dated/stage/historical evidence:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
STAGE_2026_08_MAINTENANCE.md
POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md
FRONTIER_ALIGNMENT.md
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
docs/03-maintenance-and-audit/history/superpowers/
```

The archived Superpowers material is superseded historical design/planning evidence. Its relocation does not make it current authority.

## Recovery authority

Use **subject-scoped** authority in this order:

```text
current merged main implementation
> current machine-readable capability contract / schema / configuration for that subject
> active RESEARCH_CONTRACT.md and active specialized contract for that subject
> operational examples / configuration / test evidence for supported use
> README / Architecture / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

Important consequences:

- a newer dated maintenance record does not outrank an active capability/scientific contract merely because its date is later;
- `maintenance/cadence.yaml` is authoritative for its local maintenance/scanner configuration, not for artifact-lineage or scientific-validity semantics;
- `DOCUMENT_STATUS.md` routes documents but does not override implementation or active subject contracts;
- `AGENTS.md` remains operational guidance and its hard rules remain active; if an older embedded recovery-order list conflicts with this 2026-09-15 router, this current router/taxonomy governs document recovery;
- execution evidence exists only when the execution actually occurred and its result was preserved.

## Dated evidence interpretation

The 2026-08-31 cadence demonstration is a worked historical/reference example, not an automatically preserved clean scanner run.

The 2026-09-01 repair records post-stage hardening without reopening the August stage.

The 2026-09-06 reconciliation records governance/cadence correction. The 2026-09-01 through 2026-09-06 frontier refresh is source-bounded post-stage calibration and does not itself change runtime capability or active Research Contract semantics.

The 2026-09-13 reconciliation remains valid point-in-time evidence that the pass found `NO_CHANGE_REQUIRED` for implementation/capability semantics, refreshed maintenance-layer observation through 2026-09-13, kept September month-to-date, and did not fabricate absent scanner runs. It does not mechanically advance `MANIFEST.yaml` capability calibration.

```text
maintenance freshness != capability calibration
latest observation != highest semantic authority
NO_CHANGE_REQUIRED != skipped inspection
```

## Historical preservation

`FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, `SIX_DAY_CONSOLIDATION.md`, closed-stage records, superseded design files, and historical PR/task narratives remain point-in-time evidence.

Do not rewrite them merely because current terminology or behavior changed. Correct forward through a current file, correction, reconciliation, or later time-point record.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
agent completion claim != current verification
```

## Stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
September 2026: month-to-date until natural month close
```

Post-stage repairs, reconciliations, taxonomy work, and frontier refreshes do not reopen the August stage.

## Hard boundaries

```text
document current != scientific truth
implementation presence != execution evidence
scanner source != scanner execution
maintenance clean != scientific validity
artifact lineage != inherited validity
frontier calibration != runtime capability
reference demonstration != runtime proof
calendar close != independent reproduction
historical agent narrative != current repository truth
path relocation != semantic change
classification != deletion authority
```
