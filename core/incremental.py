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
        重构：采用类似 React Virtual DOM 的同层递归比对（LCS算法），
        彻底解决文档中间插入节点导致的全局索引偏移问题。
        """
        import difflib

        def diff_ast_recursive(old_node: ASTNode, new_node: ASTNode, path: str = "root") -> List[ChangeRecord]:
            changes = []
            old_children = old_node.children
            new_children = new_node.children

            def get_sig(n: ASTNode):
                return compute_hash(node_to_text(n))

            old_sigs = [get_sig(c) for c in old_children]
            new_sigs = [get_sig(c) for c in new_children]

            sm = difflib.SequenceMatcher(None, old_sigs, new_sigs)

            for tag, i1, i2, j1, j2 in sm.get_opcodes():
                if tag == 'equal':
                    for i, j in zip(range(i1, i2), range(j1, j2)):
                        child_path = f"{path}/{old_children[i].type.value}[{j}]"
                        changes.append(ChangeRecord(
                            node_id=child_path,
                            node_type=old_children[i].type.value,
                            old_hash=old_sigs[i],
                            new_hash=new_sigs[j],
                            action='unchanged'
                        ))
                        # 递归，即使本身相同，子树也会被当做 unchanged 记录
                        changes.extend(diff_ast_recursive(old_children[i], new_children[j], child_path))

                elif tag == 'insert':
                    for j in range(j1, j2):
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
                        def _add_all_children(n, current_path):
                            for k, child in enumerate(n.children):
                                cp = f"{current_path}/{child.type.value}[{k}]"
                                text = node_to_text(child)
                                changes.append(ChangeRecord(
                                    node_id=cp,
                                    node_type=child.type.value,
                                    old_hash='',
                                    new_hash=compute_hash(text),
                                    action='add',
                                    new_content=text
                                ))
                                _add_all_children(child, cp)
                        _add_all_children(new_children[j], child_path)

                elif tag == 'delete':
                    for i in range(i1, i2):
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
                        def _del_all_children(n, current_path):
                            for k, child in enumerate(n.children):
                                cp = f"{current_path}/{child.type.value}[{k}]"
                                text = node_to_text(child)
                                changes.append(ChangeRecord(
                                    node_id=cp,
                                    node_type=child.type.value,
                                    old_hash=compute_hash(text),
                                    new_hash='',
                                    action='delete',
                                    old_content=text
                                ))
                                _del_all_children(child, cp)
                        _del_all_children(old_children[i], child_path)

                elif tag == 'replace':
                    min_len = min(i2 - i1, j2 - j1)
                    for k in range(min_len):
                        i = i1 + k
                        j = j1 + k
                        child_path = f"{path}/{new_children[j].type.value}[{j}]"

                        if old_children[i].type == new_children[j].type:
                            old_text = node_to_text(old_children[i])
                            new_text = node_to_text(new_children[j])
                            changes.append(ChangeRecord(
                                node_id=child_path,
                                node_type=new_children[j].type.value,
                                old_hash=old_sigs[i],
                                new_hash=new_sigs[j],
                                action='modify',
                                old_content=old_text,
                                new_content=new_text
                            ))
                            changes.extend(diff_ast_recursive(old_children[i], new_children[j], child_path))
                        else:
                            # 类别不同，视作先删后增
                            del_path = f"{path}/{old_children[i].type.value}[{i}]"
                            changes.append(ChangeRecord(
                                node_id=del_path,
                                node_type=old_children[i].type.value,
                                old_hash=old_sigs[i],
                                new_hash='',
                                action='delete',
                                old_content=node_to_text(old_children[i])
                            ))
                            def _del_all_children(n, current_path):
                                for c_k, child in enumerate(n.children):
                                    cp = f"{current_path}/{child.type.value}[{c_k}]"
                                    text = node_to_text(child)
                                    changes.append(ChangeRecord(
                                        node_id=cp,
                                        node_type=child.type.value,
                                        old_hash=compute_hash(text),
                                        new_hash='',
                                        action='delete',
                                        old_content=text
                                    ))
                                    _del_all_children(child, cp)
                            _del_all_children(old_children[i], del_path)

                            changes.append(ChangeRecord(
                                node_id=child_path,
                                node_type=new_children[j].type.value,
                                old_hash='',
                                new_hash=new_sigs[j],
                                action='add',
                                new_content=node_to_text(new_children[j])
                            ))
                            def _add_all_children(n, current_path):
                                for c_k, child in enumerate(n.children):
                                    cp = f"{current_path}/{child.type.value}[{c_k}]"
                                    text = node_to_text(child)
                                    changes.append(ChangeRecord(
                                        node_id=cp,
                                        node_type=child.type.value,
                                        old_hash='',
                                        new_hash=compute_hash(text),
                                        action='add',
                                        new_content=text
                                    ))
                                    _add_all_children(child, cp)
                            _add_all_children(new_children[j], child_path)

                    for i in range(i1 + min_len, i2):
                        del_path = f"{path}/{old_children[i].type.value}[{i}]"
                        changes.append(ChangeRecord(
                            node_id=del_path,
                            node_type=old_children[i].type.value,
                            old_hash=old_sigs[i],
                            new_hash='',
                            action='delete',
                            old_content=node_to_text(old_children[i])
                        ))
                        def _del_all_children(n, current_path):
                            for c_k, child in enumerate(n.children):
                                cp = f"{current_path}/{child.type.value}[{c_k}]"
                                text = node_to_text(child)
                                changes.append(ChangeRecord(
                                    node_id=cp,
                                    node_type=child.type.value,
                                    old_hash=compute_hash(text),
                                    new_hash='',
                                    action='delete',
                                    old_content=text
                                ))
                                _del_all_children(child, cp)
                        _del_all_children(old_children[i], del_path)

                    for j in range(j1 + min_len, j2):
                        child_path = f"{path}/{new_children[j].type.value}[{j}]"
                        changes.append(ChangeRecord(
                            node_id=child_path,
                            node_type=new_children[j].type.value,
                            old_hash='',
                            new_hash=new_sigs[j],
                            action='add',
                            new_content=node_to_text(new_children[j])
                        ))
                        def _add_all_children(n, current_path):
                            for c_k, child in enumerate(n.children):
                                cp = f"{current_path}/{child.type.value}[{c_k}]"
                                text = node_to_text(child)
                                changes.append(ChangeRecord(
                                    node_id=cp,
                                    node_type=child.type.value,
                                    old_hash='',
                                    new_hash=compute_hash(text),
                                    action='add',
                                    new_content=text
                                ))
                                _add_all_children(child, cp)
                        _add_all_children(new_children[j], child_path)

            return changes

        return diff_ast_recursive(old_ast, new_ast)
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
