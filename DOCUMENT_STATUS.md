# Document Status — auto-doc-engine

**Status:** active document-governance map  
**Calibrated:** 2026-08-31  
**Stage:** August 2026 research-infrastructure phase closed on 2026-08-31

This file classifies repository documentation by authority and historical role

A document being present in the repository does not mean it is the current normative contract

## Current authoritative documents

These files describe the current repository state and should be reconciled during weekly/monthly maintenance

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
STAGE_2026_08_MAINTENANCE.md
MANIFEST.yaml
AGENTS.md
CONTRIBUTING.md
FRONTIER_ALIGNMENT.md
DOCUMENT_STATUS.md
maintenance/cadence.yaml
```

Authority is still scoped by subject

- implementation decides what code actually does
- `MANIFEST.yaml` is the machine-readable repository capability map
- `RESEARCH_CONTRACT.md` defines active scientific-integrity semantics
- specialized contracts define their named surfaces
- `MAINTENANCE_CADENCE.md` defines repository-maintenance horizons
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline
- `DOCUMENT_STATUS.md` defines documentation authority/history roles

## Historical snapshots

These files are intentionally preserved as records of earlier repository state

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

They are **not** current architecture contracts

Do not rewrite them merely because later terminology or capabilities changed

A factual correction may be made only when the historical file itself contains a demonstrable factual error, and the correction should preserve the original time context

```text
historical snapshot != current contract
superseded terminology != permission to rewrite history
```

## Examples

```text
examples/README.md
examples/README_zh.md
examples/artifact_lineage.md
```

Examples demonstrate supported use but do not override implementation, Manifest, or active contracts

## External / citation metadata

```text
CITATION.cff
```

Real external format/standard versions remain valid provenance metadata and are not subject to the project's no-decorative-version rule

Examples include CFF 1.2.0, RO-Crate 1.3, and SARIF 2.1.0 + Approved Errata 01 where used by the repository

## Stage-close status

The represented maintenance stage is now

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
```

The 2026-08-30 `month-to-date` statement was correct at the time and is historical context, not the current 2026-08-31 status

## Maintenance rule

Daily maintenance may update current authoritative files when source truth changes

Weekly maintenance reconciles current authoritative files against each other and inventories historical snapshots

Monthly or explicit phase-close maintenance records a closed baseline and reviews document status without automatically deleting or rewriting historical records

## Hard boundaries

```text
document current != scientific truth
document historical != invalid
document inventory != deprecation decision
maintenance clean != scientific validity
calendar close != independent reproduction
```
