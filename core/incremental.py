#!/usr/bin/env python3
"""
增量更新引擎 — 追踪文档变更，只更新差异部分
"""

import hashlib
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
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
    """计算文本的 SHA-256 哈希"""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]

def node_to_text(node: ASTNode) -> str:
    """将 AST 节点转换为可比较的文本表示"""
    parser = MarkdownParser()
    return parser.render(ASTNode(NodeType.DOCUMENT, children=[node]))

class DiffTracker:
    """变更追踪器"""
    
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
    
    def compute_diff(self, doc_id: str, old_ast: ASTNode, new_ast: ASTNode) -> List[ChangeRecord]:
        """计算两个 AST 间的差异"""
        changes = []
        
        old_nodes = {self._node_id(n): n for n in self._flatten(old_ast)}
        new_nodes = {self._node_id(n): n for n in self._flatten(new_ast)}
        
        all_ids = set(old_nodes.keys()) | set(new_nodes.keys())
        
        for nid in all_ids:
            if nid in old_nodes and nid in new_nodes:
                old_text = node_to_text(old_nodes[nid])
                new_text = node_to_text(new_nodes[nid])
                old_hash = compute_hash(old_text)
                new_hash = compute_hash(new_text)
                
                if old_hash != new_hash:
                    changes.append(ChangeRecord(
                        node_id=nid,
                        node_type=old_nodes[nid].type.value,
                        old_hash=old_hash,
                        new_hash=new_hash,
                        action='modify',
                        old_content=old_text,
                        new_content=new_text
                    ))
                else:
                    changes.append(ChangeRecord(
                        node_id=nid,
                        node_type=old_nodes[nid].type.value,
                        old_hash=old_hash,
                        new_hash=new_hash,
                        action='unchanged'
                    ))
            elif nid in new_nodes:
                new_text = node_to_text(new_nodes[nid])
                changes.append(ChangeRecord(
                    node_id=nid,
                    node_type=new_nodes[nid].type.value,
                    old_hash='',
                    new_hash=compute_hash(new_text),
                    action='add',
                    new_content=new_text
                ))
            else:
                old_text = node_to_text(old_nodes[nid])
                changes.append(ChangeRecord(
                    node_id=nid,
                    node_type=old_nodes[nid].type.value,
                    old_hash=compute_hash(old_text),
                    new_hash='',
                    action='delete',
                    old_content=old_text
                ))
        
        return changes
    
    def _node_id(self, node: ASTNode) -> str:
        """为节点生成唯一标识（基于类型和内容哈希）"""
        content = node.content or ''
        level = node.level or 0
        return f"{node.type.value}:{level}:{compute_hash(content)[:8]}"
    
    def _flatten(self, node: ASTNode) -> List[ASTNode]:
        """扁平化 AST"""
        result = [node]
        for child in node.children:
            result.extend(self._flatten(child))
        return result
    
    def record_generation(self, doc_id: str, template: str, data_source: str, 
                         changes: List[ChangeRecord], output_path: str):
        """记录一次生成事件"""
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
                for c in changes
            ]
        }
        
        self.history[doc_id].append(record)
        self._save_history()
        
        return record
    
    def get_history(self, doc_id: str) -> List[dict]:
        """获取文档的生成历史"""
        return self.history.get(doc_id, [])
    
    def has_changes(self, changes: List[ChangeRecord]) -> bool:
        """判断是否有实质性变更"""
        return any(c.action in ('add', 'modify', 'delete') for c in changes)

def demo():
    """演示增量更新"""
    from core.ast_engine import MarkdownParser
    
    parser = MarkdownParser()
    
    old_doc = """# 周报

## 本周概览

本周进展顺利。

## 数据

| 项目 | 进度 |
|------|------|
| A | 80% |
"""
    
    new_doc = """# 周报

## 本周概览

本周进展顺利，已完成里程碑。

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
    print(f"总节点数: {len(changes)}")
    print(f"\n变更详情:")
    for c in changes:
        if c.action != 'unchanged':
            print(f"  {c.action.upper():8s} [{c.node_type:12s}] {c.node_id[:30]}")
    
    # 记录生成
    record = tracker.record_generation(
        'weekly_report', 'templates/weekly_report.j2', 
        'data/weekly.csv', changes, 'output/weekly_report.md'
    )
    
    print(f"\n生成记录:")
    print(f"  修改: {record['modified']}")
    print(f"  新增: {record['added']}")
    print(f"  删除: {record['deleted']}")
    print(f"  未变: {record['unchanged']}")

if __name__ == '__main__':
    demo()
