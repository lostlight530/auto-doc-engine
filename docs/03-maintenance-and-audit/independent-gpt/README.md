# Independent GPT Governance — Lineage Beacon

Status: current public recovery kernel
Scope: repository-local recovery, independent audit, reconciliation, and bounded repair

This directory is a public handoff point for a memoryless independent reviewer. It is a Class 03 maintenance/audit router, not a new authority layer. Current repository-native implementation and subject-specific contracts remain authoritative for their own subjects.

## Start from current main

At audit start record the current date, default branch, current `main` SHA, relevant open pull requests, recent merged changes, and checks actually executed.

Then follow the repository’s current subject-scoped recovery order from `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md`:

```text
current merged main implementation
> current machine-readable capability contract / schema / configuration for that subject
> active docs/02-examples-and-contracts/RESEARCH_CONTRACT.md and active specialized contract for that subject
> operational examples / configuration / test evidence for supported use
> README / docs/01-source-and-explanation/ARCHITECTURE.md / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

This file does not override that order.

## Repository map

1. `core/`, `templates/`, `sync/`, `tests/`, and current implementation determine actual behavior.
2. `MANIFEST.yaml` is the machine-readable capability map for its named surface.
3. `docs/02-examples-and-contracts/RESEARCH_CONTRACT.md` and the specialized contracts beside it govern their named scientific / integrity subjects.
4. `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` routes document roles; `docs/README.md` defines the current three-class taxonomy.
5. `docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, and current maintenance records govern maintenance only within their declared scope.
6. Dated stage, consolidation, frontier, Jules-correction, and superseded design records under `docs/03-maintenance-and-audit/history/` are historical evidence, not automatic current capability authority.
7. Git history and revision-matched tests / GitHub Actions evidence resolve disputed execution, path, timing, and provenance claims.

## Evidence boundaries

Maintenance freshness is not capability calibration. Path relocation is not semantic change. Examples do not create capabilities absent from implementation or active contracts. Execution evidence exists only when execution actually occurred and its result was preserved.

Independent governance may inspect lineage, artifact identity, synchronization, public documentation, maintenance records, and current implementation, but it must not promote maintenance prose above current subject contracts.

## History discipline

Historical records remain point-in-time evidence. Later evidence may change current interpretation through a dated correction or reconciliation; it does not rewrite the earlier record. Preserve negative, failed, missing, blocked, superseded, and unknown states. Do not fabricate absent scanner or research runs.

## Independent audit outcome

Separate current facts, historical facts, corrections, external claims, execution evidence, inference, and unknown state. When a concise governance status is useful, use `HEALTHY`, `REPAIR`, `COORDINATE`, or `BLOCKED`.

`HEALTHY` means no repair is required for the audited surface. If repair is justified, change only the owning current file(s) and the contracts or projections that must remain synchronized. Do not create activity-only edits.

## Public boundary and handoff

This kernel is intentionally repository-bounded and does not require reconstruction of unavailable operator context or unrelated orchestration.

A durable audit should leave the next reviewer able to identify the base `main` SHA, scope and evidence window, authority used, checks run, checks not run, current findings, historical findings, corrections, unresolved items, and whether history and negative evidence were preserved.

Independent governance may recommend or prepare bounded changes. Final merge and doctrine authority remains with the maintainer.
