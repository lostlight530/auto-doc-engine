# Maintenance Cadence — auto-doc-engine

**Status:** active maintenance contract  
**Calibrated:** 2026-09-17  
**Current closed stage:** 2026-08-24 through 2026-08-31

This document defines repository maintenance across Daily, Weekly, and Monthly or explicit phase-close horizons. The cadence is a maintenance contract, not a scheduler, scientific validator, CI system, or GitHub merge gate.

## 1. Recover repository truth first

Before planning work, recover the exact current repository state. Maintenance-control recovery uses:

```text
current merged main implementation
> MANIFEST.yaml / current machine-readable configuration for the subject
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> maintenance/cadence.yaml and this cadence contract
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

For scientific/capability semantics inside a named subsystem, the most specific implementation, machine contract, and active subject contract still own that claim. A newer maintenance record does not override implementation merely because of date.

Do not use an agent task description, PR body, handoff, generated summary, or remembered narrative as a substitute for inspecting current `main`.

## 2. Maintenance identity and idempotency

For each pass record, when applicable:

```text
repository
owning surface / task
logical period or evidence window
producer / maintainer
exact base revision
run identity when available
```

Before creating a branch or writing files, inspect open PRs and live branches for the same owning surface and logical period.

```text
overlapping live owner -> COORDINATE
no confirmed defect -> NO_CHANGE_REQUIRED
confirmed current drift -> REPAIR
required evidence or safe access unavailable -> BLOCKED
```

`NO_CHANGE_REQUIRED` follows real inspection. It must not be used as a synonym for skipped inspection.

Do not create a branch, file, commit, issue, or PR merely to prove write access. **Write never probes.**

## 3. Cadence model

```text
daily
  local drift / new facts / bounded corrections
        ↓
weekly
  cross-day reconciliation / document authority / trend review
        ↓
monthly or explicit phase-close
  calendar baseline / complete current-document inventory / deprecation review
```

Cadence labels do not require duplicate work. If one real correction satisfies Daily and Weekly scope, one branch and one final Draft PR should carry that work whenever practical.

## 4. Daily

Daily work is narrow and evidence-driven.

Required behavior:

- start from current merged `main`;
- inspect current authoritative files routed by `DOCUMENT_STATUS.md`;
- inspect the latest relevant dated repair/current maintenance record before older snapshots when relevant;
- correct demonstrated source, contract, profile, configuration, or documentation drift;
- preserve historical consolidation snapshots and historical PR/task prose;
- keep unknown provider/model/version/source/review values unknown;
- preserve stable project-owned profile identifiers without decorative versions;
- treat coding-agent task/PR prose as proposal or delivery metadata unless current repository evidence independently supports the claim;
- record checks actually executed separately from checks merely available;
- create at most one bounded final Draft PR when a real repair exists.

Daily work must not:

- manufacture an edit solely to satisfy cadence;
- rewrite historical snapshots because terminology changed later;
- infer lineage from filenames, timestamps, prose similarity, Git history, or model output;
- reuse historical `PASS`, `complete`, `fully aligned`, `100%`, or `fixed` as current verification without re-checking the current revision;
- add GitHub Actions, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture as routine maintenance.

If inspection confirms no repair, stop with `NO_CHANGE_REQUIRED`; do not create activity-only churn.

## 5. Weekly

Weekly maintenance includes Daily checks plus whole-current-document reconciliation.

Required behavior:

- reconcile current implementation, `MANIFEST.yaml`, active contracts, README/Architecture, `AGENTS.md`, contributor guidance, examples, current maintenance records, and document-status routing;
- reconcile `DOCUMENT_STATUS.md` with the current tree;
- inspect maintenance configuration and checker ownership;
- verify stable project profile names remain unversioned;
- inspect the preceding maintenance/correction window and retained historical consolidations without rewriting them;
- inspect cross-repository handoff names for drift;
- review whether any agent-generated narrative is being treated as current authority without current evidence;
- produce SHA-256 baselines only when the local scanner is actually used.

### Daily + Weekly coalescing

```text
one real correction
!= two required PRs because two cadence labels apply
```

One branch and one final Draft PR may satisfy both scopes when they own the same real repair.

## 6. Monthly / explicit phase-close

Monthly maintenance is the strongest non-destructive maintenance horizon.

Required behavior:

- determine temporal status from the actual date;
- use `month-to-date` before the natural final calendar day and `calendar-month-close` only at natural month close;
- inventory retained historical stage/consolidation material;
- hash configured canonical files only when the scanner actually runs;
- reconcile current authoritative documents;
- review current / experimental / proposed / not-integrated labels;
- identify stale or superseded documents as manual review candidates only;
- record whether an explicit research phase is active or closed;
- never convert a calendar close into a reproduction or scientific-validity claim.

The August 2026 research-infrastructure phase remains closed after 2026-08-31. September maintenance does not reopen it.

## 7. Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of YYYY-MM-DD --output output/maintenance-YYYY-MM-DD.json
```

The scanner enforces repository-local path scope, configuration identity, canonical-path presence, profile/version boundaries, Manifest calibration age, optional SHA-256 baselines, optional history inventory, calendar status, and configured stage status.

The scanner does **not**:

- mutate inspected source/configuration/history files;
- call GitHub;
- inspect open PR ownership;
- run tests or converters;
- validate scientific truth;
- certify standards conformance;
- validate historical Jules task/PR claims;
- prove that a scheduled maintenance pass actually occurred.

`--output` may write only the caller-requested report file. That write is distinct from mutation of inspected source/configuration/history.

A clean maintenance report means only that the configured structural maintenance checks found no error-level finding.

## 8. Execution evidence

Keep these states separate:

```text
checker source present != checker executed
checker executed != checker passed
checker passed != scientific validity
historical pass != current pass
workflow definition != workflow execution
```

If a relevant check was not run, record `NOT_EXECUTED`. If scheduler/workflow execution was not observed, use `EXECUTION_NOT_OBSERVED` where that distinction matters.

Inspection of checker source or configuration is **contract inspection**, not execution evidence.

## 9. Current and dated maintenance evidence

Current active control surfaces are:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
AGENTS.md
```

Dated records such as the 2026-08-31 demonstration, 2026-09-01 repair, 2026-09-06 reconciliation, and 2026-09-13 month-to-date reconciliation remain point-in-time maintenance evidence. They are not silently rewritten into current scanner results or capability truth.

`MANIFEST.yaml` capability/frontier calibration changes only when a real capability/profile/architecture transition justifies it. Maintenance freshness alone does not authorize a capability calibration bump.

## 10. History and correction discipline

Preserve FOUR_DAY, FIVE_DAY, SIX_DAY, closed-stage, frontier-alignment, Jules-correction, and superseded design records as historical evidence.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
path relocation != semantic change
```

Correct forward through a current owning file or a later dated reconciliation. Do not rewrite old bodies merely to make the historical record look cleaner.

## 11. Delivery contract

When a repair is confirmed:

1. branch from the exact observed current `main`;
2. modify only the owning surfaces and required synchronized control files;
3. inspect the aggregate `main...branch` diff;
4. refresh current-main and open-PR overlap before delivery;
5. record checks run and checks not run;
6. open one bounded **Draft PR**;
7. stop for maintainer review.

Do not auto-merge, force-push, or write maintenance repairs directly to `main`.

A Draft PR is a review boundary, not proof of CI/test/scientific success.

## 12. Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != proof of correctness
calendar-month close != independent reproduction
history inventory != deprecation decision
hash != semantic equivalence
coverage != quality
provenance != truth
report written != repository validated
agent task / PR narrative != current repository truth
claimed test pass != current runtime verification
cadence label != duplicate PR requirement
maintenance calibration != machine capability transition
contract inspection != checker execution
```
