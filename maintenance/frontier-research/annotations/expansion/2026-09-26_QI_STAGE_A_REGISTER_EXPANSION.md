# Annotation Expansion — Stage A SOURCE_OBJECT_REGISTER 锚级批注（扩容样板）

**Reviewer:** 淇（Qi）· 2026-09-26 · 对象：stage-a-2024-q1/SOURCE_OBJECT_REGISTER.md 全部 O/S 条目 · Independence: 同首轮声明 · 本文件为"锚级批注"扩容样板——REGISTER 每对象/每源逐条核验+异源佐证+判定行，行级真内容。

## 0. 总体发现

REGISTER 的对象-源-映射-族-冲突五表结构与 SPEC 的对象/来源/映射分离原则相符（identity rules 八条 != 判据是全系列最佳实践）。O1-O6/S1-S16 的主要缺口不在结构在**来源族多样性**：四族（DataCite/Quarto/Pandoc/Typst）全部 single-family——§5 自己承认"cross-family convergence can support broader interpretation but does not prove causal influence"——**本批注为每个对象补 1-2 个跨族佐证候选**。

## 1. 对象批注（O1-O6 逐条）

### O1 DataCite Metadata Schema 4.5（2024-01-22）
- [版本核验] 4.5.0 于 2024-01-22 发布——与 S1/S2 一致；**4.5 系列的最终补丁 4.5.1/4.5.2 在窗口后**（2024 年中），Register 记"released schema 4.5"未区分小版本——boundary 正确（released schema 泛指）
- [独立佐证候选] DataCite 4.5 的第三方解读线：GBIF/DataCite 集成公告、scholarly 社区（Force11）讨论——跨族佐证建议 2 锚
- [与 Stage 后续关系] 4.5 的 relatedIdentifier 扩张是 Stage B-F"relation semantics"线的规范起点——纵向链接点（LONGITUDINAL 未显式回指——correction 提案）
- [决定] CONFIRMED + 补跨族佐证 2 锚

### O2 Quarto 1.4 release line（1.4.x，三锚点 01-24/02-15/03-05）
- [版本核验] S6/S7/S8 三 tag commit 锚点核实——grouped release-line object 的处理方式聪明（把 1.4.x 线当一个对象而非三次事件）
- [独立佐证候选] Quarto 1.4 的社区侧反应（GitHub issues 峰值/博客评测）——跨族佐证建议 2 锚；**1.4 的 Typst 输出支持是 O6（Typst 0.11）的前史**——O2×O6 的交叉关系 Register 未记录（mapping 表只记 object-source，不记 object-object）——**mapping 表加 object-object 列的 correction 提案**
- [决定] CONFIRMED + object-object 交叉关系提案

### O3 DataCite RFC（2024-03-26）
- [版本核验] proposal 事件正确标注"explicitly not a complete schema version"——**proposal != supersession 判据的正面应用**（§1 identity rules 第 5 条）
- [语境] 2024-03-26 的 RFC 正值 EU CRA 议会表决（03-12）后两周——元数据规范演进与合规压力的同期性（背景线，Stage A 未涉及——见首轮批注 2A.3）
- [决定] CONFIRMED

### O4 Pandoc 3.1.11.1（2024-01-06）
- [版本核验] 1 月维护版定位准确——"output validation/layout fixes"
- [独立佐证候选] 单源（S10）——跨族佐证：发行版打包记录（Debian/Fedora changelog——Pandoc 3.1.11.1 的 distro 进入时间）可作时间戳第二来源
- [决定] CONFIRMED + distro 佐证候选 1

### O5 Pandoc 3.1.12 release family（02-15→03-18 四锚）
- [版本核验] 四 release 锚（S11-S14）+ corrections 三条（§6）——**O5 是 Register 里"forward patch 链"记录最完整的对象**（.1 修回归/.2 无障碍/.3 Typst writer 兼容）——"later correction != rewrite"判据的活体样本
- [关键交叉] **S14（03-18）"adjusts Typst writer after Typst 0.11 behavior"——Pandoc 为 Typst 0.11（03-15 发布后三天）出兼容补丁——O5×O6 的因果级交叉在 §6 已记但 mapping 表未提**——上一条 object-object 提案的第二个实例
- [独立佐证候选] Pandoc 3.1.12 系的社区侧（Haskell 包索引 Hackage 记录）佐证
- [决定] CONFIRMED + object-object 提案第二例 + Hackage 佐证候选

### O6 Typst 0.11.0（2024-03-15）
- [版本核验] 03-15 双源（S15 changelog/S16 release）——table structure + template packages 特征描述准确
- [独立佐证候选] Typst 0.11 的发布是**编译器新势力对 LaTeX 的替代叙事**在 Q1 的节点——LaTeX 侧同期无大版本（背景对照）；社区采用数据（GitHub stars 曲线）可作采用面佐证——**"release != adoption"边界下，采用面佐证是可选增强非必需**
- [决定] CONFIRMED + 采用面佐证候选（optional）

## 2. 源批注（S1-S16 逐条速核）

- S1-S3（DataCite 三源）：normative/rollout/chronology 三职能分工清晰——"same family as S1"的独立性限制标注正确——CONFIRMED ×3
- S4-S8（Quarto 五源）：S4/S5 对 mutable page/branch view 的限制声明清楚地区分了当前页面与历史快照——当前文档≠历史快照，判断正确；S6-S8 使用 commit/tag 级定位，内容身份比 mutable branch/page 更稳定；但 URL 可达性与托管保留仍不是永久保证——CONFIRMED ×5
- S9（RFC post）：non-normative 标注正确——CONFIRMED
- S10-S14（Pandoc 五源）：五 release tag 锚全部不可变引用——CONFIRMED ×5
- S15-S16（Typst 双源）：producer source 限制标注正确——CONFIRMED ×2
- 本批注未执行 16 个 URL 的实时可达性复测；从记录形态看，commit/tag 级定位比 mutable 页面更利于历史复核，S3/S4/S5 的可变性已被原 Register 声明。LINK_HEALTH = NOT_RECHECKED_IN_THIS_ANNOTATION

## 3. 补全汇总（correction 提案）

1. mapping 表加 object-object 交叉列（O5×O6 因果补丁/O2×O6 前史）——2 实例
2. 跨族佐证 7 锚候选清单（GBIF/Force11/distro/Hackage/issues 曲线）
3. 纵向回指针：4.5 作为 B-F relation 线起点——1 句
4. 源健康度声明：16 源 3 mutable 已声明——可入 REGISTER §8

## 4. 扩容方法声明

本样板展示的是一种锚级批注粒度：对象、来源、关系与不确定性分开记录。若推广到其他 Stage，应按真实对象数与证据复杂度决定篇幅，不设行数目标，也不因外部激励或产量目标扩写；只有新增可核验信息、关系或边界时才增加内容。
---
*Expansion annotation ends. 历史文件零改动。*
