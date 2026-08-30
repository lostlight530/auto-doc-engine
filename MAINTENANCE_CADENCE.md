# Maintenance Cadence — auto-doc-engine

**Status:** active maintenance contract  
**Calibrated:** 2026-08-31  
**Current closed stage:** 2026-08-24 through 2026-08-31

This document defines repository maintenance across daily, weekly, and monthly or explicit phase-close horizons

The cadence is a maintenance contract, not a scheduler, scientific validator, or GitHub merge gate

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

Daily work is intentionally narrow

Required behavior

- start from current `main`
- inspect current authoritative files listed in `DOCUMENT_STATUS.md`
- correct source-grounded code, contract, profile, or documentation drift
- incorporate external research only when it changes a real architecture decision
- preserve historical consolidation snapshots
- keep unknown provider/model/version/source/review values unknown
- preserve stable project-owned profile identifiers without decorative versions
- keep unsupported composite research-quality scores absent or null
- create at most one final maintenance PR for the repository

Daily work must not

- rewrite historical snapshots because terminology changed later
- introduce a new abstraction solely to manufacture daily activity
- infer artifact lineage from filenames, timestamps, prose similarity, Git history, or model output
- add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge gates

## Weekly

Weekly maintenance includes daily checks plus whole-current-document reconciliation

Required behavior

- reconcile implementation, Manifest, active contracts, README/Architecture, Agent Guide, Contributor Guide, examples, and Frontier Alignment
- reconcile `DOCUMENT_STATUS.md` with files actually present
- verify stable project profile names remain unversioned
- inspect the previous seven days of historical consolidation snapshots without rewriting them
- inspect cross-repository handoff names for drift
- review frontier calibration freshness
- produce deterministic SHA-256 baselines for configured canonical files when the local scanner is used

Weekly questions

```text
Did a daily change create code/document contract drift
Did one current document retain a superseded profile name
Did a historical snapshot get treated as current authority
Did a cross-repository handoff name drift
Did external calibration become an unsupported capability claim
```

## Monthly / explicit phase-close

Monthly maintenance is the strongest maintenance horizon while remaining non-destructive

Required behavior

- determine temporal status from the actual date rather than assuming month close
- record `month-to-date` before the final calendar day and `calendar-month-close` on the final day
- inventory all historical consolidation and stage snapshots
- hash configured canonical files
- reconcile all current authoritative documents listed in `DOCUMENT_STATUS.md`
- review current / experimental / proposed / not-integrated labels
- identify stale or superseded documents as manual review candidates only
- reconcile the complete month of merged changes against current architecture
- record whether an explicit research phase is active or closed

For the current stage

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

Hard rules

```text
monthly review != automatic deletion
calendar close != history rewrite
phase close != scientific validation
superseded document != invalid historical evidence
```

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report

```bash
python core/maintenance_cadence.py monthly --as-of 2026-08-31 --output maintenance/august-close.json
```

The scanner reports

- configured canonical-path presence
- forbidden governance-path presence
- decorative project-owned profile versions
- Manifest calibration age
- optional canonical SHA-256 baseline
- optional historical snapshot inventory
- calendar-month status
- configured research-stage status

It does not

- modify repository files
- delete or rewrite historical material
- call GitHub
- dereference remote references
- run tests
- validate scientific truth
- certify standards conformance

A clean maintenance report means only that configured structural maintenance checks found no error-level finding

## First complete Daily / Weekly / Monthly demonstration

The first complete worked three-horizon example is

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

Read order for a new maintainer or agent

```text
MAINTENANCE_CADENCE.md
        ↓ normative horizon semantics
DOCUMENT_STATUS.md
        ↓ current vs historical authority
STAGE_2026_08_MAINTENANCE.md
        ↓ current closed stage
FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
        ↓ worked commands and interpretation
```

The dated demonstration is intentionally **not** a pre-asserted clean scanner log
It does not fabricate findings or SHA-256 values that require actual execution

```text
reference demonstration != runtime proof
worked example != scientific evidence
```

## Document authority

`DOCUMENT_STATUS.md` is the active map of current, historical, example, and external-metadata documents

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` files remain preserved as time-scoped snapshots

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## External calibration

The cadence design is informed by long-horizon research work on phase structure, persistent/recoverable state, process-level evaluation, and re-openable provenance

Current adjacent signals include ScienceFlow-style segmented recovery, long-horizon studies showing workflow-induced phases, and evaluation work showing that final scores alone do not expose where progress, regression, or misleading experience reuse occurs

These sources calibrate maintenance design only

They do not establish that daily, weekly, or monthly intervals are scientifically optimal

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != proof of correctness
calendar-month close != independent reproduction
history inventory != deprecation decision
hash != semantic equivalence
coverage != quality
provenance != truth
```
