# auto-doc-engine 示例

[English](README.md) · [根 README](../README_zh.md) · [Artifact Record Contract](../ARTIFACT_RECORD.md)

这里记录真实运行入口，不记录 GitHub workflow 指令

## 结构化数据渲染

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
print(engine.render("paper_summary.j2", context))
```

支持 JSON / CSV / YAML / YML

## Markdown Typed AST

```python
from core.ast_engine import MarkdownParser

parser = MarkdownParser()
root = parser.parse("# Evidence\n\n1. source\n2. result\n")
print(parser.render(root))
```

输出是 normalized Markdown，不是原文件字节级复刻

## 结构差异与诊断

```bash
python core/incremental.py
python core/cross_ref.py
python core/doctor.py path/to/docs --json
python core/sarif.py path/to/docs -o output/doctor.sarif
```

structural diff 不是 merge；Doctor/SARIF 不是 scientific review certification；SARIF 真实外部标准版本为 2.1.0 + Approved Errata 01

## 多格式同步

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
```

Markdown 使用 Python 原生复制；Pandoc / PDF engine 保持可选

## Frontmatter + Process Disclosure

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
AI tool identifier != 已验证 provider identity
reviewed != peer reviewed
```

## 生成 Artifact Record

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

稳定项目 profile 为 `auto-doc-engine/artifact-record`

它索引 source / derivative byte identity、有界 metadata、过程披露和 diagnostics，不判断来源可信、作者资格或 scientific validity

## SyncEngine 生成 Artifact Record

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

R1 是项目内 replay-addressable metadata，不是独立复现

## RO-Crate 1.3

```bash
python core/ro_crate.py output report.md \
  --name "Research artifact set" \
  --description "One report with declared contextual metadata" \
  --author lostlight530 \
  --license MIT
```

RO-Crate 1.3 是真实外部标准目标，生成文件不代表外部 validator 已认证

## Artifact Record + RO-Crate

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
    emit_ro_crate=True,
)
```

`.artifact.json` 可以作为普通 crate File payload 被 package，但不会因此变成 RO-Crate 标准 profile

## 下游 handoff

后续 Epistemic Pipeline 可以引用 `output/report.artifact.json`；这是文件/引用约定，不是直接 import 或 inherited scientific validity

## 本地维护

`make test` 只是可选本地维护命令，不是 GitHub merge gate 或 scientific validation
