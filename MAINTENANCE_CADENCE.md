# Maintenance Cadence — auto-doc-engine

**Status:** active maintenance contract  
**Calibrated:** 2026-09-01  
**Current closed stage:** 2026-08-24 through 2026-08-31

This document defines repository maintenance across daily, weekly, and monthly or explicit phase-close horizons.

The cadence is a maintenance contract, not a scheduler, scientific validator, or GitHub merge gate.

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
- correct source-grounded code, contract, profile, or documentation drift;
- incorporate external research only when it changes a real architecture decision;
- preserve historical consolidation snapshots;
- keep unknown provider/model/version/source/review values unknown;
- preserve stable project-owned profile identifiers without decorative versions;
- keep unsupported composite research-quality scores absent or null;
- create at most one final maintenance PR for the repository.

Daily work must not:

- rewrite historical snapshots because terminology changed later;
- introduce a new abstraction solely to manufacture daily activity;
- infer artifact lineage from filenames, timestamps, prose similarity, Git history, or model output;
- add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge gates.

## Weekly

Weekly maintenance includes daily checks plus whole-current-document reconciliation.

Required behavior:

- reconcile implementation, Manifest, active contracts, README/Architecture, Agent Guide, Contributor Guide, examples, and Frontier Alignment;
- reconcile `DOCUMENT_STATUS.md` with files actually present;
- verify stable project profile names remain unversioned;
- inspect the previous seven days of historical consolidation snapshots without rewriting them;
- inspect cross-repository handoff names for drift;
- review frontier calibration freshness;
- produce deterministic SHA-256 baselines for configured canonical files when the local scanner is used.

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

On 2026-09-01 the August stage remains closed; post-stage repair does not reopen it.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of 2026-09-01 --output output/maintenance-2026-09-01.json
```

### 2026-09-01 portability and scope repair

The scanner now enforces the scope it claims:

- configured repository paths must be relative to the repository root;
- `..`, absolute paths, and symlink resolutions outside the root fail closed as error findings;
- historical inventory paths are emitted repository-relative rather than as machine-local absolute paths;
- repo-local configuration is emitted as a relative path and its exact bytes are bound by `configuration_file_sha256`;
- an external configuration, if explicitly supplied, is identified as external without embedding the machine's full absolute path;
- duplicate configured paths are surfaced as warnings rather than silently double-counted;
- the report declares `scan_scope_outside_repository_permitted: false` and `absolute_repository_root_embedded: false`.

The previous wording that the scanner “does not modify repository files” was too broad because `--output` can intentionally write a report file. The precise boundary is now:

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
- certify standards conformance.

A clean maintenance report means only that configured structural maintenance checks found no error-level finding.

## First complete Daily / Weekly / Monthly demonstration

The first complete worked three-horizon example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

It is a worked reference, not a fabricated clean scanner log.

## Document authority

`DOCUMENT_STATUS.md` is the active map of current, historical, example, and external-metadata documents.

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` files remain preserved as time-scoped snapshots.

## External calibration

The cadence design is informed by long-horizon research work on phase structure, persistent/recoverable state, process-level evaluation, and re-openable provenance. The 2026-09-01 repair also takes seriously the broader scientific-agent lesson that terminal success can hide intermediate structural defects; therefore scanner scope, path identity, and write behavior are recorded explicitly rather than inferred.

These sources calibrate maintenance design only. They do not establish that daily, weekly, or monthly intervals are scientifically optimal.

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
```
