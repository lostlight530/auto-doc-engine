# Artifact lineage example

## 中文技术对应 / Chinese technical reading

**实际对象 / Owning subject:** 本示例演示声明的 Artifact Lineage 数据格式和可复核链接，不代表生产数据、外部科研结果或自动获得 R3 复现

**English document title:** Artifact lineage example

**运行与证据区分 / Evidence distinction:** 需要明确 producer/consumer 的 profile、源码版本、输入/sidecar bytes、实际命令与失败状态，静态参考与交付示例不能冒充真实三仓联调或外部科学验真 / Preserve exact source revision, profile, source bytes, commands and failures, a documentary contract is not a run receipt

| Source heading / 英文拥有者章节 | 中文阅读归属 / Chinese meaning |
| --- | --- |


**保留 / Preservation:** 原始英文合同字段、sample payload、历史 Stage 和运行未知状态不被本翻译改变 / Source technical semantics and dated evidence are preserved


Generate a normal artifact record first, then describe its relationship to earlier/related artifacts without modifying the original record.

```bash
python core/artifact_lineage.py output/report.artifact.json \
  --relation revision-of=archive/report-v1.artifact.json \
  --relation uses=data/source-dataset.json \
  --output output/report.lineage.json
```

Supported declared relations:

```text
derived-from
revision-of
supersedes
uses
related-to
```

Local target files receive SHA-256 identity. URI/opaque references are preserved without network dereference.

```text
revision-of != semantic equivalence
supersedes != deletion of history
uses != evidence sufficiency
lineage != scientific validity
```
