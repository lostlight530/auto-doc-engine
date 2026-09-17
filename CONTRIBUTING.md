# Contributing to auto-doc-engine

Contributions should make the document/artifact evidence architecture more truthful, portable, inspectable, or maintainable. Module count and automation volume are not goals by themselves.

## Before changing the repository

Read the current owning surfaces first:

```text
README.md
docs/01-source-and-explanation/ARCHITECTURE.md
docs/02-examples-and-contracts/RESEARCH_CONTRACT.md
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/independent-gpt/README.md
MANIFEST.yaml
AGENTS.md
```

For maintenance work, start from exact current merged `main`, inspect open PRs/live branches for overlapping ownership, and identify the owning surface before writing.

A maintenance task should retain, when applicable:

```text
repository + owning surface/task + logical period/evidence window
+ producer/maintainer + exact base revision + run identity when available
```

Overlap means `COORDINATE`. No confirmed defect means `NO_CHANGE_REQUIRED` and no activity-only branch or PR. Do not create repository objects merely to test permissions: **write never probes**.

## Development principles

- Structural Markdown behavior goes through `core/ast_engine.py`.
- Document/artifact identity surfaces use SHA-256.
- External tools use argument lists; do not introduce `shell=True`.
- Built-in operations prefer portable stdlib behavior; Pandoc/PDF engines remain optional.
- Structural diff is not merge or conflict resolution.
- Doctor/SARIF findings establish only implemented predicates.
- New frontmatter fields need explicit type and semantics.
- AI/human-review fields are declarations, not authorship adjudication, AI-text detection, or peer review.
- `artifact-record` is project-owned, not RO-Crate/PROV/Run Crate conformance.
- `artifact-lineage` is typed declared lineage, not semantic equivalence, history deletion, or inherited validity.
- `auto-doc-engine/ro-crate` is the project exporter identity; RO-Crate 1.3 is the external standard target.
- Artifact records stay payload-minimal; local files may be hashed while URI/opaque refs are not automatically fetched.
- Assertion basis describes how a field entered the record and must not be described as correctness verification.
- Audit coverage remains dimensional; do not create an unsupported aggregate research-quality score.
- Coverage ratios must not be relabelled probabilities, credibility scores, or evidence-sufficiency scores.
- Metadata/checksums/packages/maintenance baselines never self-award R3 reproduction.
- Experimental modules remain Experimental until intentionally integrated.
- Unknown provider/model/version/source/review state remains unknown; never guess.
- Historical FOUR_DAY, FIVE_DAY, SIX_DAY, closed-stage, frontier-alignment, and Jules-correction records remain point-in-time evidence.

## Evidence and lineage rules

When adding an artifact or lineage field, ask separately:

```text
What is the value?
What is its assertion/observation basis?
Can this repository actually observe that basis?
Is presence/coverage distinct from correctness?
Can scientific authority accidentally be inherited through this field?
```

Allowed lineage relations remain:

```text
derived-from
revision-of
supersedes
uses
related-to
```

Do not infer them from filenames, timestamps, prose similarity, Git history, or model output.

```text
heuristic score -> probability      # prohibited without calibration evidence
bounds -> confidence interval       # prohibited without declared semantics
reviewed -> peer reviewed           # prohibited
source ref -> trusted source        # prohibited
coverage ratio -> quality score     # prohibited
revision-of -> semantic equivalence # prohibited
```

## Maintenance workflow

Maintenance is defined by `DOCUMENT_STATUS.md`, `MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `AGENTS.md`, and the Independent GPT recovery kernel.

```text
daily -> bounded demonstrated drift
weekly -> full current-document / contract reconciliation
monthly -> calendar-month or explicit phase-close baseline
```

Cadence is not an obligation to manufacture a change. Daily/Weekly work may coalesce into one real branch/PR when they own the same correction.

Before delivery:

1. verify the aggregate diff against the exact base revision;
2. refresh current `main` and live overlap;
3. list checks actually executed and checks not run;
4. open one bounded **Draft PR**;
5. stop for maintainer review.

Never report an unrun check as passed. Use `NOT_EXECUTED` for an unrun checker/test and `EXECUTION_NOT_OBSERVED` when execution itself was not observed.

```text
maintenance clean != scientific validity
calendar close != reproduction
history inventory != deprecation decision
checker source != checker execution
Draft PR != validation success
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

Do not silently strengthen imported semantics.

## Repository governance boundary

Local/manual checks may be used when useful. Test execution is engineering evidence for the tested surface, not scientific-validation evidence.

Do not add GitHub Actions, CI/CodeQL workflows, dependency bots, branch-protection assumptions, or merge-gate architecture as routine maintenance.

Do not publish private Jules prompts, repository memory, hidden reasoning, credentials, or unrelated operator context. Public repository governance may encode the effect of a rule without copying private control text.

Final review, doctrine, and merge authority remains with the maintainer.

## License

Contributions are licensed under the MIT License.
