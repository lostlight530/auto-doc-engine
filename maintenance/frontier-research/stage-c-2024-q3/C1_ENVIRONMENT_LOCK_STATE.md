# Frontier Research Part C1 — Environment Lock and Resolution State

## Identity

- Stage: `C / 2024-Q3`
- Window: `2024-07-01 through 2024-09-30`
- Reconstructed: `2026-09-22`
- Coverage: `SEARCH_BOUNDED`
- Status: `COMPLETE`

## Research question

When does dependency-resolution state become artifact provenance, and what can a lockfile not establish by itself

## Objects and sources

- O1 uv 0.3 project-management expansion, announced 2024-08-20
- S1 Astral, “uv: Unified Python packaging”, 2024-08-20: https://astral.sh/blog/uv-unified-python-packaging
- S2 uv 0.3.x changelog: https://github.com/astral-sh/uv/blob/main/changelogs/0.3.x.md
- S3 current uv project lockfile documentation, retrospective explanation only: https://docs.astral.sh/uv/concepts/projects/layout/

S1/S2/S3 are one project family

## Observations

Astral announced uv 0.3 as an expansion from pip-compatible workflows into project management, tools, scripts and Python installation

The announcement explicitly introduced `uv run`, `uv lock` and `uv sync`, with cross-platform lockfiles based on project metadata

The 0.3 changelog also records early lockfile corrections such as lockfile cache instability and invalidation behavior for dependency changes

The current uv docs explain a useful conceptual distinction: `pyproject.toml` carries broad project requirements while `uv.lock` carries exact resolved versions for the supported environment space

Current documentation contains later capabilities too, so only the stable lockfile distinction is used retrospectively; later standards such as `pylock.toml` are not back-projected into Q3 2024

## Analysis

Stage B ended with a question about when environment identity becomes necessary artifact provenance

uv 0.3 supplies a concrete Q3 answer: once project execution can automatically resolve/sync an environment from a lock state, the lockfile becomes a material input to reproducibility claims

But the correct chain is:

```text
project metadata
→ resolver decision
→ lock state
→ synchronized environment
→ command execution
→ produced artifact
```

A stored lockfile directly evidences resolved dependency intent/state

It does not prove that the environment was actually synchronized, that every external system dependency was captured, that the command ran, or that the scientific result reproduced

## Counterevidence / limits

- current uv docs are mutable and contain post-2024 features
- no uv environment was recreated in this Stage
- no cross-platform lock equivalence test was executed
- no claim is made that uv is the universal packaging solution
- exact OS/library/toolchain state can exceed Python dependency resolution

## Repository relation

`PARALLEL_CONVERGENCE`

The external mechanism reinforces the repository distinction between process disclosure and executed/reproduced evidence

No local implementation defect is established

## Conclusion

`SUPPORTED_OBSERVATION`

A dependency lock becomes important artifact provenance when it materially constrains the environment that generates the artifact, but:

```text
lockfile presence
!= environment recreation executed
!= scientific reproduction
```
