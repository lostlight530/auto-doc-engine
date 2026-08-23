# Agent Guide — auto-doc-engine

This file is the operational guide for agents modifying the repository. Read `ARCHITECTURE.md` for design rationale and `README.md` / `README_zh.md` / `MANIFEST.yaml` for the current capability boundary.

## 1. System identity

This repository is an AST-driven document compiler toolkit with six integrated concerns: rendering, AST parsing, structural diff, document graph, health diagnosis, and SARIF diagnostic interchange, followed by optional format synchronization. It is **not** a universal end-to-end publishing service.

## 2. Integrated map

```text
core/renderer.py      JSON/CSV -> Jinja2 Markdown
core/ast_engine.py    Markdown <-> typed AST
core/incremental.py   structural diff records
core/cross_ref.py     document/heading graph + broken-link diagnosis
core/frontmatter.py   YAML metadata validation
core/readability.py   heuristic report signals
core/doctor.py        native health aggregation + explicit exit status
core/sarif.py         SARIF 2.1.0 + Errata 01 interchange profile
core/sync.py          optional external-format conversion
```

The following remain Experimental and must not be described as integrated: `template_prewarm.py`, `self_observe.py`, `async_conduit.py`, `memory_lattice.py`, `restart_protocol.py`.

## 3. Local checks

When useful, the repository can be inspected locally with:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

`make test` covers README truth-contract checks, core module tests, incremental/cross-reference tests, the health suites, executable documentation, and `tests.test_sarif`. These checks are maintenance tools, not an automated merge gate. Optional Pandoc/XeLaTeX behavior remains environment-dependent.

## 4. Doctor / SARIF operations

```bash
python core/doctor.py <docs_dir> [--strict] [--json]
python core/sarif.py <docs_dir> [-o report.sarif] [--strict] [--no-readability]
```

Native doctor severity is the source of truth. The SARIF layer maps that model; it must not invent a second severity system.

## 5. Where to change what

| Change | Primary files | Required follow-up |
|---|---|---|
| data source | `core/renderer.py` | both READMEs + MANIFEST; nearest local checks when useful |
| Markdown node | `core/ast_engine.py` | parser/render docs; preserve explicit unsupported-node failure |
| diff semantics | `core/incremental.py` | document identity/path impact |
| graph diagnosis | `core/cross_ref.py` | doctor/SARIF mapping review |
| doctor finding | `core/doctor.py` | severity decision + `core/sarif.py` rule |
| SARIF mapping | `core/sarif.py` | stable rule/fingerprint contract |
| frontmatter schema | `core/frontmatter.py` | classify error vs warning |
| sync target | `core/sync.py`, `sync/targets.yaml` | dependency/failure docs |
| public capability | README pair, ARCHITECTURE pair, MANIFEST | update in the same change |

## 6. Hard rules

1. **AST first.** Never perform structural Markdown mutation with regex/string replacement.
2. **No `shell=True`.** External processes use argument arrays.
3. **Direct-run bootstrap.** Script-style core modules keep the repository-root bootstrap before intra-repo imports.
4. **Explicit failure.** Missing dependencies, unsupported nodes, invalid metadata, and broken links remain observable failures.
5. **Honest status.** A source file alone is not implementation evidence; unwired modules remain Experimental.
6. **Stable SARIF identity.** `ruleId` names and `autoDocFinding/v1` partial fingerprints are interoperability contracts. Change the version if identity semantics change.
7. **No timestamp fingerprints.** Fingerprints use logical identity only, so reruns can correlate findings.
8. **Executable docs.** Python-fenced README/ARCHITECTURE examples are executable documentation. Keep them runnable or use non-Python fences for illustrative commands.
9. **Bilingual architecture sync.** README and ARCHITECTURE language pairs must describe the same capability boundary.
10. **Evidence is scoped.** A successful local check does not prove optional converter availability or scientific validity.

## 7. Consistency

When behavior changes, keep code, README / ARCHITECTURE, and MANIFEST aligned. Do not silently promote Experimental modules, overstate SARIF conformance, or infer environment-dependent capability from file presence.
