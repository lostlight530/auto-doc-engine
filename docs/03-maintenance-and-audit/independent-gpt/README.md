# Independent GPT Governance — Lineage Beacon

Status: current public recovery kernel
Scope: repository-local recovery, independent audit, reconciliation, bounded repair, and participation in coordinated research-infrastructure review

This directory is the current public handoff point for a memoryless independent reviewer. It is a Class 03 maintenance/audit router, not a new authority layer. Current repository-native implementation and subject-specific contracts remain authoritative for their own subjects.

## Coordinated research-infrastructure context

This repository participates in the coordinated set:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Cross-repository review may compare shared profile names, contract names, handoff vocabulary, and maintenance state. Coordination does not merge authority: each repository must be recovered and judged from its own current `main` and repository truth.

## Recovery order

Start from current repository state and record the revision and evidence window actually examined. Then use the subject-scoped order defined by `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md`:

```text
current merged main implementation
> current machine-readable capability contract / schema / configuration for that subject
> active docs/02-examples-and-contracts/RESEARCH_CONTRACT.md and active specialized contract for that subject
> operational examples / configuration / test evidence for supported use
> README / docs/01-source-and-explanation/ARCHITECTURE.md / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

Older maintenance or correction records remain evidence at their original time boundary and do not override this current subject-scoped order.

## Repository map

1. `core/`, `templates/`, `sync/`, `tests/`, and current implementation determine actual behavior.
2. Root `MANIFEST.yaml` and other machine-readable configuration define capability/configuration only for their named subjects.
3. `docs/02-examples-and-contracts/RESEARCH_CONTRACT.md` and the specialized contracts beside it govern their named artifact, lineage, process-disclosure, and scientific-integrity semantics.
4. `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` routes document roles; `docs/README.md` defines the three-class taxonomy.
5. `docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, and current maintenance records govern maintenance only within their declared scope.
6. `maintenance/POST_STAGE_REPAIR_2026_09_01.md` is a dated post-stage checkpoint.
7. Closed-stage, consolidation, frontier, Jules-correction, and superseded design records under `docs/03-maintenance-and-audit/history/` are historical evidence, not automatic current capability authority.
8. Git history and revision-matched execution evidence resolve disputed path, timing, and execution claims.

## Repository-specific doctrine

Preserve these boundaries:

```text
artifact-lineage relation = caller-declared
artifact lineage != inherited scientific validity
supersedes != history deletion
hash identity != semantic equivalence
assertion basis != correctness
coverage != quality
coverage ratio != probability
R1 != R3
```

Real external standard/runtime versions remain factual metadata when genuinely known; stable internal identifiers do not erase them.

## Maintenance and evidence discipline

Periodic maintenance is an inspection opportunity, not a requirement to manufacture changes. `NO_CHANGE_REQUIRED` is valid when no current defect or drift is demonstrated. Weekly or monthly synthesis requires an actual contract, calendar/phase, evidence, or drift reason.

The 2026-08-24 through 2026-08-31 research stage is closed historical evidence. The 2026-09-01 post-stage repair is the dated starting checkpoint for steady-state maintenance; current merged `main` may supersede it through explicit current evidence or reconciliation.

Execution evidence exists only when execution actually occurred and its result was preserved. Preserve negative, failed, missing, blocked, insufficient-evidence, superseded, and unknown states. Do not fabricate absent scanner, research, or test runs.

## Repair boundary

When drift is confirmed, identify the owning current surface and every machine contract, router, or current explanation that must remain synchronized. Make the smallest truthful change, keep configured paths repository-relative and inside the repository root, preserve configuration identity where required, and do not rewrite historical bodies.

Independent governance may recommend or prepare bounded changes. Delivery mechanics are session- and maintainer-controlled rather than encoded as repository doctrine. Final merge and doctrine authority remains with the maintainer.
