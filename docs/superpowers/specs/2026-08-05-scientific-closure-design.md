# Auto Doc Engine Scientific Closure Design

Date: 2026-08-05
Status: approved design baseline
Base: `main@b2bd28a3c5cfbe9d4952ecfa8ace56d7bbaed252`

## Objective

Turn the repository into a compact, truthful, reproducible document-engine project without changing the root README, adding a frontend, or introducing agent-owned output directories. Existing public module paths remain compatible.

## Verified starting point

The AST, incremental, rendering, synchronization, watch, memory, cross-reference, and restart modules exist, together with V2 variants and tests. The repository has no GitHub workflow or cloud test evidence. `MANIFEST.yaml` declares `incremental/diff_tracker.yaml`, but that path is runtime state and is absent from the tracked tree. The former `submit.sh` was an unused one-line placeholder and must not be restored as an empty compatibility artifact.

## Architecture decision

The engine keeps its current library-first structure. A small canonical contract layer will identify the supported AST, diff, render, and synchronization interfaces while preserving legacy imports. Runtime state is isolated from source and written atomically. Capability declarations distinguish implemented, optional, and experimental behavior; declared paths must either exist as source assets or be explicitly marked as generated runtime paths.

The data flow is:

`source -> parser -> typed AST -> structural diff -> renderer -> optional sync target -> provenance result`

Each stage returns a structured result or raises a typed error. No stage silently changes the current working directory, executes through a shell, or reports success after a partial write.

## Planned change set

- Correct `MANIFEST.yaml` so tracker state is declared as generated runtime state rather than a missing repository asset.
- Add a canonical contracts/facade module without deleting the existing V1 or V2 modules.
- Make tracker, index, restart, and observation writes atomic and deterministic; corrupted state fails with a diagnostic rather than being silently accepted.
- Add a real verification entry point under `scripts/`; do not recreate the deleted placeholder `submit.sh`.
- Add repository-contract tests for every manifest path, supported format, runtime boundary, and public facade.
- Add negative tests for malformed AST input, corrupt tracker state, unavailable optional converters, unsafe sync configuration, and interrupted writes.
- Add a reproducibility statement, evidence baseline, AI-use disclosure, security policy, contribution rules, and repo-specific GitHub templates.
- Add least-privilege GitHub verification, CodeQL, and dependency-maintenance workflows with actions pinned to immutable commits.

## Security and failure model

External conversion commands use argument arrays and allowlisted executables only. Input and output paths are resolved before use and may not escape the caller-selected roots. Runtime files are never committed by default. Temporary files are written beside their final target and atomically replaced. Optional dependencies produce an explicit unsupported result; they never fabricate an output.

## Verification and acceptance

Cloud checks run on Python 3.12 and 3.14. Acceptance requires the complete existing suite plus new contract, failure-path, and determinism tests to pass; `compileall` must succeed; generated state must remain untracked; manifest references must validate; action permissions and pinning must pass repository-contract tests. A repeated run on identical input must produce identical semantic output and provenance hashes except for fields explicitly designated as wall-clock observations.

## Non-goals

No root README edit, frontend work, package publication, Jules integration, speculative site generator, network-backed data source, or replacement of stable module paths. Optional Pandoc behavior remains optional.

## Rollout and rollback

Implementation is isolated on `codex/scientific-closure-20260805` and delivered through one repository-specific pull request. The PR is merged only after its own cloud checks pass. Rollback is a single merge-commit revert; runtime-state migrations are versioned and retain read compatibility for existing tracker files.
