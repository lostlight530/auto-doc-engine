# auto-doc-engine Examples

[简体中文](README_zh.md) · [Root README](../README.md)

These examples are operational entry points, not GitHub workflow instructions. External converter/validator behavior remains environment-dependent.

## 1. Render structured data

The renderer accepts JSON, CSV and YAML/YML.

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
print(engine.render("paper_summary.j2", context))
```

The shipped template demos can also be inspected directly:

```bash
python core/renderer.py
```

## 2. Parse and normalize Markdown AST

```python
from core.ast_engine import MarkdownParser

parser = MarkdownParser()
root = parser.parse("# **Evidence**\n\n1. source\n2. result\n")
print(parser.render(root))
```

Normalized rendering preserves the supported structure, not the source file's exact bytes.

## 3. Compute structural changes

```bash
python core/incremental.py
```

The output reports add/modify/delete/unchanged structural records. It is not an automatic patch or conflict resolver.

## 4. Build and diagnose a document graph

```bash
python core/cross_ref.py
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
```

`--strict` only asks the command to return non-zero for warnings too. It does not create a GitHub merge gate.

## 5. Export diagnostics as SARIF

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
```

The result targets SARIF 2.1.0 + Approved Errata 01 and links back to the versioned Doctor profile.

## 6. Synchronize formats

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
print(results)
```

Markdown copying is built in. Pandoc/XeLaTeX-dependent paths remain optional. HTML can use the Mistune fallback.

## 7. Generate RO-Crate 1.3 metadata directly

```bash
python core/ro_crate.py output report.md \
  --name "Research artifact set" \
  --description "One report with declared contextual metadata" \
  --author lostlight530 \
  --license MIT
```

This creates `output/ro-crate-metadata.json` describing the selected payload. File generation is not evidence that an external validator has certified the crate.

## 8. Let SyncEngine package successful outputs

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_ro_crate=True,
)
print(results["ro_crate"])
```

`sync/targets.yaml` also supports opt-in default crate metadata such as name, description, authors and license.

## 9. Research frontmatter

```yaml
---
title: Evidence synthesis
description: Summary of declared sources
status: draft
updated: 2026-08-23
authors: [lostlight530]
sources: [source-a, source-b]
license: MIT
artifact_id: synthesis-001
---
```

Unknown fields are warnings. This is a bounded repository metadata contract rather than a universal publication ontology.

## 10. Experimental modules

Experimental files can be imported for isolated exploration, but they are not canonical pipeline entry points. Their historical names must not be treated as capability claims.
