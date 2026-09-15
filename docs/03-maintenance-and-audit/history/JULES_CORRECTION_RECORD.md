# Jules Correction Record — auto-doc-engine

**Status:** active correction / authority record  
**Calibrated:** 2026-09-06  
**Scope:** historical Jules-created pull-request narratives and their relationship to current repository truth

## Purpose

This record does **not** declare historical Jules work invalid and does not rewrite old pull requests.

It fixes a governance ambiguity: early automated coding-agent PR descriptions contain implementation, test, completeness, and quality claims that are useful historical delivery metadata, but they are not durable current authority by themselves.

```text
agent task / PR narrative != current repository truth
claimed test pass != current runtime verification
historical completion claim != permanent capability guarantee
proposal wording != normative contract
```

## Historical Jules PRs in scope

- PR #1 — `Comprehensive Architecture Overhaul & Bilingual Documentation Upgrade`
- PR #2 — `refactor(incremental): optimize DiffTracker memory algorithm via recursive LCS`
- PR #3 — `chore: align codebase with core memories and security rules`

Each was created automatically by Jules for a user-started Jules task. Their PR bodies are preserved as historical task/delivery narratives.

They may describe real changes that entered repository history, but phrases such as `100% accurate`, `all tests pass`, `robust`, `fully aligned`, or equivalent completion language are **time-scoped assertions** unless current evidence independently re-establishes them.

## Current authority order

When recovering repository truth, use:

```text
current main implementation
> MANIFEST.yaml and current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active specialized contracts
> MAINTENANCE_CADENCE.md and maintenance/cadence.yaml
> Architecture / README
> historical consolidation snapshots
> historical PR / task narratives, including Jules
```

Subject-specific contracts remain authoritative only for their named surface.

## Correction rules

### J-C01 — PR body is not merged state

An unmerged agent PR is a proposal. After merge, the repository fact is the actual resulting tree on `main`, not every statement in the PR body.

### J-C02 — Execution claims expire unless reverified

Historical statements such as test counts, test success, exact runtime behavior, performance, or completeness must be reverified against the current revision before being used as current evidence.

### J-C03 — Agent wording is not normative terminology

Historical phrases such as `core memories`, `enterprise-ready`, `fully aligned`, or broad architecture analogies are not project contracts unless they are present in current authoritative repository documents.

### J-C04 — Correct forward; do not rewrite history

If current implementation or contracts supersede an old agent narrative, preserve the historical PR and record the correction in current documentation or a dated repair/maintenance record.

```text
superseded != fabricated
requires re-verification != false
historical != current
```

## Current auto-doc-engine calibration

The current repository has materially evolved beyond the early Jules PR descriptions. Current authority includes the artifact-record, artifact-lineage, assertion-basis / audit-coverage, process-disclosure, maintenance-cadence, document-authority, and post-stage-repair surfaces now present on `main`.

Therefore early Jules PRs must be read as point-in-time development history, not as a substitute for inspecting current implementation and current contracts.

## External calibration

Google's own Jules guidance states that AI-generated code should still be reviewed carefully before use, even when Jules' critic/review mechanisms are involved. Later Jules work also emphasizes evaluation of useful agent insight rather than treating agent confidence as correctness.

Primary references checked 2026-09-06:

- Google Developers Blog — `Meet Jules’ sharpest critic and most valuable ally` (2025-08-12)
- Google Developers Blog — `Measuring What Matters with Jules` (2026-06-22)

These references calibrate the governance rule only. They do not prove any historical repository change wrong.

## Durable boundary

```text
agent assistance != repository authority
review mechanism != infallibility
PR metadata != runtime proof
current main != historical PR prose
correction record != deletion of history
```
