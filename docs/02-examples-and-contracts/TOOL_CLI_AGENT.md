# Research document Tool / CLI / Agent console

## 中文技术对应 / Chinese technical reading

**实际对象 / Owning subject:** 本地 CLI 工具入口采用显式 allowlist 和参数合同，不等于 MCP 服务、网络代理、shell 任意执行或无条件授权

**English document title:** Research document Tool / CLI / Agent console

**运行与证据区分 / Evidence distinction:** 需要明确 producer/consumer 的 profile、源码版本、输入/sidecar bytes、实际命令与失败状态，静态参考与交付示例不能冒充真实三仓联调或外部科学验真 / Preserve exact source revision, profile, source bytes, commands and failures, a documentary contract is not a run receipt

| Source heading / 英文拥有者章节 | 中文阅读归属 / Chinese meaning |
| --- | --- |
| Where this sits | 当前工程合同及其具体边界 |
| Registered tools | 当前工程合同及其具体边界 |
| CLI: immediate practical use | 当前工程合同及其具体边界 |
| Programmatic Agent binding (no vendor SDK needed) | 当前工程合同及其具体边界 |
| Agent plan harness: human collaboration and bounded execution | 当前工程合同及其具体边界 |
| Stable result contract | 当前工程合同及其具体边界 |
| UI style and accessibility scope | 当前工程合同及其具体边界 |
| Test and operational verification | 当前工程合同及其具体边界 |

**保留 / Preservation:** 原始英文合同字段、sample payload、历史 Stage 和运行未知状态不被本翻译改变 / Source technical semantics and dated evidence are preserved


> Current implementation surface · 2026-10-19 · `auto-doc-engine/tool-adapter`

## Where this sits

```text
caller / human / independent agent
    ├─ import agent_tools.tool_definitions() → JSON Schema declarations
    ├─ import agent_tools.execute_tool_call(name, arguments)
    └─ tool_cli.py (JSON / styled terminal / offline HTML)
                    ↓
          explicit allowlist dispatch
                    ↓
             existing core modules
                    ↓
        typed result + explicit error/domain finding
```

This is an **opt-in, local, synchronous** tool adapter. The caller orchestrates model decisions, approvals and persistence. No background agent, scheduler, online gateway, MCP server, remote model SDK, external provider authentication, unrestricted shell or automatic repository edits are introduced.

## Registered tools

`document_inspect` delegates to `core.doctor.run_doctor` to inspect an existing Markdown directory and returns its `DoctorReport` JSON with a separate diagnostic exit code. `artifact_lineage` delegates to `core.artifact_lineage.build_artifact_lineage` for typed, caller-declared relations; it never writes a sidecar.

Tool names, required arguments and JSON Schema are inspected with `list` and `describe`. The registry rejects unknown tool names, unexpected argument keys, wrong value types and malformed JSON before calling implementation. Runtime paths are caller-supplied and are *not* sandboxed; execute only with appropriate filesystem permissions and inspect untrusted inputs independently.

## CLI: immediate practical use

From this repository root with its existing Python dependencies installed:

```bash
python3 tool_cli.py list --format text
python3 tool_cli.py describe document_inspect
python3 tool_cli.py invoke document_inspect --args '{"docs_dir":"docs","with_readability":false}' --format text
python3 tool_cli.py invoke artifact_lineage --args '{"artifact_record":"output/example.artifact-record.json","relations":[{"relation":"uses","target":"docs/README.md"}]}'
```

**JSON-first automation** (single JSON object on stdout, no ANSI escape sequences):

```bash
python3 tool_cli.py list
python3 tool_cli.py invoke document_inspect --args-file request.json > result.json
cat request.json | python3 tool_cli.py invoke document_inspect --args-file - > result.json
```

To generate a **standalone offline UI report**:

```bash
python3 tool_cli.py invoke document_inspect --args '{"docs_dir":"docs","with_readability":false}' --format html --output output/tool-inspection.html
```

Open the resulting HTML file locally. It is a static report; it does not fetch content, execute JavaScript, host a server or provide live agent control.

## Programmatic Agent binding (no vendor SDK needed)

```python
import json
from agent_tools import tool_definitions, execute_tool_call

definitions = tool_definitions()  # agent/model-side function declarations
assert len(definitions) == 2

# The caller chooses an allowlisted function and supplies validated arguments.
name = "document_inspect"
arguments = { "docs_dir": "docs", "with_readability": False }
result = execute_tool_call(name, arguments)
assert result["tool"] == name
print(json.dumps(result, ensure_ascii=False))
```

Stringified JSON arguments are also supported for provider-neutral function-call transport, but there is no built-in provider loop, approval policy, retry orchestration or MCP protocol conformance.

## Agent plan harness: human collaboration and bounded execution

`agent_plan.run_plan(plan, approved=False)` preflights a caller-authored plan of **1–16** allowlisted tool calls without invoking any tool. It returns `APPROVAL_REQUIRED` with the proposed arguments. Unknown tool names, invalid arguments, unexpected keys or more than 16 steps are rejected before execution.

```json
{
  "purpose": "review declared local research assets",
  "on_error": "stop",
  "steps": [
    {"tool": "document_inspect",
     "arguments": {"docs_dir":"docs","with_readability":false}}
  ]
}
```

Save this object as `plan.json`, then review before explicitly approving:

```bash
python3 tool_cli.py plan --plan-file plan.json --format text
python3 tool_cli.py plan --plan-file plan.json --approve --format json
python3 tool_cli.py plan --plan-file plan.json --approve --format html --output output/approved-plan.html
python3 -m unittest tests.test_agent_plan -v
```

`--approve` is **caller-granted approval, not authenticated human identity or remote authorization**. It is deliberately opt-in. On execution, each step returns its own original tool envelope; a failed domain check is retained as a failed step. `on_error: stop` is the default; `continue` must be specified explicitly. No hidden retries, parallel branches, autonomous model reasoning, durable execution, background scheduling or arbitrary shell are implied.

The Agent plan is a narrow caller-to-tool **Harness**, not a replacement for `epistemic-pipeline`'s native StateMachineEngine nor an MCP host. A caller that requires persistent state must separately store and validate the returned JSON.

## Stable result contract

```json
{
  "profile": "auto-doc-engine/tool-adapter",
  "tool": "an-allowlisted-tool",
  "status": "ok",
  "result": {},
  "error": null,
  "scientific_validity_claim": false,
  "remote_provider_called": false
}
```

The execution status reports whether **tool invocation succeeded**, not whether domain findings passed. For CLI automation, exit 0 means invocation and domain checks passed; exit 1 means an invocation or domain check failed; exit 2 means writing the requested output report failed. Error responses include `error.code` such as `UNKNOWN_TOOL`, `INVALID_ARGUMENT` or `EXECUTION_FAILED`. Failures are valid evidence and must not be rewritten into successes.

The doctor scanner reads local Markdown files and may return diagnostic findings; `status: ok` means the adapter executed, whereas `diagnostic_exit_code: 1` is still a failing diagnostic result. File-system symlink limitations and TOCTOU are owned by the cross-reference implementation.

## UI style and accessibility scope

The console shares a single visual language across all three repositories:

| Surface | Design | Reliability boundary |
|---|---|---|
| `--format json` | stable key structure, machine-readable, no decorative output | truth comes only from `status` and domain findings |
| `--format text` | compact cyan console frame, explicit EXECUTED / CHECK FAILED headings | ANSI only for interactive TTY, removable with `--no-color` or `NO_COLOR` |
| `--format html` | navy/teal editorial style, responsive cards, system typography, auto light/dark mode, readable monospace blocks | local static HTML with escaped user data and **no scripts** |

Color is never the only status indicator. A result can be `EXECUTED` while its research/diagnostic meaning stays bounded; a human should still review the original evidence and source.

## Test and operational verification

```bash
python3 -m unittest tests.test_tool_cli -v
python3 tool_cli.py list
python3 tool_cli.py list --format html --output output/tool-catalog.html
```

These are executable instructions, **not a claim that any runner, GitHub Actions, security review or independent reproduction passed**. The adapter is optional and deliberately does not alter the canonical scientific/runtime paths.

For the three-repository chain, produce upstream artifact/claim/figure sidecars with each repository's native runtime first; then use these explicit read/transfer tools for portable handoffs. There are no hidden direct cross-repository imports, shared secrets, or automatic promotion of source evidence into scientific truth.
