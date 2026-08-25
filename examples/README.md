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

## 9. Research frontmatter and process disclosure

```yaml
---
title: Evidence synthesis
description: Summary of declared sources
status: draft
updated: 2026-08-26
authors: [lostlight530]
sources: [source-a, source-b]
license: MIT
artifact_id: synthesis-001
ai_assistance: used
ai_tools:
  - provider/model or tool identifier declared by the author
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

Process-disclosure enums:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Unknown fields are warnings. Invalid types/enums are errors. Cross-field disclosure gaps are warnings; for example, `ai_assistance: used` with no usable `ai_tools` entry.

These fields are bounded project metadata. They do not establish authorship, provider authenticity, peer review, scientific truth, publisher compliance, or independent reproduction.

The current RO-Crate writer does not automatically map the process-disclosure fields into RO-Crate standard properties.

See `PROCESS_DISCLOSURE.md` for the full field contract.

## 10. Cross-repository handoff

A downstream research run can preserve the artifact's declared process context without importing this repository:

```text
auto-doc-engine frontmatter
  -> epistemic-pipeline/evidence-envelope@2
  -> sci-render-kit/figure-evidence@2
```

Preferred fields include artifact identity/source refs plus `ai_assistance`, `ai_tools`, `human_review`, and `disclosure_ref` when declared.

## 11. Experimental modules

Experimental files can be imported for isolated exploration, but they are not canonical pipeline entry points. Their historical names must not be treated as capability claims.
