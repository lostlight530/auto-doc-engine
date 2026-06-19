#!/usr/bin/env python3
"""
增量更新引擎 — 追踪文档变更，只更新差异部分
"""

import hashlib
import uuid
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass
from core.ast_engine import ASTNode, NodeType, MarkdownParser

@dataclass
class ChangeRecord:
    node_id: str
    node_type: str
    old_hash: str
    new_hash: str
    action: str  # add, modify, delete, unchanged
    old_content: str = ""
    new_content: str = ""

def compute_hash(text: str) -> str:
    return hashlib.sha256((text or "").encode('utf-8')).hexdigest()[:16]

def node_to_text(node: ASTNode) -> str:
    parser = MarkdownParser()
    return parser.render(ASTNode(NodeType.DOCUMENT, children=[node]))

class DiffTracker:
    def __init__(self, tracker_path: str = "incremental/diff_tracker.yaml"):
        self.tracker_path = Path(tracker_path)
        self.history = self._load_history()
    
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
        """生成带层级的唯一标识符"""
        return f"{parent_path}/{node.type.value}[{index}]"

    def _flatten_with_path(self, node: ASTNode, path: str = "root") -> Dict[str, ASTNode]:
        """展平 AST 树，并记录每个节点的结构路径"""
        nodes = {}
        # 忽略 DOCUMENT 根节点本身
        if node.type != NodeType.DOCUMENT:
            nodes[path] = node

        for i, child in enumerate(node.children):
            child_path = self._generate_node_path(child, path, i)
            nodes.update(self._flatten_with_path(child, child_path))

        return nodes

    def compute_diff(self, doc_id: str, old_ast: ASTNode, new_ast: ASTNode) -> List[ChangeRecord]:
        """
        计算两个 AST 间的差异。
        优化：通过节点路径比对，解决相同内容哈希碰撞的问题。
        """
        changes = []
        
        old_nodes = self._flatten_with_path(old_ast)
        new_nodes = self._flatten_with_path(new_ast)
        
        all_paths = set(old_nodes.keys()) | set(new_nodes.keys())
        
        for path in all_paths:
            if path in old_nodes and path in new_nodes:
                old_text = node_to_text(old_nodes[path])
                new_text = node_to_text(new_nodes[path])
                old_hash = compute_hash(old_text)
                new_hash = compute_hash(new_text)
                
                if old_hash != new_hash:
                    changes.append(ChangeRecord(
                        node_id=path,
                        node_type=old_nodes[path].type.value,
                        old_hash=old_hash,
                        new_hash=new_hash,
                        action='modify',
                        old_content=old_text,
                        new_content=new_text
                    ))
                else:
                    changes.append(ChangeRecord(
                        node_id=path,
                        node_type=old_nodes[path].type.value,
                        old_hash=old_hash,
                        new_hash=new_hash,
                        action='unchanged'
                    ))
            elif path in new_nodes:
                new_text = node_to_text(new_nodes[path])
                changes.append(ChangeRecord(
                    node_id=path,
                    node_type=new_nodes[path].type.value,
                    old_hash='',
                    new_hash=compute_hash(new_text),
                    action='add',
                    new_content=new_text
                ))
            else:
                old_text = node_to_text(old_nodes[path])
                changes.append(ChangeRecord(
                    node_id=path,
                    node_type=old_nodes[path].type.value,
                    old_hash=compute_hash(old_text),
                    new_hash='',
                    action='delete',
                    old_content=old_text
                ))
        
        return changes
    
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
            'changes': [
                {
                    'node_id': c.node_id,
                    'type': c.node_type,
                    'action': c.action,
                    'old_hash': c.old_hash,
                    'new_hash': c.new_hash
                }
                for c in changes if c.action != 'unchanged' # 只记录变更，减小体积
            ]
        }
        
        self.history[doc_id].append(record)
        # 限制历史记录条数，防止 yaml 过大
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
    
    tracker = DiffTracker()
    changes = tracker.compute_diff('weekly_report', old_ast, new_ast)
    
    print("=== 增量更新演示 ===")
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
