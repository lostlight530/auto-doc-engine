# Agent Guide — auto-doc-engine

Quick-start for an AI agent cloned to work on this repository. Read this
first; it tells you what exists, how to run it, where to change things, and
what is forbidden. For design rationale see `ARCHITECTURE.md`; for the
verified capability status see the capability matrix in `README.md` /
`README_zh.md` and `MANIFEST.yaml` — those are the source of truth.

## 1. What this repository is

An AST-driven document toolkit: a set of independently callable Python
modules (render, parse, diff, cross-reference, health-check, sync). There is
**no unified pipeline facade or end-to-end CLI**. Do not claim one exists.

## 2. Repository map

```text
auto-doc-engine/
├── core/
│   ├── renderer.py        # Jinja2 rendering + JSON/CSV data loading
│   ├── ast_engine.py      # Markdown <-> AST (mistune), NodeType, ASTEngine
│   ├── incremental.py     # DiffTracker: structural diff of two ASTs
│   ├── sync.py            # Multi-target sync via external commands
│   ├── cross_ref.py       # Heading index, link graph, broken-link diagnose()
│   ├── doctor.py          # Document-set health-check CLI (CI gate)
│   ├── frontmatter.py     # YAML frontmatter parse + schema validation
│   ├── readability.py     # Readability metrics (report-mode, never a gate)
│   └── template_prewarm.py, self_observe.py, async_conduit.py,
│       memory_lattice.py, restart_protocol.py   # EXPERIMENTAL, not wired in
├── templates/jinja2/      # Templates loaded by DataBindingEngine
├── sync/targets.yaml      # Sync target selection + pandoc options
├── tests/                 # One file per suite (see §3)
├── examples/              # Runnable walkthroughs (bilingual)
├── MANIFEST.yaml          # Declarative manifest, mirrors capability matrix
└── Makefile               # make test = the full gate
```

## 3. Environment, tests, demos

Setup:

```bash
python -m venv .venv && source .venv/bin/activate
pip install jinja2 "mistune>=3.2.1" pyyaml
# optional external tools: pandoc (html/docx/pdf/epub), xelatex (pdf), cp (markdown target)
```

`make test` runs five suites; all must exit 0:

| Target | Command | Covers |
|---|---|---|
| `test-contract` | `python -m unittest tests.test_readme_contract -v` | README_zh truth-contract |
| `test-all` | `python tests/test_all.py` | renderer / ast_engine / sync |
| `test-incremental` | `python tests/test_incremental.py` | DiffTracker |
| `test-cross-ref` | `python -m unittest tests.test_cross_ref -v` | cross_ref index/graph |
| `test-health` | `python -m unittest tests.test_diagnostics -v` (plus `test_frontmatter`, `test_doctor`, `test_readability`, `test_doc_examples`) | health layer + executable docs |

Every integrated core module is directly runnable as a demo:

```bash
python core/renderer.py    python core/ast_engine.py    python core/incremental.py
python core/sync.py        python core/cross_ref.py     python core/frontmatter.py
python core/readability.py
```

The incremental and sync demos write runtime artifacts (`incremental/`,
`output/`); these are untracked.

The `doctor` command audits any Markdown document set and exits non-zero on
error-level findings (broken links, frontmatter schema errors):

```bash
python core/doctor.py <docs_dir> [--strict] [--json]
```

## 4. Where to change what

| Task | File | Entry point |
|---|---|---|
| New data source (DB, API) | `core/renderer.py` | `DataBindingEngine.load_data()` — parse into a dict/list context; today only `.json` and `.csv` branches exist |
| New Jinja2 filter | `core/renderer.py` | `_register_filters()` — function returning a Markdown string, registered on `self.env.filters` |
| New Markdown node type | `core/ast_engine.py` | Add mistune plugin in `MarkdownParser.__init__`, a `NodeType` member, and mapping arms in `_map_mistune_node()` and `render()`; unmapped nodes must keep raising `UNSUPPORTED_AST_NODE` |
| New sync target | `core/sync.py`, `sync/targets.yaml` | Add a `SyncTarget` to `TARGETS`; command is a `List[str]` template, missing tools must return `ERROR`, never fake success |
| New doctor check | `core/doctor.py` | Extend `run_doctor()`; classify findings as error vs warning (warnings only gate under `--strict`) |
| New frontmatter field | `core/frontmatter.py` | Extend the schema; unknown fields stay warnings, type/enum violations stay errors |
| New test suite | `tests/`, `Makefile` | Add the file, then wire it into an existing target or a new one in `test` |

## 5. Hard rules

1. **AST-first.** Never use regex or string replacement to change Markdown
   structure. Parse, mutate `ASTNode` objects, re-render.
2. **No `shell=True`.** All subprocess calls use argument lists.
3. **Direct-run bootstrap.** Core modules that run as scripts keep this guard
   before intra-repo imports:

   ```python
   if __package__ in (None, ""):
       sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
   ```

4. **Dependency policy.** Runtime deps are exactly `jinja2`, `mistune`
   (≥ 3.2.1 recommended floor; AST exit point is `renderer='ast'`), and
   `pyyaml`. Format conversion goes through external commands (pandoc,
   xelatex, cp), not new Python packages. Any new dependency needs
   justification and must be recorded in `MANIFEST.yaml` and both READMEs.
5. **Honest status.** Every capability is labeled Implemented / Optional /
   Experimental / Not Integrated in the README capability matrix and mirrored
   in `MANIFEST.yaml`. New modules not wired into a validated entry point are
   Experimental. Keep `README.md` and `README_zh.md` (and the ARCHITECTURE
   pair) in sync in the same commit.
6. **Preserve tracker paths.** `DiffTracker` keys nodes by structural path
   (`root/table[0]/table_row[1]`). Do not change AST nesting in a way that
   breaks path uniqueness in `core/incremental.py`.
7. **Executable docs.** Every ` ```python ` block in the README and
   ARCHITECTURE files is executed by `tests/test_doc_examples.py`. Keep
   examples runnable, or start the block with `# doc-example: skip` when it
   needs external tools.

## 6. Before you finish

- `make test` is green (all five suites, exit 0).
- New/changed behavior has a test in the matching suite.
- Capability matrix, MANIFEST, and bilingual docs reflect what you actually
  shipped — nothing more.
