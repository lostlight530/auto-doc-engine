# auto-doc-engine 示例

[English](README.md) · [根 README](../README_zh.md)

这里记录真实运行入口，不记录 GitHub workflow 指令。外部转换器与外部 validator 仍属于环境相关能力。

## 1. 读取结构化数据并渲染

当前支持 JSON / CSV / YAML / YML

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
print(engine.render("paper_summary.j2", context))
```

也可以直接看仓库 demo：

```bash
python core/renderer.py
```

## 2. Markdown AST

```python
from core.ast_engine import MarkdownParser

parser = MarkdownParser()
root = parser.parse("# **Evidence**\n\n1. source\n2. result\n")
print(parser.render(root))
```

这里输出的是 normalized Markdown，不是原文件字节级复刻

## 3. 结构差异

```bash
python core/incremental.py
```

输出 add / modify / delete / unchanged 结构记录，不负责自动 patch 和冲突解决

## 4. 文档图与诊断

```bash
python core/cross_ref.py
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
```

`--strict` 只表示“warning 也让当前命令返回非零”，不创建 GitHub 合并门禁

## 5. SARIF

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
```

输出目标为 SARIF 2.1.0 + Approved Errata 01，并保留 Doctor profile 与稳定 finding identity

## 6. 多格式同步

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
print(results)
```

Markdown 使用 Python 原生复制；Pandoc / XeLaTeX 路径仍为可选；HTML 可以走 Mistune fallback

## 7. 直接生成 RO-Crate 1.3 metadata

```bash
python core/ro_crate.py output report.md \
  --name "Research artifact set" \
  --description "One report with declared contextual metadata" \
  --author lostlight530 \
  --license MIT
```

生成 `output/ro-crate-metadata.json`

这表示仓库已经有真实 writer，不表示外部 validator 已经替这份 crate 完成认证

## 8. SyncEngine 自动打包成功产物

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

`sync/targets.yaml` 还可以配置默认 crate name / description / authors / license

## 9. 科研 frontmatter

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

未知字段 warning；它是仓库的有界 portable metadata contract，不是完整出版物 ontology

## 10. 实验区

实验文件可以单独探索，但不是规范主链入口

- template prewarm = LRU cache
- async conduit = bounded scheduler
- memory lattice = local node/link store
- restart protocol = conditional replay verification
- self observe = instrumentation

历史命名保留不等于名字中的隐喻就是已实现事实
