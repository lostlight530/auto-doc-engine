#!/usr/bin/env python3
"""Local Tool / CLI / agent-plan adapter for the repository's existing core.

This is a bounded JSON invocation protocol, NOT an MCP transport/server.
It does not invoke a language model or run arbitrary shell commands.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

REPOSITORY = "auto-doc-engine"
PROFILE = REPOSITORY + "/tool-execution"
TOOL_DEFINITIONS = [
    {
        "name": "documents.doctor",
        "description": "Read-only structured Markdown document diagnostics from canonical Doctor.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "docs_dir": {
                    "type": "string"
                },
                "with_readability": {
                    "type": "boolean"
                }
            },
            "required": [
                "docs_dir"
            ],
            "additionalProperties": false
        }
    },
    {
        "name": "artifact.lineage",
        "description": "Create an in-memory typed lineage record from an existing artifact-record sidecar; never infer validity.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "artifact_record_path": {
                    "type": "string"
                },
                "relations": {
                    "type": "array",
                    "items": {
                        "type": "object"
                    }
                }
            },
            "required": [
                "artifact_record_path"
            ],
            "additionalProperties": false
        }
    }
]


def _digest(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":"), default=str).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _validate_args(name: str, args: Any) -> None:
    spec = next((item for item in TOOL_DEFINITIONS if item["name"] == name), None)
    if spec is None:
        raise ValueError(f"tool not allowlisted: {name}")
    if not isinstance(args, dict):
        raise TypeError("tool arguments must be a JSON object")
    schema = spec["inputSchema"]
    unknown = set(args) - set(schema["properties"])
    if unknown:
        raise ValueError(f"unknown tool arguments: {sorted(unknown)}")
    missing = [key for key in schema["required"] if key not in args]
    if missing:
        raise ValueError(f"missing required arguments: {missing}")
    types = {"string": str, "boolean": bool, "array": list, "object": dict}
    for key, value in args.items():
        kind = schema["properties"][key]["type"]
        if not isinstance(value, types[kind]):
            raise TypeError(f"{key} must be {kind}")
        if kind == "string" and not value.strip():
            raise ValueError(f"{key} must be nonempty")


def _dispatch(name: str, args: dict) -> dict:

    if name == "documents.doctor":
        from core.doctor import run_doctor
        directory = Path(args["docs_dir"])
        if not directory.is_dir():
            raise FileNotFoundError(f"Markdown root does not exist: {directory}")
        root = directory.resolve()
        for file in directory.rglob("*.md"):
            if not file.resolve().is_relative_to(root):
                raise ValueError(f"Markdown input escapes docs_dir: {file}")
        report = run_doctor(str(directory), with_readability=args.get("with_readability", False))
        data = report.to_dict()
        data["evaluation_status"] = "failed" if report.errors() else ("observations" if report.warnings() else "clean")
        return data
    if name == "artifact.lineage":
        from core.artifact_lineage import build_artifact_lineage
        relations = args.get("relations", [])
        if not isinstance(relations, list):
            raise ValueError("relations must be an array")
        pairs = []
        for item in relations:
            if not isinstance(item, dict) or set(item) != {"relation", "target"}:
                raise ValueError("each relation must contain only relation and target strings")
            if not isinstance(item["relation"], str) or not isinstance(item["target"], str):
                raise ValueError("relation and target must be strings")
            pairs.append((item["relation"], item["target"]))
        return build_artifact_lineage(args["artifact_record_path"], relations=pairs)
    raise ValueError(f"tool not allowlisted: {name}")


def invoke(name: str, args: Any) -> dict:
    """One typed receipt: local invocation result, not a truth verdict."""
    receipt = {
        "profile": PROFILE,
        "repository": REPOSITORY,
        "tool": name,
        "input_sha256": _digest(args),
        "status": "failed",
        "assertion_basis": "local-tool-invocation",
        "scientific_validity_claim": False,
        "independent_reproduction_claim": False,
    }
    try:
        _validate_args(name, args)
        receipt["output"] = _dispatch(name, args)
        receipt["status"] = "success"
    except (OSError, ValueError, TypeError, KeyError, ImportError) as exc:
        receipt["error"] = {"type": type(exc).__name__, "message": str(exc)}
    return receipt


def run_plan(plan: Any) -> dict:
    """Bounded deterministic coordinator; no model or implicit approval."""
    if not isinstance(plan, dict) or set(plan) != {"steps"}:
        raise ValueError("plan must contain only a steps array")
    steps = plan["steps"]
    if not isinstance(steps, list) or not 1 <= len(steps) <= 32:
        raise ValueError("plan must contain between 1 and 32 steps")
    ids: set[str] = set()
    results = []
    for index, step in enumerate(steps):
        if not isinstance(step, dict) or set(step) != {"id", "tool", "arguments"}:
            raise ValueError(f"step[{index}] requires id, tool and arguments")
        step_id = step["id"]
        if not isinstance(step_id, str) or not step_id or step_id in ids:
            raise ValueError(f"step[{index}] has blank or duplicate id")
        if not isinstance(step["tool"], str):
            raise ValueError(f"step[{index}] tool must be a string")
        ids.add(step_id)
        receipt = invoke(step["tool"], step["arguments"])
        results.append({"id": step_id, "receipt": receipt})
        if receipt["status"] != "success":
            break
    return {
        "profile": REPOSITORY + "/agent-plan",
        "repository": REPOSITORY,
        "plan_sha256": _digest(plan),
        "status": "failed" if results[-1]["receipt"]["status"] != "success" else "success",
        "completed_steps": len(results),
        "requested_steps": len(steps),
        "steps": results,
        "execution_mode": "deterministic-declared-plan-no-model",
        "scientific_validity_claim": False,
    }


def _read_input(path: str) -> Any:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def _write_atomic(path: str, content: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=str(target.parent), prefix="." + target.name + ".")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Local bounded Tool/CLI/agent-plan interface")
    parser.add_argument("command", choices=("list", "call", "agent"))
    parser.add_argument("tool", nargs="?", help="allowlisted tool for call")
    parser.add_argument("--input", default="-", help="JSON file or stdin (-)")
    parser.add_argument("--output", help="optional explicit atomic JSON receipt output")
    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            if args.tool:
                raise ValueError("list takes no tool argument")
            result = {"profile": REPOSITORY + "/tool-catalog", "tools": TOOL_DEFINITIONS}
        elif args.command == "call":
            if not args.tool:
                raise ValueError("call requires a tool name")
            result = invoke(args.tool, _read_input(args.input))
        else:
            if args.tool:
                raise ValueError("agent takes no tool argument")
            result = run_plan(_read_input(args.input))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        result = {"profile": PROFILE, "status": "failed",
                  "error": {"type": type(exc).__name__, "message": str(exc)}}
    rendered = json.dumps(result, indent=2, ensure_ascii=False, default=str) + "\n"
    if args.output:
        _write_atomic(args.output, rendered)
    sys.stdout.write(rendered)
    return 1 if result.get("status") == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
