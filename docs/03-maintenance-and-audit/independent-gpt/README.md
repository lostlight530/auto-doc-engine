# Independent GPT Governance — Lineage Beacon

Status: current public recovery kernel  
Calibration: 2026-09-17  
Scope: repository-local recovery, independent audit, reconciliation, bounded repair, and coordinated research-infrastructure maintenance

This directory is the public cold-start handoff for a memoryless independent maintainer. It is a Class 03 maintenance/audit router, not a new semantic authority layer. Current repository implementation and subject-specific contracts remain authoritative for the behavior they own.

## Coordinated research-infrastructure context

This repository participates in the coordinated set:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Coordination may share an inspection window, vocabulary review, or handoff audit. It does not merge authority or permit one repository to overwrite another repository's truth.

## Cold-start recovery

Before planning or writing, recover:

- current date and intended evidence window;
- default branch and exact current merged `main` SHA;
- relevant open pull requests and live maintenance branches;
- recent merged changes that may own the same surface;
- current implementation and machine-readable contracts;
- latest relevant dated repair/current maintenance record;
- current document-status and maintenance contracts;
- checks actually executed, separately from checks merely available.

For **maintenance-control recovery**, use:

```text
current merged main implementation
> MANIFEST.yaml / machine-readable maintenance or capability configuration for the subject
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical FOUR_DAY / FIVE_DAY / SIX_DAY and other point-in-time snapshots
```

For a scientific/capability claim inside a named subsystem, continue to use the most specific implementation/machine/subject contract for that claim. A maintenance record does not outrank implementation merely because it is newer.

## Maintenance task identity

A maintenance attempt is not identified by branch name alone. Record, when applicable:

```text
repository
+ owning surface / task
+ logical period or evidence window
+ producer / maintainer
+ exact base revision
+ run identity when one exists
```

Before creating a branch or writing files, inspect current open PRs and live branches for the same owning surface and logical period. If another live change already owns the same work, return `COORDINATE` rather than creating a parallel repair.

A branch, PR, or file must never be created merely to test whether write access exists. **Write never probes.**

## Repository map

1. `core/`, `templates/`, `sync/`, `tests/`, and current implementation determine actual behavior.
2. Root `MANIFEST.yaml` and machine-readable configuration define only their named capability/configuration surfaces.
3. `docs/02-examples-and-contracts/RESEARCH_CONTRACT.md` and specialized contracts govern named artifact, lineage, process-disclosure, and scientific-integrity semantics.
4. `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` routes document roles; `docs/README.md` defines the three-class taxonomy.
5. `docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, and current maintenance records govern repository maintenance within their declared scope.
6. Dated maintenance records remain time-scoped evidence.
7. Closed-stage consolidations, Jules corrections, and superseded plans under `docs/03-maintenance-and-audit/history/` remain historical evidence.
8. Git history and revision-matched execution evidence resolve disputed path, timing, producer, or execution claims.

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

Real external standard/runtime versions remain factual metadata when genuinely known; stable project-owned identifiers do not erase them.

## Maintenance outcomes

Use these action states when useful:

- `HEALTHY` — inspected surface requires no repair;
- `REPAIR` — confirmed current drift has an owning repair;
- `COORDINATE` — another live owner already overlaps the same work;
- `BLOCKED` — required evidence, permission, or safe recovery is unavailable.

`NO_CHANGE_REQUIRED` is a valid repository result after real inspection. It means no confirmed current defect requires a write; it does not mean inspection was skipped.

If no defect is confirmed, do not create an activity-only branch or PR.

## Execution-evidence discipline

Keep these separate:

```text
checker source present
!= checker executed
checker executed
!= checker passed
checker passed
!= scientific validity
historical pass
!= current pass
```

Unrun checks are `NOT_EXECUTED`. Unobserved scheduler or workflow execution is `EXECUTION_NOT_OBSERVED`. Never reuse a historical `PASS`, `100%`, `complete`, or `fixed` statement as current verification without current evidence.

Preserve negative, failed, missing, blocked, insufficient-evidence, superseded, and unknown states. Do not fabricate scanner, research, test, converter, or agent runs.

## Repair and synchronization

When drift is confirmed:

1. identify the owning implementation/configuration/document;
2. identify every machine contract, router, operator guide, or current explanation that must stay synchronized;
3. make the smallest semantically complete repair;
4. preserve historical bodies unless correcting their own point-in-time fact;
5. verify the aggregate branch diff against the exact base revision;
6. refresh overlap/current-main state before delivery.

A correction changes current interpretation forward. It does not pretend later knowledge existed during an earlier run.

## Delivery contract

For an actual repair:

- use one bounded maintenance branch per repository/owning task whenever practical;
- prefer one combined branch when Daily/Weekly labels describe the same real correction;
- record checks run and checks not run;
- create one **Draft PR** against current `main` after the aggregate diff is verified;
- stop after the Draft PR is reviewable; do not auto-merge, force-push, or write directly to `main`;
- final doctrine and merge authority remains with the maintainer.

A Draft PR is a review boundary, not a claim that tests, CI, scientific validation, or merge approval succeeded.

## Public boundary

This recovery kernel is repository-bounded. It does not publish or reconstruct private Jules prompts, repository memory, hidden reasoning, credentials, or unrelated operator context. Public repository governance may preserve the **effect** of a rule without copying private control text.

## 2026-11-11 scoped independent A1/A2 acceptance clarification

This is a forward interpretation correction for the Nov01–11, 2026 window, not a change to Native production, periodic-audit, or historical original PR evidence. See the [Nov01–11 original PR acceptance ledger](../../../maintenance/frontier-research/annotations/2026-11-11_A1A2_EFFECTIVE_PR_ACCEPTANCE_RECONCILIATION.md).

- Independent A1 reviews the complete applicable MonthStart..N−1 corpus, including a per-file source, evidence and disposition decision; it is not a yesterday-only summary.
- Independent A2 starts only after its original A1 is merged and fresh-read from main, and updates the complete MonthStart..N source/evidence/relationship version, not a Day N note.
- Valid A1/A2 maintenance content includes relevant individual file judgments, source/path/blob SHA custody, evidence-index references, lineage relationships, dated source-status transitions, real contradiction tests, historical state inheritance, qualified NO_FOLLOW_UP and necessary structured coverage matrices.
- Do not mistake 100 meaningful PR additions for 100 unrelated novel scientific findings, 100 independent issuers or 100 invented new observations.
- Keep each original PR's GitHub additions >=100 numeric gate separate from scope completeness, content validity, producer claims, checks actually executed, merge evidence and current-main retention.
- Inspect the final merged original PR head when adjudicating the originally delivered diff; early Draft NOT_MET cannot automatically represent the final amended head.
- The original PRs are immutable historical deliveries: successor, QA, cleanup, audit and this reconciliation never add lines to the original.
- Smaller original PRs retain a truthful NUMERIC_NOT_MET without erasing real maintenance coverage; content-validity PASS cannot be deduced from additions alone.
- Dated source-path reviews, verifiable evidence custody and bounded no-change judgments count as real maintenance when accurate; boilerplate, repeated filler, unsupported execution or fabricated science do not.
- Stage/Native producer states (including BLOCKED/NOT_EXECUTED/UNKNOWN) are not promoted by independent maintenance or GitHub merge.
- D7/D10/D14/D30 are a separate audit plane; no additional periodic audit or native run is implied by this record.
- W45 is closed, W46 is open and November remains open at this evidence cut; do not infer natural month closure.
- In this repository 20 original Nov02–11 independent A1/A2 PRs are merged, 14 with >=100 additions and 6 with numeric NOT_MET, subject to separately evidence-reviewed semantic validity.
