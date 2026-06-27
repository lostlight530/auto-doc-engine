#!/usr/bin/env python3
"""
数据绑定与渲染引擎 — 负责加载数据并结合 Jinja2 生成初始 Markdown
"""

import os
import json
import csv
from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader

class DataBindingEngine:
    def __init__(self, template_dir: str = "templates/jinja2"):
        self.template_dir = Path(template_dir)
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self._register_filters()

    def _register_filters(self):
        """注册自定义过滤器，比如自动生成表格的过滤器"""
        def format_table(data: list, headers: list) -> str:
            if not data:
                return "MISSING_DATA_FIELD"
            header_row = "| " + " | ".join(headers) + " |"
            sep_row = "|-" + "-|-".join(["" for _ in headers]) + "-|"
            rows = [header_row, sep_row]
            for item in data:
                # 假设 item 是字典，按 headers 取值；若是列表则按顺序
                if isinstance(item, dict):
                    row = "| " + " | ".join(str(item.get(h, '')) for h in headers) + " |"
                else:
                    row = "| " + " | ".join(str(x) for x in item) + " |"
                rows.append(row)
            return "\n".join(rows)

        self.env.filters['table'] = format_table

    def load_data(self, source_path: str) -> Dict[str, Any]:
        """加载数据源 (目前支持 JSON, CSV)"""
        path = Path(source_path)
        if not path.exists():
            return {}

        if path.suffix == '.json':
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif path.suffix == '.csv':
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return {'rows': list(reader)}
        return {}

    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        """渲染模板"""
        template = self.env.get_template(template_name)
        return template.render(**context)

def demo():
    engine = DataBindingEngine()

    # Mock data based on weekly_report.j2 structure
    context = {
        "period": "2024-W10",
        "generated_at": "2024-03-08",
        "tasks": [
            {"日期": "03-04", "项目": "API重构", "进度": "80", "风险": "无", "负责人": "Alice"},
            {"日期": "03-05", "项目": "前端迁移", "进度": "60", "风险": "延期", "负责人": "Bob"}
        ],
        "avg_progress": 70,
        "risks": [
            {"日期": "03-05", "项目": "前端迁移", "风险描述": "依赖库版本冲突", "建议": "降级依赖"}
        ],
        "next_plans": ["完成 API 文档", "修复迁移 Bug"]
    }

    # Create template for demo if not exists
    os.makedirs('templates/jinja2', exist_ok=True)

    rendered = engine.render('weekly_report.j2', context)
    print("=== 渲染结果 ===")
    print(rendered)

if __name__ == '__main__':
    demo()
