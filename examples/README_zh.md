# auto-doc-engine 示例

[English](README.md) | [根 README](../README_zh.md)

这里记录仓库的真实入口。确定性能力由 `make test` 与 GitHub Actions 契约覆盖；外部转换器仍属于环境相关的可选能力。

## 渲染示例文档

```bash
python core/renderer.py
```

## 计算结构变化

```bash
python core/incremental.py
```

输出是结构 Diff 描述，不等于自动解决人类/Agent 并发编辑冲突。

## 建立并诊断文档图

```bash
python core/cross_ref.py
python core/doctor.py .
```

`doctor` 聚合链接、图结构、frontmatter 与可读性证据。需要让警告也阻断命令时使用 `--strict`。

## 把同一健康模型导出为 SARIF

```bash
python core/sarif.py . -o output/doctor.sarif
```

输出面向 OASIS SARIF 2.1.0 + Errata 01，并使用稳定、版本化 partial fingerprint。它让诊断结果可以被下游工具交换，而不会另造一套 doctor 严重级别。

## 可选格式同步

```bash
python core/sync.py
```

HTML 可使用本地 Mistune 回退；其他目标可能依赖 Pandoc / XeLaTeX。缺少这些工具时不能把对应格式包装成已验证。

## 仅有模板的场景

`paper_summary.j2` 与 `project_status.j2` 可以使用本地 JSON / CSV 上下文渲染。网络 API 获取器与 SQLite 适配器仍是“当前未集成”；模板存在本身不是数据源适配器的实现证据。
