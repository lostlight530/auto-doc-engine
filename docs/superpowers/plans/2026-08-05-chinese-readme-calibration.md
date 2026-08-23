# Auto Doc Engine Chinese README Calibration Plan — Historical Record

**Original date:** 2026-08-05  
**Status:** **COMPLETED / SUPERSEDED by the 2026-08-23 full repository refresh**

This file is retained to explain the earlier correction of unsupported Chinese README claims. It is not an active task list and must not be re-executed by an automated maintainer.

## Historical goal

The original goal was to replace unsupported capability claims with an evidence-bounded description of the cloud repository. That principle remains valid.

The original scope, however, was intentionally narrow: README calibration plus a local truth-contract check. The repository has since advanced beyond that scope.

## 2026-08-23 current baseline

The current authority files are:

```text
README.md
README_zh.md
ARCHITECTURE.md
ARCHITECTURE_zh.md
RESEARCH_CONTRACT.md
MANIFEST.yaml
AGENTS.md
```

Current implementation includes JSON/CSV/YAML binding, a broader typed AST subset, structural change reporting, document graph diagnostics, bounded research frontmatter, SARIF interchange, cross-platform synchronization, and an implemented RO-Crate 1.3 core metadata writer.

## Superseded instructions

The following instructions from the historical plan are no longer active repository policy:

- restricting maintenance to the Chinese README and one test;
- implementing on the old `codex/scientific-closure-20260805` branch;
- requiring cloud/PR checks before merge;
- treating a local test report as a completion gate.

Current rule: local checks may be used manually when useful, but GitHub-native CI/merge gating is outside this repository's research architecture.

## Durable evidence rule

The historical README correction established a rule that remains active:

- source files and wired behavior determine capability;
- optional external tools stay optional;
- Experimental modules stay Experimental until explicitly integrated;
- local/unmerged reference material is not repository implementation evidence;
- docs and MANIFEST must follow the actual code boundary.

## Archive note

Do not use the checkbox workflow from the original plan. For current maintenance, follow `AGENTS.md` and `RESEARCH_CONTRACT.md`.
