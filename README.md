# auto-doc-engine

> AST-driven document compilation, structural diffing, document-graph health checks, and standards-based diagnostic interchange.

[简体中文](README_zh.md) | [Architecture](ARCHITECTURE.md) | [Examples](examples/README.md)

## Positioning

`auto-doc-engine` treats Markdown as a typed document structure rather than a string blob. The repository is a collection of independently callable modules, not a single production pipeline facade. The design goal is **deterministic evidence before capability claims**: parsing, diffing, cross-document diagnosis, health reporting, and export each have an explicit boundary.

## Capability matrix

| Capability | Status | Evidence and boundary |
|---|---|---|
| `core/renderer.py` | Implemented | Jinja2 rendering; JSON/CSV loading; `table` and `bullet_list` filters. SQLite/API adapters are not integrated. |
| `core/ast_engine.py` | Implemented | Mistune-backed Markdown AST mapping and rendering. Unsupported nodes fail explicitly. |
| `core/incremental.py` | Implemented | Structural add/modify/delete/unchanged records using recursive sibling alignment. This is a diff report, not an automatic conflict-free merge guarantee. |
| `core/sync.py` | Implemented interface / Optional conversion | Argument-list subprocess execution. HTML may use the Mistune fallback; DOCX/PDF/EPUB depend on external tools. |
| `core/cross_ref.py` | Implemented | AST-based document/heading index, link graph, near-miss vs dangling diagnostics, recurring missing-target backlog. |
| `core/doctor.py` | Implemented | Aggregates broken links, orphans, cycles, frontmatter issues, readability signals, and graph statistics; error findings produce a non-zero exit status. |
| `core/sarif.py` | Implemented | Exports doctor findings as a conservative **SARIF 2.1.0 + Errata 01** result set with stable versioned partial fingerprints. |
| `core/frontmatter.py` | Implemented | YAML frontmatter parsing and hand-written schema validation. |
| `core/readability.py` | Implemented | Report-mode Latin/CJK readability heuristics; never presented as a quality guarantee. |
| executable documentation | Implemented | Local documentation checks can execute Python-fenced examples in README/ARCHITECTURE documents. |
| SQLite/API data sources | Not Integrated | No production adapter or contract exists. |
| `template_prewarm`, `self_observe`, `async_conduit`, `memory_lattice`, `restart_protocol` | Experimental | Source exists but is not wired into a validated canonical flow. |

## Architecture in one line

```text
Data -> Template -> Markdown AST -> Structural Diff -> Document Graph -> Health Diagnostics -> Text/JSON/SARIF -> Optional Format Sync
```

The layers share one principle: **do not infer success from the existence of a file or declaration**. A capability is Implemented only when code and repository evidence support the stated boundary.

## Python API example

The AST layer is directly usable without going through a repository workflow:

```python
from core.ast_engine import MarkdownParser

root = MarkdownParser().parse("# Research note\n")
assert root.children
```

## Doctor and SARIF

Human/JSON health checks:

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --strict
python core/doctor.py path/to/docs --json
```

Standards-based interchange:

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
python core/sarif.py path/to/docs --strict -o output/doctor.sarif
```

The SARIF exporter targets OASIS SARIF 2.1.0 incorporating Approved Errata 01. It uses stable `ruleId` values and `autoDocFinding/v1` partial fingerprints so downstream systems can correlate the same logical finding across repeated audits. SARIF is used here as a result-interchange container; the project does **not** claim that Markdown health analysis is source-code static analysis.

## Local checks

For contributors who want to inspect the deterministic Python surface locally:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

These checks cover the README truth contract, renderer/AST/sync, incremental diff, cross-document graph, health layer, executable docs, and SARIF export. They are a local maintenance aid, **not a GitHub merge gate**.

Environment-dependent converters remain outside that local surface: Pandoc/XeLaTeX availability is reported honestly and is not converted into a fake pass.

## Dependencies and failure behavior

- **Python:** `jinja2`, `mistune>=3.2.1`, `pyyaml`.
- **Optional external tools:** Pandoc, XeLaTeX, and the current Markdown-copy command.
- Unsupported AST nodes, broken links, invalid frontmatter, missing converters, and CLI usage errors surface explicitly.
- Runtime artifacts (`output/`, `incremental/`) are generated state, not source directories.

## Repository map

```text
auto-doc-engine/
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── sync.py
│   ├── cross_ref.py
│   ├── doctor.py
│   ├── sarif.py
│   ├── frontmatter.py
│   └── readability.py
├── templates/jinja2/
├── sync/targets.yaml
├── tests/
├── examples/
├── CITATION.cff
└── MANIFEST.yaml
```

## Boundaries

- There is still no unified end-to-end production facade that guarantees every data source and every output format in one call.
- Parse/render is structural, not byte-for-byte Markdown preservation.
- Structural diff records do not themselves apply safe merges or resolve human/agent edit conflicts.
- Readability and near-miss matching are heuristic signals.
- SARIF export is an interoperability profile for findings, not proof of conformance by downstream consumers.

## Citation and license

Software citation metadata is provided in `CITATION.cff` (CFF 1.2.0). License: MIT.
