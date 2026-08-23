#!/usr/bin/env python3
"""Data binding and Jinja2 Markdown rendering.

The renderer keeps a deliberately small source contract: JSON, CSV and YAML
files are converted into a mapping that can be passed to Jinja2 templates.
SQLite/network adapters remain outside the implemented surface.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Dict

import yaml
from jinja2 import Environment, FileSystemLoader


class DataBindingEngine:
    """Load small structured data sources and render Markdown templates."""

    SUPPORTED_SUFFIXES = {".json", ".csv", ".yaml", ".yml"}

    def __init__(self, template_dir: str = "templates/jinja2"):
        self.template_dir = Path(template_dir)
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=False,
            keep_trailing_newline=True,
        )
        self._register_filters()

    def _register_filters(self) -> None:
        """Register the repository's Markdown-oriented Jinja2 filters."""

        def format_table(data: list, headers: list) -> str:
            if not data:
                return "MISSING_DATA_FIELD"
            header_row = "| " + " | ".join(str(h) for h in headers) + " |"
            sep_row = "| " + " | ".join("---" for _ in headers) + " |"
            rows = [header_row, sep_row]
            for item in data:
                if isinstance(item, dict):
                    row = "| " + " | ".join(str(item.get(h, "")) for h in headers) + " |"
                else:
                    row = "| " + " | ".join(str(x) for x in item) + " |"
                rows.append(row)
            return "\n".join(rows)

        def bullet_list(data: list) -> str:
            if not data:
                return "MISSING_DATA_FIELD"
            return "\n".join(f"- {item}" for item in data)

        self.env.filters["table"] = format_table
        self.env.filters["bullet_list"] = bullet_list

    def load_data(self, source_path: str, *, strict: bool = False) -> Dict[str, Any]:
        """Load JSON, CSV or YAML data into a Jinja2 context mapping.

        The historical non-strict behavior is preserved: a missing or
        unsupported source returns ``{}``. ``strict=True`` upgrades those
        conditions to explicit exceptions for callers that need fail-fast
        research pipelines.
        """
        path = Path(source_path)
        if not path.is_file():
            if strict:
                raise FileNotFoundError(source_path)
            return {}

        suffix = path.suffix.lower()
        if suffix not in self.SUPPORTED_SUFFIXES:
            if strict:
                raise ValueError(f"unsupported data source: {suffix or '<none>'}")
            return {}

        if suffix == ".json":
            with path.open("r", encoding="utf-8") as handle:
                loaded = json.load(handle)
        elif suffix == ".csv":
            with path.open("r", encoding="utf-8", newline="") as handle:
                return {"rows": list(csv.DictReader(handle))}
        else:
            with path.open("r", encoding="utf-8") as handle:
                loaded = yaml.safe_load(handle)

        if loaded is None:
            return {}
        if isinstance(loaded, dict):
            return loaded
        if isinstance(loaded, list):
            return {"rows": loaded}
        if strict:
            raise ValueError("top-level JSON/YAML data must be a mapping or list")
        return {"value": loaded}

    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """Render one template using the supplied context."""
        template = self.env.get_template(template_name)
        return template.render(**context)


def demo() -> None:
    engine = DataBindingEngine()
    context = {
        "period": "2026-W34",
        "generated_at": "2026-08-23",
        "tasks": [
            {"日期": "08-22", "项目": "证据整理", "进度": "80", "风险": "无", "负责人": "Alice"},
            {"日期": "08-23", "项目": "研究对象打包", "进度": "60", "风险": "依赖", "负责人": "Bob"},
        ],
        "avg_progress": 70,
        "risks": [{"日期": "08-23", "项目": "研究对象打包", "风险描述": "外部工具可选", "建议": "显式记录环境边界"}],
        "next_plans": ["补全来源元数据", "生成 RO-Crate 元数据"],
    }
    print("=== 渲染结果 ===")
    print(engine.render("weekly_report.j2", context))


if __name__ == "__main__":
    demo()
