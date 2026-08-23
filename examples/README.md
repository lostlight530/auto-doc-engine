# auto-doc-engine Examples

[简体中文](README_zh.md) | [Root README](../README.md)

These examples describe repository entry points. Deterministic behavior is covered by `make test` and the GitHub Actions contract; optional external converters remain environment-dependent.

## Render a sample document

```bash
python core/renderer.py
```

## Compute structural changes

```bash
python core/incremental.py
```

The output is a structural diff description. It is not an automatic conflict resolver for concurrent edits.

## Build and diagnose a document graph

```bash
python core/cross_ref.py
python core/doctor.py .
```

`doctor` combines link, graph, frontmatter, and readability evidence. Use `--strict` when warnings should also gate the command.

## Export the same health model as SARIF

```bash
python core/sarif.py . -o output/doctor.sarif
```

The result targets OASIS SARIF 2.1.0 + Errata 01 and uses stable versioned partial fingerprints. This enables result interchange without changing the native doctor severity model.

## Optional format synchronization

```bash
python core/sync.py
```

HTML may use the local Mistune fallback. Other targets can require Pandoc/XeLaTeX and must not be reported as verified when those tools are absent.

## Template-only scenarios

`paper_summary.j2` and `project_status.j2` can be rendered from local JSON/CSV context. A network API fetcher and SQLite adapter remain Not Integrated; the existence of a template is not evidence of a data-source adapter.
