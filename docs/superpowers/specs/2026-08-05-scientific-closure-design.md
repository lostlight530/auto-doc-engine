# Auto Doc Engine Scientific Closure Design

Date: 2026-08-05
Status: approved revised design baseline
Base: `main@b2bd28a3c5cfbe9d4952ecfa8ace56d7bbaed252`

## Objective

Turn the repository into a compact, truthful, reproducible document-engine project. The urgent first correction is the obsolete Chinese README. The larger MIT3 closure will then harden and selectively integrate the local reference work without presenting unreviewed files as cloud implementation.

## Corrected starting point

The cloud `main` tree contains the original AST, incremental, rendering, synchronization, cross-reference, watch, memory, observation, and restart modules, plus `tests/test_all.py` and `tests/test_incremental.py`. It does **not** contain `core/*_v2.py`, `core/declarative_engine.py`, or `tests/test_v2.py`.

Those V2 files and the 95-test report exist only in `D:\Agent-farm\work\mit3-analysis`. They are reference inputs, not verified repository evidence. They must be reviewed for unsafe expression execution, incomplete backend branches, false capability claims, and compatibility before any cloud integration.

The Chinese README currently claims complete API/SQLite binding, complete multi-format delivery, preservation of human edits, immutable provenance, and a tracked `incremental/` directory. These claims exceed or contradict the current cloud tree. The English README is more cautious but remains evidence to cross-check, not authority.

## Immediate README design

Rewrite `README_zh.md` to mirror the calibrated capability states:

- implemented: current renderer, AST parser, incremental diff, and sync modules within their tested contracts;
- optional: environment-dependent converters and data-source integrations;
- experimental: modules not integrated into one canonical chain;
- absent: capabilities present only in the local V2 reference pack.

The README will provide real dependency prerequisites, verification commands, current paths, explicit failure behavior, and links to architecture/examples. It will not claim lossless human-edit preservation, immutable provenance, production readiness, or one-command end-to-end delivery without a corresponding cloud test.

## Scientific closure architecture

Keep the current library-first paths. Introduce a canonical contract/facade only after compatibility tests exist. Runtime tracker and checkpoint state are generated, ignored, versioned, and atomically written. Capability declarations distinguish source assets from generated state and implemented behavior from optional or experimental behavior.

The target flow is:

`source -> validated binding -> typed AST -> structural diff -> renderer -> optional sync target -> provenance result`

Each stage returns a structured result or raises a typed error. No shell execution, arbitrary expression execution, silent fallback, fabricated output, or partial-success claim is permitted.

## Planned larger change set

- Audit the local V2 reference pack file by file; import only behavior that closes a validated requirement.
- Eliminate unsafe expression execution and incomplete placeholder branches before import.
- Correct `MANIFEST.yaml` so runtime tracker state is not represented as a missing tracked asset.
- Add deterministic, atomic state storage and a canonical public contract while retaining compatibility paths.
- Add repository-contract, negative, determinism, corruption, optional-dependency, and interrupted-write tests.
- Add a real verification entry under `scripts/`; do not restore the deleted one-line `submit.sh`.
- Add reproducibility, evidence, AI-use, security, contribution, and repo-specific GitHub governance files.
- Add least-privilege, immutable-SHA-pinned cloud verification, CodeQL, and dependency maintenance.

## Verification and acceptance

Cloud checks run on Python 3.12 and 3.14. Existing tests must remain green before any reference-pack integration. Each imported capability requires its own failing-then-passing contract test. `compileall`, manifest/path validation, generated-state hygiene, dependency failure reporting, and deterministic semantic hashes must pass. A local report is not counted as cloud evidence.

## Non-goals and rollback

No root English README change in this urgent pass, frontend, Jules integration, package publication, network-backed source, or blind V2 bulk upload. Delivery stays on `codex/scientific-closure-20260805`. Each coherent commit and later PR can be independently reverted; no generated runtime state is committed.
