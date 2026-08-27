# auto-doc-engine Examples

[简体中文](README_zh.md) · [Root README](../README.md) · [Artifact Record Contract](../ARTIFACT_RECORD.md)

These are operational entry points, not GitHub workflow instructions. External converter/validator behavior remains environment-dependent.

## 1. Render structured data

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
print(engine.render("paper_summary.j2", context))
```

Supported source formats: JSON, CSV, YAML/YML.

## 2. Parse and normalize Markdown AST

```python
from core.ast_engine import MarkdownParser

parser = MarkdownParser()
root = parser.parse("# **Evidence**\n\n1. source\n2. result\n")
print(parser.render(root))
```

Normalized rendering preserves the supported structure, not exact source bytes.

## 3. Structural changes

```bash
python core/incremental.py
```

The output reports add/modify/delete/unchanged structural records. It is not a patch/merge engine.

## 4. Document graph and diagnostics

```bash
python core/cross_ref.py
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
```

`--strict` changes only the local process exit status. It does not create a GitHub merge gate.

## 5. SARIF findings

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
```

The file targets SARIF 2.1.0 + Approved Errata 01 and preserves Doctor profile/finding identity. It is not scientific review certification.

## 6. Format synchronization

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
print(results)
```

Markdown copying is built in. Pandoc/PDF-engine paths remain optional. HTML can use the Mistune fallback.

## 7. Research frontmatter + process disclosure

```yaml
---
title: Evidence synthesis
status: draft
updated: 2026-08-27
authors: [lostlight530]
sources: [source-a, source-b]
artifact_id: synthesis-001
ai_assistance: used
ai_tools: [declared-provider/model]
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

The process fields are declarations only:

```text
AI tool identifier != independently verified provider identity
reviewed != peer reviewed
```

## 8. Generate a standalone artifact record

Assume `output/report.html` already exists:

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync@1 \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

The record indexes source/derivative byte identities, bounded metadata, process disclosure and diagnostics. It does not embed the full report text or establish scientific validity.

## 9. Let SyncEngine emit the artifact record

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
print(results["artifact_record"])
```

Equivalent opt-in configuration:

```yaml
artifact_record:
  emit: true
  reproducibility_level: R1
```

R1 is local replay-addressable metadata, not independent reproduction.

## 10. Generate RO-Crate 1.3 metadata directly

```bash
python core/ro_crate.py output report.md \
  --name "Research artifact set" \
  --description "One report with declared contextual metadata" \
  --author lostlight530 \
  --license MIT
```

File generation is not evidence that an external validator has certified the crate.

## 11. Artifact record + RO-Crate together

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
    emit_ro_crate=True,
)
```

Order:

```text
render derivatives
  -> report.artifact.json
  -> ro-crate-metadata.json
```

The artifact record may become a normal crate payload. It is **not** re-labelled as an RO-Crate standard profile.

## 12. Downstream handoff example

A later `epistemic-pipeline` run can reference the artifact record:

```bash
python core/run_bundle.py graphs/linear.yaml \
  --upstream-artifact-ref output/report.artifact.json
```

This is a file/reference handoff convention, not direct repository coupling.

## 13. Experimental modules

Experimental files may be explored independently but are not canonical pipeline entry points. Their historical names do not establish autonomous, semantic-memory or physics capabilities.

## 14. Optional local checks

```bash
make test
```

This is a manual maintenance command, not a GitHub merge gate or scientific-validation step.
