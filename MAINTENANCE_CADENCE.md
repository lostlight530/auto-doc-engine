# Maintenance Cadence — auto-doc-engine

**Status:** active maintenance contract  
**Calibrated:** 2026-09-06  
**Current closed stage:** 2026-08-24 through 2026-08-31

This document defines repository maintenance across daily, weekly, and monthly or explicit phase-close horizons.

The cadence is a maintenance contract, not a scheduler, scientific validator, or GitHub merge gate.

## Authority recovery before every pass

Recover repository truth before proposing work:

```text
current main implementation
> MANIFEST.yaml and current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active specialized contracts
> this cadence contract / maintenance configuration
> Architecture / README
> historical consolidation snapshots
> historical PR / task narratives
```

`JULES_CORRECTION_RECORD.md` defines the specific authority boundary for historical Jules-created PR/task narratives.

An agent task description, PR body, generated summary, or historical test/completeness claim is not a substitute for current repository inspection.

## Cadence model

```text
daily
  local drift / new facts / bounded corrections
        ↓
weekly
  cross-day reconciliation / document authority / trend review
        ↓
monthly or explicit phase-close
  calendar baseline / complete document inventory / deprecation review
```

## Daily

Daily work is intentionally narrow.

Required behavior:

- start from current `main`;
- inspect current authoritative files listed in `DOCUMENT_STATUS.md`;
- inspect the latest dated repair/current maintenance record before older snapshots or PR narratives;
- correct source-grounded code, contract, profile, or documentation drift;
- incorporate external research only when it changes a real architecture decision;
- preserve historical consolidation snapshots and historical PR text;
- keep unknown provider/model/version/source/review values unknown;
- preserve stable project-owned profile identifiers without decorative versions;
- keep unsupported composite research-quality scores absent or null;
- treat Jules/Codex/other coding-agent PR/task prose as proposal/delivery metadata unless current repository evidence independently supports the claim;
- create at most one final maintenance PR for the repository.

Daily work must not:

- rewrite historical snapshots because terminology changed later;
- rewrite historical agent PR/task narratives to make later corrections look contemporaneous;
- introduce a new abstraction solely to manufacture daily activity;
- infer artifact lineage from filenames, timestamps, prose similarity, Git history, or model output;
- promote historical `tests passed`, `complete`, `fully aligned`, or similar agent claims into current verification without re-checking the current revision;
- add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge gates.

## Weekly

Weekly maintenance includes daily checks plus whole-current-document reconciliation.

Required behavior:

- reconcile implementation, Manifest, active contracts, README/Architecture, Agent Guide, Contributor Guide, examples, Frontier Alignment, and current maintenance/correction records;
- reconcile `DOCUMENT_STATUS.md` with files actually present;
- verify stable project profile names remain unversioned;
- inspect the previous seven days of maintenance/correction history and historical consolidation snapshots without rewriting them;
- inspect cross-repository handoff names for drift;
- review frontier calibration freshness;
- review whether any agent-generated PR/task narrative is being treated as current authority without current evidence;
- produce deterministic SHA-256 baselines for configured canonical files when the local scanner is used.

### Daily + Weekly coalescing

If a Daily maintenance pass is also the Weekly settlement/reconciliation pass, use one branch and one final PR for the real combined work whenever practical.

```text
one real correction
!= two required PRs because two cadence labels exist
```

The Daily and Weekly scopes must both be documented, but duplicate changes or cosmetic second PRs must not be manufactured.

## Monthly / explicit phase-close

Monthly maintenance is the strongest maintenance horizon while remaining non-destructive.

Required behavior:

- determine temporal status from the actual date rather than assuming month close;
- record `month-to-date` before the final calendar day and `calendar-month-close` on the final day;
- inventory historical consolidation and stage snapshots;
- hash configured canonical files;
- reconcile current authoritative documents listed in `DOCUMENT_STATUS.md`;
- review current / experimental / proposed / not-integrated labels;
- identify stale or superseded documents as manual review candidates only;
- record whether an explicit research phase is active or closed.

For the closed August stage:

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

On and after 2026-09-01 the August stage remains closed; post-stage repair and later maintenance do not reopen it.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of 2026-09-06 --output output/maintenance-2026-09-06.json
```

### 2026-09-01 portability and scope repair

The scanner enforces the scope it claims:

- configured repository paths must be relative to the repository root;
- `..`, absolute paths, and symlink resolutions outside the root fail closed as error findings;
- historical inventory paths are emitted repository-relative rather than as machine-local absolute paths;
- repo-local configuration is emitted as a relative path and its exact bytes are bound by `configuration_file_sha256`;
- an external configuration, if explicitly supplied, is identified as external without embedding the machine's full absolute path;
- duplicate configured paths are surfaced as warnings rather than silently double-counted;
- the report declares `scan_scope_outside_repository_permitted: false` and `absolute_repository_root_embedded: false`.

The previous wording that the scanner “does not modify repository files” was too broad because `--output` can intentionally write a report file. The precise boundary remains:

```text
inspected_files_mutated: false
report_output_write_requested: true | false
report_output_inside_repository: true | false | null
```

The scanner does not rewrite inspected source, configuration, contracts, history, or evidence artifacts. It may write only the report path explicitly requested by the caller.

## Scanner checks

The scanner reports:

- configured canonical-path presence;
- invalid or escaping configured paths;
- forbidden governance-path presence;
- decorative project-owned profile versions;
- Manifest calibration age;
- configuration SHA-256 identity;
- optional canonical SHA-256 baseline;
- optional repository-relative historical snapshot inventory;
- calendar-month status;
- configured research-stage status.

It does not:

- mutate inspected files or history;
- delete or rewrite historical material;
- call GitHub;
- dereference remote references;
- run tests;
- validate scientific truth;
- certify standards conformance;
- validate historical Jules PR/task claims.

A clean maintenance report means only that configured structural maintenance checks found no error-level finding.

## First complete Daily / Weekly / Monthly demonstration

The first complete worked three-horizon example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

It is a worked reference, not a fabricated clean scanner log.

The current Daily/Weekly reconciliation record is:

```text
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
```

It records governance/cadence correction and is not a scanner result or runtime-validation record.

## Document authority

`DOCUMENT_STATUS.md` is the active map of current, historical, example, and maintenance/correction documents.

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` files remain preserved as time-scoped snapshots.

Historical Jules PR/task narratives remain preserved externally in GitHub history and are governed by `JULES_CORRECTION_RECORD.md`.

## External calibration

The cadence design is informed by long-horizon research work on phase structure, persistent/recoverable state, process-level evaluation, and re-openable provenance.

For coding-agent provenance, current Google Jules guidance reinforces a narrow rule: generated code still requires careful review, and agent insight quality should be evaluated rather than inferred from confidence or completion language.

These sources calibrate maintenance design only. They do not validate this repository or establish that daily, weekly, or monthly intervals are scientifically optimal.

## Shared boundaries

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
cadence label != requirement for duplicate PR churn
```
