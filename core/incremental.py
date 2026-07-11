#!/usr/bin/env python3
"""
增量更新引擎 — 追踪文档变更，只更新差异部分
Enhanced: Myers O(ND) diff, xxhash caching, async support, YAML history
"""

import asyncio
import hashlib
import uuid
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from core.ast_engine import ASTNode, NodeType, MarkdownParser

logger = __import__('logging').getLogger('incremental')


def compute_hash(text: str) -> str:
    try:
        import xxhash
        return xxhash.xxh64((text or "").encode('utf-8')).hexdigest()
    except ImportError:
        return hashlib.sha256((text or "").encode('utf-8')).hexdigest()[:16]


def node_to_text(node: ASTNode) -> str:
    parser = MarkdownParser()
    return parser.render(ASTNode(NodeType.DOCUMENT, children=[node]))


@dataclass
class ChangeRecord:
    node_id: str
    node_type: str
    old_hash: str
    new_hash: str
    action: str  # add, modify, delete, unchanged
    old_content: str = ""
    new_content: str = ""

    def to_dict(self) -> dict:
        return {
            'node_id': self.node_id,
            'node_type': self.node_type,
            'old_hash': self.old_hash,
            'new_hash': self.new_hash,
            'action': self.action,
        }


class MyersDiff:
    """Myers O(ND) diff algorithm implementation"""

    def __init__(self):
        pass

    def diff(self, old_items: List[str], new_items: List[str]) -> List[tuple]:
        """
        Myers diff algorithm O(ND)
        Returns list of (action, old_index, new_index) tuples
        """
        n, m = len(old_items), len(new_items)
        if n == 0:
            return [('insert', None, j) for j in range(m)]
        if m == 0:
            return [('delete', i, None) for i in range(n)]

        max_d = n + m
        v = {1: 0}
        trace = []

        for d in range(max_d + 1):
            trace.append(dict(v))
            for k in range(-d, d + 1, 2):
                if k == -d or (k != d and v.get(k - 1, 0) < v.get(k + 1, 0)):
                    x = v.get(k + 1, 0)
                else:
                    x = v.get(k - 1, 0) + 1
                y = x - k

                while x < n and y < m and old_items[x] == new_items[y]:
                    x += 1
                    y += 1

                v[k] = x
                if x >= n and y >= m:
                    return self._backtrack(trace, old_items, new_items, d, k)

        return self._legacy_diff(old_items, new_items)

    def _backtrack(self, trace, old_items, new_items, d, k):
        """Backtrack to find the edit script"""
        edits = []
        x, y = len(old_items), len(new_items)

        for d_idx in range(d, -1, -1):
            v = trace[d_idx]
            if k == -d_idx or (k != d_idx and v.get(k - 1, 0) < v.get(k + 1, 0)):
                prev_k = k + 1
            else:
                prev_k = k - 1

            prev_x = v.get(prev_k, 0)
            prev_y = prev_x - prev_k

            while x > prev_x and y > prev_y:
                x -= 1
                y -= 1
                edits.append(('equal', x, y))

            if d_idx > 0:
                if x == prev_x:
                    edits.append(('insert', None, y - 1))
                    y -= 1
                else:
                    edits.append(('delete', x - 1, None))
                    x -= 1

            k = prev_k

        edits.reverse()
        return edits

    def _legacy_diff(self, old_items, new_items):
        """Fallback to legacy difflib"""
        import difflib
        sm = difflib.SequenceMatcher(None, old_items, new_items)
        edits = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                for i, j in zip(range(i1, i2), range(j1, j2)):
                    edits.append(('equal', i, j))
            elif tag == 'insert':
                for j in range(j1, j2):
                    edits.append(('insert', None, j))
            elif tag == 'delete':
                for i in range(i1, i2):
                    edits.append(('delete', i, None))
            elif tag == 'replace':
                for i in range(i1, i2):
                    edits.append(('delete', i, None))
                for j in range(j1, j2):
                    edits.append(('insert', None, j))
        return edits


class DiffTracker:
    """Enhanced diff tracker with Myers algorithm and async support"""

    def __init__(self, tracker_path: str = "incremental/diff_tracker.yaml",
                 algorithm: str = 'myers'):
        self.tracker_path = Path(tracker_path)
        self.history = self._load_history()
        self.algorithm = algorithm
        self._myers = MyersDiff()

    def _load_history(self) -> Dict:
        if self.tracker_path.exists():
            import yaml
            with open(self.tracker_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        return {}

    def _save_history(self):
        import yaml
        self.tracker_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.tracker_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.history, f, allow_unicode=True, sort_keys=False)

    def _generate_node_path(self, node: ASTNode, parent_path: str, index: int) -> str:
        return f"{parent_path}/{node.type.value}[{index}]"

    def _flatten_with_path(self, node: ASTNode, path: str = "root") -> Dict[str, ASTNode]:
        nodes = {}
        if node.type != NodeType.DOCUMENT:
            nodes[path] = node
        for i, child in enumerate(node.children):
            child_path = self._generate_node_path(child, path, i)
            nodes.update(self._flatten_with_path(child, child_path))
        return nodes

    def _compute_sigs(self, children: List[ASTNode]) -> List[str]:
        return [c.compute_hash() for c in children]

    def compute_diff(self, doc_id: str, old_ast: ASTNode, new_ast: ASTNode) -> List[ChangeRecord]:
        """Compute diff using Myers algorithm"""
        def diff_recursive(old_node: ASTNode, new_node: ASTNode, path: str = "root") -> List[ChangeRecord]:
            changes = []
            old_children = old_node.children
            new_children = new_node.children

            old_sigs = self._compute_sigs(old_children)
            new_sigs = self._compute_sigs(new_children)

            if self.algorithm == 'myers':
                edits = self._myers.diff(old_sigs, new_sigs)
            else:
                edits = self._myers._legacy_diff(old_sigs, new_sigs)

            for action, old_idx, new_idx in edits:
                if action == 'equal':
                    i, j = old_idx, new_idx
                    child_path = f"{path}/{old_children[i].type.value}[{j}]"
                    changes.append(ChangeRecord(
                        node_id=child_path,
                        node_type=old_children[i].type.value,
                        old_hash=old_sigs[i],
                        new_hash=new_sigs[j],
                        action='unchanged'
                    ))
                    changes.extend(diff_recursive(old_children[i], new_children[j], child_path))

                elif action == 'insert':
                    j = new_idx
                    child_path = f"{path}/{new_children[j].type.value}[{j}]"
                    new_text = node_to_text(new_children[j])
                    changes.append(ChangeRecord(
                        node_id=child_path,
                        node_type=new_children[j].type.value,
                        old_hash='',
                        new_hash=new_sigs[j],
                        action='add',
                        new_content=new_text
                    ))
                    self._add_all_children(new_children[j], child_path, changes)

                elif action == 'delete':
                    i = old_idx
                    child_path = f"{path}/{old_children[i].type.value}[{i}]"
                    old_text = node_to_text(old_children[i])
                    changes.append(ChangeRecord(
                        node_id=child_path,
                        node_type=old_children[i].type.value,
                        old_hash=old_sigs[i],
                        new_hash='',
                        action='delete',
                        old_content=old_text
                    ))
                    self._del_all_children(old_children[i], child_path, changes)

            return changes

        return diff_recursive(old_ast, new_ast)

    async def compute_diff_async(self, doc_id: str, old_ast: ASTNode, new_ast: ASTNode) -> List[ChangeRecord]:
        """Async wrapper for compute_diff"""
        return await asyncio.get_event_loop().run_in_executor(
            None, self.compute_diff, doc_id, old_ast, new_ast
        )

    def _add_all_children(self, node: ASTNode, path: str, changes: List[ChangeRecord]):
        for k, child in enumerate(node.children):
            cp = f"{path}/{child.type.value}[{k}]"
            text = node_to_text(child)
            changes.append(ChangeRecord(
                node_id=cp,
                node_type=child.type.value,
                old_hash='',
                new_hash=compute_hash(text),
                action='add',
                new_content=text
            ))
            self._add_all_children(child, cp, changes)

    def _del_all_children(self, node: ASTNode, path: str, changes: List[ChangeRecord]):
        for k, child in enumerate(node.children):
            cp = f"{path}/{child.type.value}[{k}]"
            text = node_to_text(child)
            changes.append(ChangeRecord(
                node_id=cp,
                node_type=child.type.value,
                old_hash=compute_hash(text),
                new_hash='',
                action='delete',
                old_content=text
            ))
            self._del_all_children(child, cp, changes)

    def record_generation(self, doc_id: str, template: str, data_source: str,
                         changes: List[ChangeRecord], output_path: str):
        if doc_id not in self.history:
            self.history[doc_id] = []

        import datetime
        record = {
            'timestamp': datetime.datetime.now().isoformat(),
            'template': template,
            'data_source': data_source,
            'output': output_path,
            'total_nodes': len(changes),
            'modified': sum(1 for c in changes if c.action == 'modify'),
            'added': sum(1 for c in changes if c.action == 'add'),
            'deleted': sum(1 for c in changes if c.action == 'delete'),
            'unchanged': sum(1 for c in changes if c.action == 'unchanged'),
            'changes': [c.to_dict() for c in changes if c.action != 'unchanged']
        }

        self.history[doc_id].append(record)
        if len(self.history[doc_id]) > 50:
            self.history[doc_id] = self.history[doc_id][-50:]

        self._save_history()
        return record


def demo():
    parser = MarkdownParser()

    old_doc = """# 周报
## 本周概览
进展顺利。
## 数据
| 项目 | 进度 |
|------|------|
| A | 80% |
"""
    new_doc = """# 周报
## 本周概览
进展顺利，完成里程碑。
## 数据
| 项目 | 进度 |
|------|------|
| A | 90% |
| B | 70% |
"""

    old_ast = parser.parse(old_doc)
    new_ast = parser.parse(new_doc)

    tracker = DiffTracker(algorithm='myers')
    changes = tracker.compute_diff('weekly_report', old_ast, new_ast)

    print("=== 增量更新演示 (Myers Diff) ===")
    print(f"总节点比对数: {len(changes)}")
    print(f"\n变更详情:")
    for c in changes:
        if c.action != 'unchanged':
            print(f"  {c.action.upper():8s} [{c.node_type:12s}] {c.node_id}")

    record = tracker.record_generation(
        'weekly_report', 'templates/weekly_report.j2',
        'data/weekly.csv', changes, 'output/weekly_report.md'
    )

    print(f"\n生成记录汇总:")
    print(f"  修改: {record['modified']}")
    print(f"  新增: {record['added']}")
    print(f"  删除: {record['deleted']}")
    print(f"  未变: {record['unchanged']}")


if __name__ == '__main__':
    demo()
