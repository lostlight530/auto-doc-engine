# auto-doc-engine Examples

[简体中文](README_zh.md) · [Root README](../README.md) · [Artifact Record Contract](../ARTIFACT_RECORD.md)

These are operational entry points, not GitHub workflow instructions.

## Render structured data

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
print(engine.render("paper_summary.j2", context))
```

Supported sources: JSON, CSV, YAML/YML.

## Parse normalized Markdown structure

```python
from core.ast_engine import MarkdownParser

parser = MarkdownParser()
root = parser.parse("# Evidence\n\n1. source\n2. result\n")
print(parser.render(root))
```

Normalized rendering preserves supported structure, not exact source bytes.

## Structural change and diagnostics

```bash
python core/incremental.py
python core/cross_ref.py
python core/doctor.py path/to/docs --json
python core/sarif.py path/to/docs -o output/doctor.sarif
```

Structural diff is not merge. Doctor/SARIF output is not scientific review certification. SARIF uses the real external 2.1.0 + Approved Errata 01 standard.

## Format synchronization

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
```

Markdown copying is built in. Pandoc/PDF-engine paths remain optional and environment-dependent.

## Frontmatter and process disclosure

```yaml
---
title: Evidence synthesis
status: draft
updated: 2026-08-27
authors: [lostlight530]
sources: [source-a, source-b]
artifact_id: synthesis-001
ai_assistance: used
ai_tools: [declared-tool-id]
human_review: reviewed
---
```

```text
AI tool identifier != independently verified provider identity
reviewed != peer reviewed
```

## Generate an artifact record

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

The stable project profile is `auto-doc-engine/artifact-record`. It indexes identities and declared context; it does not establish scientific validity.

## SyncEngine artifact record

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

R1 is local replay-addressable metadata, not independent reproduction.

## RO-Crate 1.3

```bash
python core/ro_crate.py output report.md \
  --name "Research artifact set" \
  --description "One report with declared contextual metadata" \
  --author lostlight530 \
  --license MIT
```

RO-Crate 1.3 is a real external standard target. File generation does not mean external validator certification.

## Artifact record + RO-Crate

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
    emit_ro_crate=True,
)
```

The artifact record may be packaged as a normal crate File and is not relabelled as an RO-Crate standard profile.

## Downstream handoff

A later Epistemic Pipeline run may reference `output/report.artifact.json`. This is file/reference interoperability, not direct repository coupling or inherited scientific validity.

## Local maintenance

`make test` is an optional local maintenance command, not a GitHub merge gate or scientific-validation step.
