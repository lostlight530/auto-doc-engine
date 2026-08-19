# auto-doc-engine

> AST-driven document rendering, parsing, diffing, and optional format conversion toolkit.

[简体中文](README_zh.md) | [English](README.md)

---

## Overview

`auto-doc-engine` is currently a set of independently callable Python modules: Jinja2 template rendering, Mistune Markdown AST parsing, structural diffing, cross-document reference indexing with classified broken-link diagnostics, a `doctor` health-check command, frontmatter schema validation, readability metrics, and external-command-based format synchronization. The repository has unit tests covering part of these interfaces but does not yet provide an end-to-end validated unified production pipeline.

## Capability Matrix

Status is based on the current cloud source code and tests:

- **Implemented**: Implementation exists with source or test support for stated boundaries.
- **Optional**: Implementation depends on local tools, additional configuration, or uncovered runtime environments.
- **Experimental**: Source exists but is not wired into a validated main chain.
- **Not Integrated**: No corresponding adapter or implementation exists in the current cloud repository.

| Capability | Status | Current Evidence & Boundaries |
|---|---|---|
| [`core/renderer.py`](core/renderer.py) | Implemented | Jinja2 template rendering with `table` and `bullet_list` filters; `load_data()` currently reads JSON and CSV only. Missing data fields return `MISSING_DATA_FIELD`. |
| [`core/ast_engine.py`](core/ast_engine.py) | Implemented | Maps supported Markdown nodes to internal AST via Mistune, with re-rendering; unmapped nodes raise `UNSUPPORTED_AST_NODE`. |
| [`core/incremental.py`](core/incremental.py) | Implemented | Computes add/modify/delete/unchanged records for AST nodes; tests cover mid-insertion, paragraph modification, and table row insertion. Not equivalent to a guarantee of automatic preservation for arbitrary human edits. |
| [`core/sync.py`](core/sync.py) | Implemented (interface) / Optional (conversion) | Calls external commands via argument lists and returns per-target results; HTML, DOCX, PDF, EPUB depend on Pandoc, PDF also on XeLaTeX. Tests verify command structure only, not full multi-format conversion chains. |
| [`core/cross_ref.py`](core/cross_ref.py) | Implemented | Builds an AST-based heading index and bidirectional cross-document link graph; only Markdown links targeting other indexed `.md` files create references. Beyond plain `validate()`, `diagnose()` classifies every broken link as `near_miss` (with "did you mean" suggestions from `difflib`, including frontmatter aliases) or `dangling`, and `recurring_targets()` reports missing targets referenced by ≥ 2 documents as a backlog. Covered by `tests/test_cross_ref.py` and `tests/test_diagnostics.py`. |
| [`core/doctor.py`](core/doctor.py) | Implemented | `python core/doctor.py <docs_dir>` audits a document set: orphan documents (no inbound links), classified broken links, reference cycles, frontmatter schema issues, readability metrics, and graph node/edge counts. Exit code is non-zero on error-level findings (CI gate), or on warnings too with `--strict`. Covered by `tests/test_doctor.py`. |
| [`core/frontmatter.py`](core/frontmatter.py) | Implemented | Parses optional YAML frontmatter with pyyaml and validates it against a hand-written schema (`title` / `aliases` / `status` / `updated` / `tags`); unknown fields warn, type and enum violations are errors. `aliases` feed near-miss link suggestions. Covered by `tests/test_frontmatter.py`. |
| [`core/readability.py`](core/readability.py) | Implemented | Stdlib-only readability metrics: Coleman-Liau grade and average sentence length for Latin text, average characters per sentence for CJK text; fenced code is excluded. Report-mode only (warnings, never a gate by itself); consumed by `doctor`. Covered by `tests/test_readability.py`. |
| Executable documentation examples | Implemented | `tests/test_doc_examples.py` parses the README/ARCHITECTURE files through the mistune AST layer and executes every `python`-fenced block, so documented examples cannot silently rot. |
| SQLite data source | Not Integrated | `DataBindingEngine.load_data()` has no SQLite branch. |
| API data source | Not Integrated | No network data source adapter, auth configuration, or corresponding tests. |
| `core/template_prewarm.py`, `core/self_observe.py`, `core/async_conduit.py`, `core/memory_lattice.py`, `core/restart_protocol.py` | Experimental | Files exist but are not wired into a validated canonical entry point. |

The SQLite/API adapters, full multi-format conversion, experimental modules above, and any local V2 reference packages are not part of a single validated cloud pipeline.

## Dependencies & Failure Behavior

| Dependency | Purpose | Behavior When Missing or Failing |
|---|---|---|
| Python 3 | Running modules and tests | Cannot run without an available interpreter. |
| `jinja2` | Template rendering | Import of renderer fails; template errors raised by Jinja2. |
| `mistune` | Markdown AST and HTML fallback | Import of related modules fails; unsupported AST nodes raise explicit errors. **Recommended: mistune ≥ 3.2.1** (includes escaping/injection and ReDoS fixes); the AST exit point is uniformly `renderer='ast'`. |
| `pyyaml` | Sync target config, diff history persistence, frontmatter parsing | Import fails when reading config, writing history, or validating frontmatter. |
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
python -m unittest tests.test_cross_ref -v
python -m unittest tests.test_diagnostics -v
python -m unittest tests.test_frontmatter -v
python -m unittest tests.test_doctor -v
python -m unittest tests.test_readability -v
python -m unittest tests.test_doc_examples -v
```

Success criteria: all commands above exit with code `0` (`make test` runs the same set). Missing dependencies, unavailable external converters, or non-zero returns should be recorded as failures, not counted as success.

The five core modules also include standalone demo entry points:

```bash
python core/renderer.py
python core/ast_engine.py
python core/incremental.py
python core/sync.py
python core/cross_ref.py
python core/frontmatter.py
python core/readability.py
```

These commands demonstrate module behavior individually; they do not represent a single unified pipeline from data source to all output formats. The incremental and sync demos may produce local runtime artifacts.

## Documentation Health Checks (doctor)

Audit any directory of Markdown documents — the command exits non-zero when broken links or frontmatter schema errors are found, so CI can gate on it:

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --strict   # also fail on warnings (orphans, cycles, readability)
python core/doctor.py path/to/docs --json     # machine-readable report
```

The same audit is available as a library call:

```python
import tempfile
from pathlib import Path
from core.doctor import run_doctor

with tempfile.TemporaryDirectory() as tmp:
    docs = Path(tmp)
    (docs / "a.md").write_text("# A\n\nSee [B](b.md).\n", encoding="utf-8")
    (docs / "b.md").write_text("# B\n\nBack to [A](a.md).\n", encoding="utf-8")
    report = run_doctor(tmp)
    assert report.doc_count == 2
    assert report.link_diagnostics == []
    assert report.exit_code() == 0
```

Broken links are classified instead of merely listed: a `near_miss` carries "did you mean" suggestions (existing documents and declared frontmatter `aliases`), a `dangling` target is a planned document, and any dangling target referenced by ≥ 2 documents is reported as a recurring backlog item:

```python
import tempfile
from pathlib import Path
from core.cross_ref import EntanglementIndex

with tempfile.TemporaryDirectory() as tmp:
    docs = Path(tmp)
    (docs / "getting-started.md").write_text("# Getting Started\n", encoding="utf-8")
    (docs / "a.md").write_text(
        "# A\n\nSee [guide](gettng-started.md) and the [plan](plan.md).\n",
        encoding="utf-8",
    )
    index = EntanglementIndex(index_path=str(docs / "index.json"))
    index.build(tmp)
    kinds = {d.target: d.kind for d in index.diagnose()}
    assert kinds["gettng-started.md"] == "near_miss"   # suggestion: getting-started.md
    assert kinds["plan.md"] == "dangling"              # planned document
```

## Current Repository Map

```text
auto-doc-engine/
├── README.md / README_zh.md
├── ARCHITECTURE.md / ARCHITECTURE_zh.md
├── CITATION.cff
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── sync.py
│   ├── cross_ref.py
│   ├── doctor.py
│   ├── frontmatter.py
│   ├── readability.py
│   └── other experimental modules
├── templates/jinja2/
├── sync/targets.yaml
└── tests/
    ├── test_all.py
    ├── test_cross_ref.py
    ├── test_diagnostics.py
    ├── test_doctor.py
    ├── test_doc_examples.py
    ├── test_frontmatter.py
    ├── test_incremental.py
    ├── test_readability.py
    └── test_readme_contract.py
```

## Known Limitations

- No unified public facade, CLI, or full-chain integration test (`doctor` is a per-document-set audit CLI, not a pipeline facade).
- JSON/CSV loading and template rendering exist, but SQLite/API still require design, implementation, and testing.
- AST accepts only mapped node types; parse-then-render may alter formatting and is not byte-level faithful.
- Diff tracker reports structural differences; safe application of changes, conflict handling, and human edit preservation require upper-layer workflow validation.
- Multi-format results depend on Pandoc, XeLaTeX, `cp`, target configuration, and OS; the repository does not currently prove all targets work in all environments.
- Readability metrics and near-miss suggestions are heuristics with documented thresholds, not guarantees of writing quality or link intent.
- `MANIFEST.yaml` is a declarative manifest aligned with the capability matrix; it is not, by itself, implementation evidence.

## Documentation

- [Architecture (English)](ARCHITECTURE.md)
- [Architecture (Chinese)](ARCHITECTURE_zh.md)
- [Examples](examples/README.md)

## License

MIT License
