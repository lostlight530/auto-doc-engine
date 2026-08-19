# auto-doc-engine

> AST-driven document rendering, parsing, diffing, and optional format conversion toolkit.

[简体中文](README_zh.md) | [English](README.md)

---

## Overview

`auto-doc-engine` is currently a set of independently callable Python modules: Jinja2 template rendering, Mistune Markdown AST parsing, structural diffing, and external-command-based format synchronization. The repository has unit tests covering part of these interfaces but does not yet provide an end-to-end validated unified production pipeline.

## Capability Matrix

Status is based on the current cloud source code and tests:

- **Implemented**: Implementation exists with source or test support for stated boundaries.
- **Optional**: Implementation depends on local tools, additional configuration, or uncovered runtime environments.
- **Experimental**: Source exists but is not wired into a validated main chain.
- **Not Integrated**: No corresponding adapter or implementation exists in the current cloud repository.

| Capability | Status | Current Evidence & Boundaries |
|---|---|---|
| [`core/renderer.py`](core/renderer.py) | Implemented | Jinja2 template rendering; `load_data()` currently reads JSON and CSV only. Missing data fields return `MISSING_DATA_FIELD`. |
| [`core/ast_engine.py`](core/ast_engine.py) | Implemented | Maps supported Markdown nodes to internal AST via Mistune, with re-rendering; unmapped nodes raise `UNSUPPORTED_AST_NODE`. |
| [`core/incremental.py`](core/incremental.py) | Implemented | Computes add/modify/delete/unchanged records for AST nodes; tests cover mid-insertion, paragraph modification, and table row insertion. Not equivalent to a guarantee of automatic preservation for arbitrary human edits. |
| [`core/sync.py`](core/sync.py) | Implemented (interface) / Optional (conversion) | Calls external commands via argument lists and returns per-target results; HTML, DOCX, PDF, EPUB depend on Pandoc, PDF also on XeLaTeX. Tests verify command structure only, not full multi-format conversion chains. |
| [`core/cross_ref.py`](core/cross_ref.py) | Implemented | Builds an AST-based heading index and bidirectional cross-document link graph; only Markdown links targeting other indexed `.md` files create references, and unresolved targets are reported by `validate()`. Covered by `tests/test_cross_ref.py`. |
| SQLite data source | Not Integrated | `DataBindingEngine.load_data()` has no SQLite branch. |
| API data source | Not Integrated | No network data source adapter, auth configuration, or corresponding tests. |
| `core/template_prewarm.py`, `core/self_observe.py`, `core/async_conduit.py`, `core/memory_lattice.py`, `core/restart_protocol.py` | Experimental | Files exist but are not wired into a validated canonical entry point. |

The SQLite/API adapters, full multi-format conversion, experimental modules above, and any local V2 reference packages are not part of a single validated cloud pipeline.

## Dependencies & Failure Behavior

| Dependency | Purpose | Behavior When Missing or Failing |
|---|---|---|
| Python 3 | Running modules and tests | Cannot run without an available interpreter. |
| `jinja2` | Template rendering | Import of renderer fails; template errors raised by Jinja2. |
| `mistune` | Markdown AST and HTML fallback | Import of related modules fails; unsupported AST nodes raise explicit errors. |
| `pyyaml` | Sync target config and diff history persistence | Import fails when reading config or writing history. |
| `pandoc` | HTML, DOCX, PDF, EPUB conversion | Target result returns `ERROR: pandoc not installed`; target is not reported as successful. |
| `xelatex` | Pandoc PDF backend | Pandoc subprocess fails; error text written to that target's result. |
| `cp` command | Markdown copy target | Subprocess fails in environments lacking `cp`; should be specifically checked on Windows. |

`DiffTracker.record_generation()` writes YAML runtime records per configuration; `core/sync.py` demo writes to `output/`. These generated artifacts are not tracked source directories in the current repository.

## Quick Verification

Create an isolated environment and install dependencies needed for current tests:

```bash
python -m venv .venv
# Activate .venv per your current shell
python -m pip install jinja2 mistune pyyaml
```

Run README contract and existing tests:

```bash
python -m unittest tests.test_readme_contract -v
python tests/test_all.py
python tests/test_incremental.py
```

Success criteria: all three commands exit with code `0`. Missing dependencies, unavailable external converters, or non-zero returns should be recorded as failures, not counted as success.

The four core files also include standalone demo entry points:

```bash
python core/renderer.py
python core/ast_engine.py
python core/incremental.py
python core/sync.py
```

These commands demonstrate module behavior individually; they do not represent a single unified pipeline from data source to all output formats. The incremental and sync demos may produce local runtime artifacts.

## Known Limitations

- No unified public facade, CLI, or full-chain integration test.
- JSON/CSV loading and template rendering exist, but SQLite/API still require design, implementation, and testing.
- AST accepts only mapped node types; parse-then-render may alter formatting and is not byte-level faithful.
- Diff tracker reports structural differences; safe application of changes, conflict handling, and human edit preservation require upper-layer workflow validation.
- Multi-format results depend on Pandoc, XeLaTeX, `cp`, target configuration, and OS; the repository does not currently prove all targets work in all environments.
- `MANIFEST.yaml` capability declarations and runtime paths still require calibration and should not be used alone as implementation evidence.

## Documentation

- [Architecture (English)](ARCHITECTURE.md)
- [Architecture (Chinese)](ARCHITECTURE_zh.md)
- [Examples](examples/README.md)

## License

MIT License
