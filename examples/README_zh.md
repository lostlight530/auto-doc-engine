# 🧪 auto-doc-engine 示例

[🇨🇳 简体中文](README_zh.md) | [🇺🇸 English](README.md)

---

本目录包含了 `auto-doc-engine` 的核心功能演示与实战用例。

## 📊 示例：全自动周报生成

本示例展示了如何将一个普通的 CSV 数据源，自动转化、绑定并发布为多格式的精美周报。

### 1. 准备原始数据源
```bash
cat > data/weekly_data.csv << 'EOF_CSV'
week,task,status,owner
2026-W25,AST引擎重构,完成,Alice
2026-W25,增量更新引擎开发,完成,Bob
2026-W25,多格式同步加固,进行中,Carol
EOF_CSV
```

### 2. 数据绑定与文档生成
运行渲染引擎，将 CSV 数据灌入 Jinja2 逻辑模板，并初步解析为 AST 树结构：
```bash
python core/renderer.py
```

### 3. 计算增量变更记录
对比上一次的生成结果，精准计算 AST 结构的 Diff 差异，并将历史写入跟踪器：
```bash
python core/incremental.py
```

### 4. 同步分发多格式文档
安全调用底层引擎，一键同步生成 Markdown 和 HTML 实体文件：
```bash
python core/sync.py
```

---

## 🛠 更多能力场景展示

| 示例名称 | 业务说明 |
|:---|:---|
| **学术论文摘要** | 读取远端 JSON API 自动生成结构化的每日学术速递 |
| **项目风险预警** | 绑定 SQLite 数据库自动生成排版精良的开发状态与风险评估报表 |
