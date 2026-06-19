#!/usr/bin/env python3
"""
AST 文档引擎 — 基于 Markdown AST 的文档操作
不依赖外部库，纯 Python 实现简易 AST 解析
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

class NodeType(Enum):
    DOCUMENT = "document"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST = "list"
    LIST_ITEM = "list_item"
    CODE_BLOCK = "code_block"
    TABLE = "table"
    TABLE_ROW = "table_row"
    TABLE_CELL = "table_cell"
    EMPHASIS = "emphasis"
    STRONG = "strong"
    LINK = "link"
    TEXT = "text"
    INLINE_CODE = "inline_code"
    BLOCKQUOTE = "blockquote"
    THEMATIC_BREAK = "thematic_break"

@dataclass
class ASTNode:
    type: NodeType
    content: str = ""
    level: int = 0
    children: List['ASTNode'] = field(default_factory=list)
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        return {
            "type": self.type.value,
            "content": self.content,
            "level": self.level,
            "attributes": self.attributes,
            "children": [c.to_dict() for c in self.children]
        }

class MarkdownParser:
    """简易 Markdown AST 解析器"""
    
    def parse(self, text: str) -> ASTNode:
        """将 Markdown 文本解析为 AST"""
        root = ASTNode(NodeType.DOCUMENT)
        lines = text.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # 空行跳过
            if not line.strip():
                i += 1
                continue
            
            # 标题
            if line.startswith('#'):
                match = re.match(r'^(#{1,6})\s+(.+)$', line)
                if match:
                    level = len(match.group(1))
                    content = match.group(2)
                    node = ASTNode(NodeType.HEADING, content=content, level=level)
                    root.children.append(node)
                    i += 1
                    continue
            
            # 代码块
            if line.startswith('```'):
                lang = line[3:].strip()
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].startswith('```'):
                    code_lines.append(lines[i])
                    i += 1
                i += 1  # 跳过 ```
                node = ASTNode(NodeType.CODE_BLOCK, content='\n'.join(code_lines))
                node.attributes['language'] = lang
                root.children.append(node)
                continue
            
            # 表格
            if '|' in line and i + 1 < len(lines) and '---' in lines[i + 1]:
                table_node = ASTNode(NodeType.TABLE)
                # 表头
                header_cells = [c.strip() for c in line.split('|')[1:-1]]
                header_row = ASTNode(NodeType.TABLE_ROW)
                for cell in header_cells:
                    header_row.children.append(ASTNode(NodeType.TABLE_CELL, content=cell))
                table_node.children.append(header_row)
                i += 2  # 跳过表头行和分隔行
                # 数据行
                while i < len(lines) and '|' in lines[i] and not lines[i].startswith('#'):
                    cells = [c.strip() for c in lines[i].split('|')[1:-1]]
                    row = ASTNode(NodeType.TABLE_ROW)
                    for cell in cells:
                        row.children.append(ASTNode(NodeType.TABLE_CELL, content=cell))
                    table_node.children.append(row)
                    i += 1
                root.children.append(table_node)
                continue
            
            # 列表
            if re.match(r'^(\s*)[-*+]\s+', line):
                list_node = ASTNode(NodeType.LIST)
                indent = len(re.match(r'^(\s*)', line).group(1))
                while i < len(lines):
                    match = re.match(r'^(\s*)[-*+]\s+(.+)$', lines[i])
                    if not match:
                        break
                    item = ASTNode(NodeType.LIST_ITEM, content=match.group(2))
                    list_node.children.append(item)
                    i += 1
                root.children.append(list_node)
                continue
            
            # 引用块
            if line.startswith('>'):
                quote_lines = []
                while i < len(lines) and lines[i].startswith('>'):
                    quote_lines.append(lines[i][1:].strip())
                    i += 1
                node = ASTNode(NodeType.BLOCKQUOTE, content='\n'.join(quote_lines))
                root.children.append(node)
                continue
            
            # 水平线
            if line.strip() == '---' or line.strip() == '***':
                root.children.append(ASTNode(NodeType.THEMATIC_BREAK))
                i += 1
                continue
            
            # 段落（默认）
            para_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('#') and not lines[i].startswith('```') and not lines[i].startswith('>') and not re.match(r'^(\s*)[-*+]\s+', lines[i]):
                para_lines.append(lines[i])
                i += 1
            
            content = ' '.join(para_lines)
            # 解析内联格式
            node = self._parse_inline(content)
            root.children.append(node)
        
        return root
    
    def _parse_inline(self, text: str) -> ASTNode:
        """解析内联格式（粗体、斜体、代码、链接）"""
        para = ASTNode(NodeType.PARAGRAPH)
        
        # 简单解析：按模式分割
        patterns = [
            (r'\*\*\*(.+?)\*\*\*', 'strong_emphasis'),
            (r'\*\*(.+?)\*\*', 'strong'),
            (r'\*(.+?)\*', 'emphasis'),
            (r'`(.+?)`', 'inline_code'),
            (r'\[(.+?)\]\((.+?)\)', 'link'),
        ]
        
        # 简化处理：先处理代码（避免干扰），然后其他
        # 实际实现应该用更复杂的递归下降解析，这里简化
        para.children.append(ASTNode(NodeType.TEXT, content=text))
        return para
    
    def render(self, node: ASTNode) -> str:
        """将 AST 渲染回 Markdown 文本"""
        lines = []
        
        for child in node.children:
            if child.type == NodeType.HEADING:
                lines.append(f"{'#' * child.level} {child.content}")
                lines.append('')
            elif child.type == NodeType.PARAGRAPH:
                if child.children:
                    text = ''.join(c.content for c in child.children if c.type == NodeType.TEXT)
                    lines.append(text)
                else:
                    lines.append(child.content)
                lines.append('')
            elif child.type == NodeType.CODE_BLOCK:
                lang = child.attributes.get('language', '')
                lines.append(f'```{lang}')
                lines.append(child.content)
                lines.append('```')
                lines.append('')
            elif child.type == NodeType.LIST:
                for item in child.children:
                    lines.append(f"- {item.content}")
                lines.append('')
            elif child.type == NodeType.TABLE:
                if child.children:
                    # 表头
                    header = child.children[0]
                    cells = [c.content for c in header.children]
                    lines.append('| ' + ' | '.join(cells) + ' |')
                    # 分隔
                    lines.append('| ' + ' | '.join(['---'] * len(cells)) + ' |')
                    # 数据
                    for row in child.children[1:]:
                        cells = [c.content for c in row.children]
                        lines.append('| ' + ' | '.join(cells) + ' |')
                lines.append('')
            elif child.type == NodeType.BLOCKQUOTE:
                for l in child.content.split('\n'):
                    lines.append(f'> {l}')
                lines.append('')
            elif child.type == NodeType.THEMATIC_BREAK:
                lines.append('---')
                lines.append('')
        
        return '\n'.join(lines)

class ASTEngine:
    """AST 文档操作引擎"""
    
    def __init__(self):
        self.parser = MarkdownParser()
    
    def load_document(self, path: str) -> ASTNode:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        return self.parser.parse(text)
    
    def save_document(self, node: ASTNode, path: str):
        text = self.parser.render(node)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    
    def find_nodes(self, node: ASTNode, node_type: NodeType) -> List[ASTNode]:
        """查找所有指定类型的节点"""
        results = []
        if node.type == node_type:
            results.append(node)
        for child in node.children:
            results.extend(self.find_nodes(child, node_type))
        return results
    
    def replace_node(self, parent: ASTNode, old: ASTNode, new: ASTNode):
        """替换子节点"""
        idx = parent.children.index(old)
        parent.children[idx] = new
    
    def insert_after(self, parent: ASTNode, target: ASTNode, new: ASTNode):
        """在目标节点后插入新节点"""
        idx = parent.children.index(target)
        parent.children.insert(idx + 1, new)
    
    def update_heading(self, node: ASTNode, old_title: str, new_title: str) -> bool:
        """更新指定标题的文本"""
        for child in node.children:
            if child.type == NodeType.HEADING and child.content == old_title:
                child.content = new_title
                return True
        return False
    
    def append_section(self, node: ASTNode, heading: str, content: str, level: int = 2):
        """在文档末尾添加新章节"""
        h = ASTNode(NodeType.HEADING, content=heading, level=level)
        p = ASTNode(NodeType.PARAGRAPH)
        p.children.append(ASTNode(NodeType.TEXT, content=content))
        node.children.append(h)
        node.children.append(p)

def demo():
    """演示 AST 引擎"""
    engine = ASTEngine()
    
    sample = """# 周报

## 本周概览

本周进展顺利。

## 详细数据

| 项目 | 进度 |
|------|------|
| A | 90% |
| B | 85% |

## 下周计划

- 完成项目 A
- 启动项目 C
"""
    
    ast = engine.parser.parse(sample)
    
    print("=== AST 解析演示 ===")
    print(f"文档节点数: {len(ast.children)}")
    
    headings = engine.find_nodes(ast, NodeType.HEADING)
    print(f"\n标题列表:")
    for h in headings:
        print(f"  {'#' * h.level} {h.content}")
    
    tables = engine.find_nodes(ast, NodeType.TABLE)
    print(f"\n表格数: {len(tables)}")
    
    # 修改标题
    engine.update_heading(ast, "本周概览", "本周概览（已更新）")
    
    # 添加新章节
    engine.append_section(ast, "风险项", "目前无重大风险。", level=2)
    
    # 渲染回文本
    rendered = engine.parser.render(ast)
    print(f"\n=== 渲染结果 ===")
    print(rendered[:500])

if __name__ == '__main__':
    demo()
