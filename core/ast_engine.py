#!/usr/bin/env python3
"""
AST 文档操作引擎 — 借助 mistune 实现健壮的解析和渲染
"""

import re
from pathlib import Path
from enum import Enum
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
import mistune

class NodeType(Enum):
    DOCUMENT = 'document'
    HEADING = 'heading'
    PARAGRAPH = 'paragraph'
    TEXT = 'text'
    CODE_BLOCK = 'code_block'
    INLINE_CODE = 'inline_code'
    LIST = 'list'
    LIST_ITEM = 'list_item'
    TABLE = 'table'
    TABLE_ROW = 'table_row'
    TABLE_CELL = 'table_cell'
    BLOCKQUOTE = 'blockquote'
    THEMATIC_BREAK = 'thematic_break'
    STRONG = 'strong'
    EMPHASIS = 'emphasis'
    LINK = 'link'
    BLANK_LINE = 'blank_line'

@dataclass
class ASTNode:
    type: NodeType
    content: Optional[str] = None
    level: Optional[int] = None
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
    """基于 mistune 的 Markdown AST 解析器"""
    
    def __init__(self):
        self.markdown = mistune.create_markdown(renderer='ast', plugins=['table', 'strikethrough'])

    def _map_mistune_node(self, node: dict) -> ASTNode:
        t = node['type']
        children = []

        if 'children' in node and node['children']:
            for child in node['children']:
                mapped = self._map_mistune_node(child)
                if mapped:
                    children.append(mapped)

        if t == 'heading':
            return ASTNode(NodeType.HEADING, level=node.get('attrs', {}).get('level', 1), children=children)
        elif t == 'paragraph':
            return ASTNode(NodeType.PARAGRAPH, children=children)
        elif t == 'text':
            return ASTNode(NodeType.TEXT, content=node.get('raw', ''))
        elif t == 'block_code':
            attrs = node.get('attrs', {})
            return ASTNode(NodeType.CODE_BLOCK, content=node.get('raw', ''), attributes={'language': attrs.get('info', '')})
        elif t == 'codespan':
            return ASTNode(NodeType.INLINE_CODE, content=node.get('raw', ''))
        elif t == 'list':
            return ASTNode(NodeType.LIST, children=children, attributes={'ordered': node.get('attrs', {}).get('ordered', False)})
        elif t == 'list_item':
            return ASTNode(NodeType.LIST_ITEM, children=children)
        elif t == 'block_text': # list_item content wrapper in mistune 3
            return ASTNode(NodeType.TEXT, children=children, content=node.get('raw', ''))
        elif t == 'table':
            return ASTNode(NodeType.TABLE, children=children)
        elif t == 'table_head':
            row = ASTNode(NodeType.TABLE_ROW, children=children)
            row.attributes['is_head'] = True
            return row
        elif t == 'table_body':
            # This is a container, we flatten its rows in the `parse` method
            return ASTNode(NodeType.DOCUMENT, children=children) # placeholder
        elif t == 'table_row':
            return ASTNode(NodeType.TABLE_ROW, children=children)
        elif t == 'table_cell':
            return ASTNode(NodeType.TABLE_CELL, children=children)
        elif t == 'block_quote':
            return ASTNode(NodeType.BLOCKQUOTE, children=children)
        elif t == 'thematic_break':
            return ASTNode(NodeType.THEMATIC_BREAK)
        elif t == 'strong':
            return ASTNode(NodeType.STRONG, children=children)
        elif t == 'emphasis':
            return ASTNode(NodeType.EMPHASIS, children=children)
        elif t == 'link':
            return ASTNode(NodeType.LINK, children=children, attributes={'url': node.get('attrs', {}).get('url', '')})
        elif t == 'blank_line':
            return ASTNode(NodeType.BLANK_LINE)
        else:
            return ASTNode(NodeType.TEXT, content=node.get('raw', ''))

    def parse(self, text: str) -> ASTNode:
        mistune_ast = self.markdown(text)
        root = ASTNode(NodeType.DOCUMENT)
        
        for node in mistune_ast:
            t = node['type']
            if t == 'table':
                table_node = ASTNode(NodeType.TABLE)
                for child in node.get('children', []):
                    if child['type'] == 'table_head':
                        row = ASTNode(NodeType.TABLE_ROW)
                        row.attributes['is_head'] = True
                        for cell in child.get('children', []):
                            row.children.append(self._map_mistune_node(cell))
                        table_node.children.append(row)
                    elif child['type'] == 'table_body':
                        for row_data in child.get('children', []):
                            row = ASTNode(NodeType.TABLE_ROW)
                            for cell in row_data.get('children', []):
                                row.children.append(self._map_mistune_node(cell))
                            table_node.children.append(row)
                root.children.append(table_node)
            else:
                mapped = self._map_mistune_node(node)
                if mapped:
                    root.children.append(mapped)

        return root
    
    def render(self, node: ASTNode) -> str:
        if node.type == NodeType.DOCUMENT:
            return '\n'.join(self.render(c) for c in node.children)
        elif node.type == NodeType.HEADING:
            content = ''.join(self.render(c) for c in node.children)
            return f"{'#' * (node.level or 1)} {content}\n"
        elif node.type == NodeType.PARAGRAPH:
            content = ''.join(self.render(c) for c in node.children)
            return f"{content}\n"
        elif node.type == NodeType.TEXT:
            if node.children:
                return ''.join(self.render(c) for c in node.children)
            return node.content or ''
        elif node.type == NodeType.CODE_BLOCK:
            lang = node.attributes.get('language', '')
            return f"```{lang}\n{node.content or ''}```\n"
        elif node.type == NodeType.INLINE_CODE:
            return f"`{node.content or ''}`"
        elif node.type == NodeType.LIST:
            content = ''.join(self.render(c) for c in node.children)
            return f"{content}\n"
        elif node.type == NodeType.LIST_ITEM:
            content = ''.join(self.render(c) for c in node.children)
            return f"- {content}\n"
        elif node.type == NodeType.TABLE:
            lines = []
            for i, row in enumerate(node.children):
                cells = [self.render(c) for c in row.children]
                lines.append('| ' + ' | '.join(cells) + ' |')
                if i == 0 and row.attributes.get('is_head', False):
                    lines.append('|' + '|'.join(['---'] * len(cells)) + '|')
            return '\n'.join(lines) + '\n'
        elif node.type == NodeType.TABLE_ROW:
            return ""
        elif node.type == NodeType.TABLE_CELL:
            return ''.join(self.render(c) for c in node.children)
        elif node.type == NodeType.BLOCKQUOTE:
            lines = []
            for child in node.children:
                child_text = self.render(child)
                for line in child_text.split('\n'):
                    if line.strip():
                        lines.append(f"> {line}")
            return '\n'.join(lines) + '\n'
        elif node.type == NodeType.THEMATIC_BREAK:
            return "---\n"
        elif node.type == NodeType.STRONG:
            content = ''.join(self.render(c) for c in node.children)
            return f"**{content}**"
        elif node.type == NodeType.EMPHASIS:
            content = ''.join(self.render(c) for c in node.children)
            return f"*{content}*"
        elif node.type == NodeType.LINK:
            content = ''.join(self.render(c) for c in node.children)
            url = node.attributes.get('url', '')
            return f"[{content}]({url})"
        elif node.type == NodeType.BLANK_LINE:
            return ""
        
        return ""

class ASTEngine:
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
        results = []
        if node.type == node_type:
            results.append(node)
        for child in node.children:
            results.extend(self.find_nodes(child, node_type))
        return results
    
    def update_heading(self, node: ASTNode, old_title: str, new_title: str) -> bool:
        for child in node.children:
            if child.type == NodeType.HEADING:
                content = ''.join(c.content for c in child.children if c.type in (NodeType.TEXT, NodeType.STRONG, NodeType.EMPHASIS))
                if content == old_title:
                    child.children = [ASTNode(NodeType.TEXT, content=new_title)]
                    return True
        return False

def demo():
    engine = ASTEngine()
    sample = """# 周报

## 本周概览

本周**进展**顺利。

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
    headings = engine.find_nodes(ast, NodeType.HEADING)
    for h in headings:
        content = ''.join(c.content for c in h.children if c.type in (NodeType.TEXT, NodeType.STRONG, NodeType.EMPHASIS))
        print(f"  {'#' * h.level} {content}")

    tables = engine.find_nodes(ast, NodeType.TABLE)
    print(f"\n表格数: {len(tables)}")
    
    engine.update_heading(ast, "本周概览", "本周概览（已更新）")
    
    print("\n=== 渲染结果 ===")
    print(engine.parser.render(ast))

if __name__ == '__main__':
    demo()
