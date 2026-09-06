# Document Status — auto-doc-engine

**Status:** active document-governance map  
**Calibrated:** 2026-09-06  
**Stage:** August 2026 research-infrastructure phase closed on 2026-08-31

This file classifies repository documentation by authority and historical role.

A document being present in the repository does not mean it is the current normative contract.

## Current authoritative documents

These files describe the current repository state and should be reconciled during weekly/monthly maintenance:

```text
README.md
README_zh.md
ARCHITECTURE.md
ARCHITECTURE_zh.md
RESEARCH_CONTRACT.md
ARTIFACT_RECORD.md
ARTIFACT_LINEAGE_CONTRACT.md
ASSERTION_BASIS_AND_COVERAGE.md
PROCESS_DISCLOSURE.md
MAINTENANCE_CADENCE.md
JULES_CORRECTION_RECORD.md
STAGE_2026_08_MAINTENANCE.md
POST_STAGE_REPAIR_2026_09_01.md
MANIFEST.yaml
AGENTS.md
CONTRIBUTING.md
FRONTIER_ALIGNMENT.md
DOCUMENT_STATUS.md
maintenance/cadence.yaml
```

Authority remains scoped by subject:

- implementation decides what code actually does;
- `MANIFEST.yaml` is the machine-readable repository capability map;
- `RESEARCH_CONTRACT.md` defines active scientific-integrity semantics;
- specialized contracts define their named surfaces;
- `MAINTENANCE_CADENCE.md` defines repository-maintenance horizons;
- `JULES_CORRECTION_RECORD.md` defines how historical Jules PR/task narratives may and may not be used as current evidence;
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline;
- `POST_STAGE_REPAIR_2026_09_01.md` records post-close implementation hardening without reopening the stage;
- `DOCUMENT_STATUS.md` defines documentation authority/history roles.

## Authority precedence for recovery

```text
current main implementation
> MANIFEST.yaml / current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active specialized contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> Architecture / README
> historical snapshots
> historical PR/task narratives
```

This precedence is a recovery rule, not a claim that every higher layer overrides every subject-specific contract.

## Historical snapshots

These files are intentionally preserved as records of earlier repository state:

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

They are **not** current architecture contracts.

Do not rewrite them merely because later terminology or capabilities changed.

A factual correction may be made only when the historical file itself contains a demonstrable factual error, and the correction should preserve the original time context.

```text
historical snapshot != current contract
superseded terminology != permission to rewrite history
```

## Dated maintenance / correction / research-calibration records

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
```

- the first complete cadence demonstration is a worked historical/reference example, not a captured clean scanner log;
- the 2026-09-01 repair records post-stage implementation hardening;
- the 2026-09-06 Daily/Weekly record documents a real governance reconciliation and cadence correction, not a scanner/runtime-validation result;
- the 2026-09-01 through 2026-09-06 frontier refresh is **post-stage, non-normative, source-bounded research calibration** for the artifact/document-evidence layer. It updates external frontier context without changing runtime capability, the active Research Contract, or the closed August stage.

`FRONTIER_ALIGNMENT.md` remains the August stage-close positioning snapshot. The dated frontier refresh is the newer external-research observation record through 2026-09-06 and must not be misread as a normative capability contract.

Dated records are evidence of what a maintenance/research pass concluded at that date. They do not override current implementation if later main changes.

## Historical coding-agent / PR narratives

Early Jules-created PRs remain preserved in GitHub history.

Their task descriptions, PR bodies, automatic summaries, test claims, and completion language are not current contracts. Read `JULES_CORRECTION_RECORD.md` before reusing them as evidence.

```text
historical agent proposal != current authority
claimed execution success != current re-verification
correction != history deletion
```

## Examples and reference demonstrations

```text
examples/README.md
examples/README_zh.md
examples/artifact_lineage.md
```

Examples demonstrate supported use but do not override implementation, Manifest, or active contracts.

## External / citation metadata

```text
CITATION.cff
```

Real external format/standard versions remain valid provenance metadata and are not subject to the project's no-decorative-version rule.

Examples include CFF 1.2.0, RO-Crate 1.3, and SARIF 2.1.0 + Approved Errata 01 where used by the repository.

## Stage-close and post-stage status

The represented maintenance stage is:

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
```

The 2026-09-01 repair, 2026-09-06 maintenance reconciliation, and 2026-09-01 through 2026-09-06 frontier refresh do not extend or reopen that window.

## Maintenance rule

Daily maintenance may update current authoritative files when source truth changes.

Weekly maintenance reconciles current authoritative files against each other, checks current agent/PR authority handling, and inventories historical snapshots without rewriting them.

If one pass serves as both Daily and Weekly maintenance, one branch/PR may carry the combined real work; cadence labels do not require duplicate PR churn.

Monthly or explicit phase-close maintenance records a closed baseline and reviews document status without automatically deleting or rewriting historical records.

## Hard boundaries

```text
document current != scientific truth
document historical != invalid
document inventory != deprecation decision
post-stage repair != stage rewrite
frontier calibration != runtime capability
external event != contract drift by default
maintenance clean != scientific validity
reference demonstration != runtime proof
calendar close != independent reproduction
agent PR narrative != current repository truth
cadence coalescing != skipped maintenance scope
```
