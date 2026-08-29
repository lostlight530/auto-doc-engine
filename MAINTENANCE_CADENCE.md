# Maintenance Cadence — auto-doc-engine

**Status:** active maintenance contract  
**Calibrated:** 2026-08-30

This document defines how repository maintenance is split across daily, weekly, and monthly or explicit phase-close work

The cadence is a repository-maintenance contract, not a scheduler and not a GitHub merge gate

## Why cadence is explicit

Long-horizon research systems benefit from phase-aware review, persistent state, recoverable work segments, and re-openable provenance

The repository therefore separates maintenance horizons instead of letting every maintenance pass rewrite the whole research surface

```text
daily
  local drift / new facts / bounded corrections
        ↓
weekly
  cross-day reconciliation / contract consistency / trend review
        ↓
monthly or explicit phase-close
  canonical baseline / history inventory / deprecation review
```

## Daily

Daily maintenance is intentionally narrow

Required behavior

- start from current `main`
- check current canonical files and stable project identifiers
- correct factual or contract drift that can be demonstrated from current source
- incorporate new external research only when it changes a real architecture decision
- preserve historical consolidation documents
- keep unknown provider/model/version/source/review state unknown
- do not synthesize a research-quality score
- create at most one final maintenance PR for the repository

Daily maintenance must not

- rewrite historical snapshots because wording changed later
- introduce a new abstraction only to create daily activity
- infer artifact lineage from filenames, timestamps, prose similarity, Git history, or model output
- add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge gates

## Weekly

Weekly maintenance includes the daily checks plus cross-day reconciliation

Required behavior

- reconcile code, Manifest, active contracts, Agent Guide, and Frontier Alignment
- verify stable project profile names remain unversioned
- review the previous seven days of consolidation snapshots without rewriting them
- inspect cross-repository handoff names for drift
- review frontier calibration freshness and remove only claims that are no longer supported
- produce deterministic baseline hashes for canonical files when the local scanner is used
- distinguish current canonical state from historical snapshots

Weekly maintenance asks

```text
Did a daily change create a contract mismatch
Did one document retain a deprecated profile name
Did a cross-repository handoff name drift
Did an external calibration source change an actual engineering decision
Did a temporary phase note accidentally become a permanent capability claim
```

## Monthly / explicit phase-close

Monthly maintenance is the strongest review horizon but still does not rewrite history automatically

Required behavior

- build a month-to-date or explicitly declared phase-close baseline
- inventory historical consolidation and stage snapshots
- hash canonical files for a reproducible maintenance baseline
- review deprecated/current/experimental capability labels
- identify stale or superseded documentation as **manual review candidates** only
- reconcile current architecture against the full month of merged changes
- state explicitly whether the month is closed or only month-to-date

Hard rule

```text
monthly review != automatic deletion
phase close != history rewrite
superseded document != invalid historical evidence
```

On 2026-08-30 the August record is **month-to-date**, not a completed calendar-month close

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-30
```

Optional output

```bash
python core/maintenance_cadence.py weekly --output maintenance/weekly-report.json
```

The scanner checks

- configured canonical paths
- forbidden GitHub-governance paths
- decorative project-owned profile versions
- Manifest calibration age
- optional canonical SHA-256 baseline
- optional historical snapshot inventory

It does not

- modify files
- delete historical material
- call GitHub
- dereference remote references
- run tests
- verify scientific truth
- certify standards conformance

A clean maintenance report means only that the configured local structural checks found no error-level maintenance finding

## History rule

Historical phase documents are append-only evidence of earlier repository state unless an explicit factual correction is required

Current contracts may supersede old semantics without erasing the old record

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## External calibration

Current cadence design is informed by

- long-horizon autonomous research work showing phase structure and the value of regime-aware re-validation
- ScienceFlow-style segmentation and recovery for long-horizon research
- provenance work emphasizing complete re-openable records that can be audited and corrected
- current research-software guidance treating software as a living research object rather than static data

These are design calibration signals only

They do not validate this repository or establish an optimal maintenance frequency

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != proof of correctness
monthly baseline != independent reproduction
history inventory != deprecation decision
hash != semantic equivalence
coverage != quality
provenance != truth
```
