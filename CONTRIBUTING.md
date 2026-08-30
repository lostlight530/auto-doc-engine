# Contributing to auto-doc-engine

Contributions should make the document/artifact evidence architecture more truthful, portable, inspectable, or maintainable

Module count and automation volume are not goals by themselves

## Before changing the repository

Read

```text
README.md
ARCHITECTURE.md
RESEARCH_CONTRACT.md
DOCUMENT_STATUS.md
MAINTENANCE_CADENCE.md
MANIFEST.yaml
AGENTS.md
```

Use `DOCUMENT_STATUS.md` to distinguish current authority from historical snapshots before editing broad documentation

## Development principles

- Structural Markdown behavior goes through `core/ast_engine.py`
- Document/artifact identity surfaces use SHA-256
- External tools use argument lists; do not introduce `shell=True`
- Built-in operations prefer portable stdlib behavior; Pandoc/PDF engines remain optional
- Structural diff is not merge or conflict resolution
- Doctor/SARIF findings establish only implemented predicates
- New frontmatter fields need explicit type and semantics
- AI/human-review fields are declarations, not authorship adjudication, AI-text detection, or peer review
- `auto-doc-engine/artifact-record` is project-owned, not RO-Crate/PROV/Run Crate conformance
- `auto-doc-engine/artifact-lineage` is typed declared lineage, not semantic equivalence, history deletion, or inherited validity
- `auto-doc-engine/ro-crate` is the project exporter identity; RO-Crate 1.3 is the external standard target
- Artifact records stay payload-minimal; local files may be hashed while URI/opaque refs are not automatically fetched
- Assertion basis describes how a field entered the record and must not be described as correctness verification
- Audit coverage remains dimensional; do not create an unsupported aggregate research-quality score
- Coverage ratios must not be relabelled probabilities, credibility scores, or evidence-sufficiency scores
- Metadata/checksums/packages/maintenance baselines never self-award R3 reproduction
- Experimental modules remain Experimental until intentionally integrated
- Unknown provider/model/version/source/review state remains unknown; never guess
- Historical `FOUR_DAY`, `FIVE_DAY`, and `SIX_DAY` consolidation files remain historical unless a factual correction to their original time context is required

## Stable project identifiers

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
auto-doc-engine/maintenance-cadence
auto-doc-engine/maintenance-report
autoDocFinding
```

Do not append decorative `@1/@2` or `/v1` suffixes

Real external standard/runtime versions remain legitimate evidence when actually known

## Evidence-field rule

When adding a new artifact or lineage field, ask separately

```text
What is the value
What is its assertion/observation basis
Can this repository actually observe that basis
Is presence/coverage distinct from correctness
Can any scientific authority accidentally be inherited through this field
```

If an answer requires external scientific adjudication, provenance soundness, source credibility, AI-content detection, or peer review, do not pretend the current repository implements it

## Artifact-lineage rule

Allowed relations remain bounded

```text
derived-from
revision-of
supersedes
uses
related-to
```

Do not infer these from filenames, timestamps, prose similarity, Git history, or model output

Every lineage relation must preserve non-inheritance of scientific validity and reproduction status

## Daily / weekly / monthly maintenance

Maintenance is defined in `MAINTENANCE_CADENCE.md` and `maintenance/cadence.yaml`

Current stage/document status is defined in `STAGE_2026_08_MAINTENANCE.md` and `DOCUMENT_STATUS.md`

```text
daily -> bounded demonstrated drift
weekly -> full current-document / contract reconciliation
monthly -> calendar-month or explicit phase-close baseline
```

For the closed August stage

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

Maintenance reports are structural evidence only

```text
maintenance clean != scientific validity
calendar close != reproduction
history inventory != deprecation decision
```

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/claim-transfer
  -> epistemic-pipeline/evidence-envelope
  -> sci-render-kit/figure-claim-audit
  -> sci-render-kit/figure-evidence
  -> sci-render-kit/communication-transfer
```

Do not silently strengthen imported semantics

```text
heuristic score -> probability      # prohibited without calibration evidence
bounds -> confidence interval       # prohibited without declared semantics
reviewed -> peer reviewed           # prohibited
source ref -> trusted source        # prohibited
coverage ratio -> quality score     # prohibited
revision-of -> semantic equivalence # prohibited
```

## Repository governance boundary

Local/manual checks may be used when useful

Do not add GitHub Actions, CI/CodeQL workflows, dependency bots, branch-protection assumptions, or merge-gate architecture as routine maintenance

Test execution is not scientific-validation evidence and is not a default completion gate for this repository-maintenance workflow

## License

Contributions are licensed under the MIT License
