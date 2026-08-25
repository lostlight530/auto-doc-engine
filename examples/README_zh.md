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

## 9. 科研 frontmatter 与过程披露

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
  - 由作者声明的 provider/model 或工具标识
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

允许值：

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

未知字段 warning，非法 type / enum error

跨字段不一致保持 warning，例如：

- `ai_assistance: used` 但没有有效 `ai_tools`
- 已列出 `ai_tools`，但 assistance 缺失 / `none` / `not_declared`

这些字段只是项目级过程元数据，不证明：

```text
作者资格
模型/工具真实身份
peer review
scientific truth
publisher AI-policy compliance
independent reproduction
```

当前 RO-Crate writer 也不会自动把这组项目字段写成 RO-Crate 标准属性

详细字段语义见根目录 `PROCESS_DISCLOSURE.md`

## 10. 三仓交接示例

```text
auto-doc-engine frontmatter
  -> epistemic-pipeline/evidence-envelope@2
  -> sci-render-kit/figure-evidence@2
```

如果声明存在，推荐把 artifact identity/source refs 与 `ai_assistance`、`ai_tools`、`human_review`、`disclosure_ref` 一起交给下游

这只是 interoperability contract，不要求三仓直接 import

## 11. 实验区

实验文件可以单独探索，但不是规范主链入口

- template prewarm = LRU cache
- async conduit = bounded scheduler
- memory lattice = local node/link store
- restart protocol = conditional replay verification
- self observe = instrumentation

历史命名保留不等于名字中的隐喻就是已实现事实
