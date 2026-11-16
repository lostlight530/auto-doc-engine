# 01 — Source and Explanation

## 中文技术对应 / Chinese technical reading

**实际对象 / Owning subject:** 本目录定位 source、architecture 和证据的解释入口，源码归属不能被导航内容覆盖

**English document title:** 01 — Source and Explanation

**运行与证据区分 / Evidence distinction:** 需要明确 producer/consumer 的 profile、源码版本、输入/sidecar bytes、实际命令与失败状态，静态参考与交付示例不能冒充真实三仓联调或外部科学验真 / Preserve exact source revision, profile, source bytes, commands and failures, a documentary contract is not a run receipt

| Source heading / 英文拥有者章节 | 中文阅读归属 / Chinese meaning |
| --- | --- |
| Implementation map | 真实代码归属 |
| Architecture and explanatory documents | 当前工程合同及其具体边界 |
| How to establish current behavior | 怎样证实当前运行行为 |
| Engineering evidence boundary | 工程证据边界 |
| Related long-lived contracts | 当前工程合同及其具体边界 |

**保留 / Preservation:** 原始英文合同字段、sample payload、历史 Stage 和运行未知状态不被本翻译改变 / Source technical semantics and dated evidence are preserved


This class answers three durable questions:

1. **What does auto-doc-engine actually implement?**
2. **Where is that behavior explained?**
3. **Which observations are engineering evidence rather than scientific validation?**

## Implementation map

| Surface | Repository role | Boundary |
|---|---|---|
| `core/` | document parsing, transformation, artifact/diagnostic logic, and executable library behavior | source code defines implemented predicates; prose cannot add capability |
| `templates/` | repository-owned document templates and rendering inputs | a template describes structure, not successful generation or scientific quality |
| `sync/` | declared synchronization targets and related behavior | configured target != successful external synchronization |
| `tests/` | executable regression/contract evidence for tested behavior | passing tests apply only to the tested revision/environment/cases |
| `Makefile` | supported engineering command entry points | command presence != command execution |

`core/maintenance_cadence.py` remains executable source in this class because classification follows implementation role, even though that module supports maintenance documents elsewhere.

## Architecture and explanatory documents

- root [`README.md`](../../README.md) — public repository entry point and capability overview.
- root [`README_zh.md`](../../README_zh.md) — Chinese public entry point; should remain semantically aligned with the English surface where both describe the same capability.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — detailed current architecture, component boundaries, data/control flow, optional-tool boundaries, and cross-repository handoff context.
- [`ARCHITECTURE_zh.md`](./ARCHITECTURE_zh.md) — Chinese architecture explanation; translation alignment does not mean either document outranks implementation.

## How to establish current behavior

For a concrete capability claim, read in this order:

```text
owning implementation
→ machine-readable contract/configuration for that subject
→ revision-matched test or observed execution when claimed
→ active specialized contract
→ Architecture / README explanation
```

A historical maintenance record, an archived publication, or a successful documentation build cannot silently strengthen what the implementation supports.

## Engineering evidence boundary

Keep these identities separate:

```text
source code present
!= code executed

test defined
!= test executed

artifact generated
!= artifact scientifically valid

SHA-256 identity
!= semantic equivalence

optional external tool documented
!= tool available in a particular environment
```

When execution matters, retain the revision, environment, exact command/input, result, and untested boundary.

## Related long-lived contracts

The documents under [`../02-examples-and-contracts/`](../02-examples-and-contracts/) explain how implemented behavior is represented, constrained, transferred, and interpreted. They do not replace source ownership.

The current document taxonomy is routed from [`../README.md`](../README.md). Current maintenance routing is separate under class 03 and should not be treated as the primary description of auto-doc-engine itself.
