#!/usr/bin/env python3
"""Typed Markdown AST parsing and rendering on top of Mistune 3.x.

The AST is structural rather than byte-preserving. Unsupported block/inline
constructs fail explicitly instead of being silently flattened. Node signatures
use SHA-256 as local identity evidence; they are not semantic hashes.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional

import mistune


class NodeType(Enum):
    DOCUMENT = "document"
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    TEXT = "text"
    CODE_BLOCK = "code_block"
    INLINE_CODE = "inline_code"
    LIST = "list"
    LIST_ITEM = "list_item"
    TABLE = "table"
    TABLE_ROW = "table_row"
    TABLE_CELL = "table_cell"
    BLOCKQUOTE = "blockquote"
    THEMATIC_BREAK = "thematic_break"
    STRONG = "strong"
    EMPHASIS = "emphasis"
    STRIKETHROUGH = "strikethrough"
    LINK = "link"
    IMAGE = "image"
    SOFTBREAK = "softbreak"
    LINEBREAK = "linebreak"
    BLANK_LINE = "blank_line"


@dataclass
class ASTNode:
    type: NodeType
    content: Optional[str] = None
    level: Optional[int] = None
    children: List["ASTNode"] = field(default_factory=list)
    attributes: Dict[str, Any] = field(default_factory=dict)

    @property
    def signature(self) -> str:
        """Return a stable shallow SHA-256 identity for local comparisons."""
        payload = {
            "type": self.type.value,
            "content": self.content,
            "level": self.level,
            "attributes": self.attributes,
        }
        canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False, default=str)
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict:
        return {
            "type": self.type.value,
            "content": self.content,
            "level": self.level,
            "attributes": self.attributes,
            "children": [child.to_dict() for child in self.children],
        }


class MarkdownParser:
    """Mistune-backed parser for the repository's explicit Markdown subset."""

    def __init__(self):
        self.markdown = mistune.create_markdown(
            renderer="ast", plugins=["table", "strikethrough"]
        )

    def _map_mistune_node(self, node: dict) -> ASTNode:
        node_type = node["type"]
        children = [self._map_mistune_node(child) for child in node.get("children", [])]
        attrs = node.get("attrs", {}) or {}

        if node_type == "heading":
            return ASTNode(NodeType.HEADING, level=attrs.get("level", 1), children=children)
        if node_type == "paragraph":
            return ASTNode(NodeType.PARAGRAPH, children=children)
        if node_type == "text":
            return ASTNode(NodeType.TEXT, content=node.get("raw", ""))
        if node_type == "block_code":
            return ASTNode(
                NodeType.CODE_BLOCK,
                content=node.get("raw", ""),
                attributes={"language": attrs.get("info", "") or ""},
            )
        if node_type == "codespan":
            return ASTNode(NodeType.INLINE_CODE, content=node.get("raw", ""))
        if node_type == "list":
            return ASTNode(
                NodeType.LIST,
                children=children,
                attributes={
                    "ordered": bool(attrs.get("ordered", False)),
                    "start": attrs.get("start"),
                },
            )
        if node_type == "list_item":
            return ASTNode(NodeType.LIST_ITEM, children=children)
        if node_type == "block_text":
            return ASTNode(NodeType.TEXT, content=node.get("raw", ""), children=children)
        if node_type == "table":
            return ASTNode(NodeType.TABLE, children=children)
        if node_type == "table_head":
            return ASTNode(NodeType.TABLE_ROW, children=children, attributes={"is_head": True})
        if node_type == "table_body":
            return ASTNode(NodeType.DOCUMENT, children=children)
        if node_type == "table_row":
            return ASTNode(NodeType.TABLE_ROW, children=children)
        if node_type == "table_cell":
            return ASTNode(NodeType.TABLE_CELL, children=children, attributes=dict(attrs))
        if node_type == "block_quote":
            return ASTNode(NodeType.BLOCKQUOTE, children=children)
        if node_type == "thematic_break":
            return ASTNode(NodeType.THEMATIC_BREAK)
        if node_type == "strong":
            return ASTNode(NodeType.STRONG, children=children)
        if node_type == "emphasis":
            return ASTNode(NodeType.EMPHASIS, children=children)
        if node_type == "strikethrough":
            return ASTNode(NodeType.STRIKETHROUGH, children=children)
        if node_type == "link":
            return ASTNode(NodeType.LINK, children=children, attributes={"url": attrs.get("url", "")})
        if node_type == "image":
            return ASTNode(
                NodeType.IMAGE,
                children=children,
                attributes={"url": attrs.get("url", ""), "title": attrs.get("title")},
            )
        if node_type == "softbreak":
            return ASTNode(NodeType.SOFTBREAK)
        if node_type == "linebreak":
            return ASTNode(NodeType.LINEBREAK)
        if node_type == "blank_line":
            return ASTNode(NodeType.BLANK_LINE)
        raise ValueError(f"UNSUPPORTED_AST_NODE: {node_type}")

    def parse(self, text: str) -> ASTNode:
        """Parse Markdown into the repository AST."""
        mistune_ast = self.markdown(text)
        root = ASTNode(NodeType.DOCUMENT)
        for node in mistune_ast:
            if node["type"] != "table":
                root.children.append(self._map_mistune_node(node))
                continue
            table = ASTNode(NodeType.TABLE)
            for child in node.get("children", []):
                if child["type"] == "table_head":
                    row = ASTNode(NodeType.TABLE_ROW, attributes={"is_head": True})
                    row.children = [self._map_mistune_node(cell) for cell in child.get("children", [])]
                    table.children.append(row)
                elif child["type"] == "table_body":
                    for row_data in child.get("children", []):
                        row = ASTNode(NodeType.TABLE_ROW)
                        row.children = [
                            self._map_mistune_node(cell) for cell in row_data.get("children", [])
                        ]
                        table.children.append(row)
            root.children.append(table)
        return root

    def render(self, node: ASTNode) -> str:
        """Render the supported AST subset back to normalized Markdown."""
        if node.type == NodeType.DOCUMENT:
            return "\n".join(self.render(child) for child in node.children)
        if node.type == NodeType.HEADING:
            content = "".join(self.render(child) for child in node.children)
            return f"{'#' * (node.level or 1)} {content}\n"
        if node.type == NodeType.PARAGRAPH:
            return "".join(self.render(child) for child in node.children) + "\n"
        if node.type == NodeType.TEXT:
            return "".join(self.render(child) for child in node.children) if node.children else (node.content or "")
        if node.type == NodeType.CODE_BLOCK:
            language = node.attributes.get("language", "")
            content = node.content or ""
            if content and not content.endswith("\n"):
                content += "\n"
            return f"```{language}\n{content}```\n"
        if node.type == NodeType.INLINE_CODE:
            return f"`{node.content or ''}`"
        if node.type == NodeType.LIST:
            ordered = bool(node.attributes.get("ordered"))
            start = int(node.attributes.get("start") or 1)
            lines: List[str] = []
            for index, child in enumerate(node.children):
                content = self.render(child).strip()
                marker = f"{start + index}." if ordered else "-"
                lines.append(f"{marker} {content}")
            return "\n".join(lines) + "\n"
        if node.type == NodeType.LIST_ITEM:
            return "".join(self.render(child) for child in node.children).strip()
        if node.type == NodeType.TABLE:
            lines: List[str] = []
            for index, row in enumerate(node.children):
                cells = [self.render(cell) for cell in row.children]
                lines.append("| " + " | ".join(cells) + " |")
                if index == 0 and row.attributes.get("is_head", False):
                    lines.append("| " + " | ".join("---" for _ in cells) + " |")
            return "\n".join(lines) + "\n"
        if node.type == NodeType.TABLE_ROW:
            return ""
        if node.type == NodeType.TABLE_CELL:
            return "".join(self.render(child) for child in node.children)
        if node.type == NodeType.BLOCKQUOTE:
            body = "".join(self.render(child) for child in node.children).rstrip("\n")
            return "\n".join(f"> {line}" if line else ">" for line in body.splitlines()) + "\n"
        if node.type == NodeType.THEMATIC_BREAK:
            return "---\n"
        if node.type == NodeType.STRONG:
            return f"**{''.join(self.render(child) for child in node.children)}**"
        if node.type == NodeType.EMPHASIS:
            return f"*{''.join(self.render(child) for child in node.children)}*"
        if node.type == NodeType.STRIKETHROUGH:
            return f"~~{''.join(self.render(child) for child in node.children)}~~"
        if node.type == NodeType.LINK:
            content = "".join(self.render(child) for child in node.children)
            return f"[{content}]({node.attributes.get('url', '')})"
        if node.type == NodeType.IMAGE:
            alt = "".join(self.render(child) for child in node.children)
            url = node.attributes.get("url", "")
            title = node.attributes.get("title")
            suffix = f' "{title}"' if title else ""
            return f"![{alt}]({url}{suffix})"
        if node.type == NodeType.SOFTBREAK:
            return "\n"
        if node.type == NodeType.LINEBREAK:
            return "  \n"
        if node.type == NodeType.BLANK_LINE:
            return ""
        raise ValueError(f"UNSUPPORTED_AST_RENDER_NODE: {node.type.value}")


class ASTEngine:
    """File-oriented convenience wrapper around ``MarkdownParser``."""

    def __init__(self):
        self.parser = MarkdownParser()

    def load_document(self, path: str) -> ASTNode:
        return self.parser.parse(Path(path).read_text(encoding="utf-8"))

    def save_document(self, node: ASTNode, path: str) -> None:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(self.parser.render(node), encoding="utf-8")

    def find_nodes(self, node: ASTNode, node_type: NodeType) -> List[ASTNode]:
        results = [node] if node.type == node_type else []
        for child in node.children:
            results.extend(self.find_nodes(child, node_type))
        return results

    def _plain_text(self, node: ASTNode) -> str:
        if node.type == NodeType.TEXT and not node.children:
            return node.content or ""
        return "".join(self._plain_text(child) for child in node.children)

    def update_heading(self, node: ASTNode, old_title: str, new_title: str) -> bool:
        """Update the first heading whose recursively extracted text matches exactly."""
        for heading in self.find_nodes(node, NodeType.HEADING):
            if self._plain_text(heading) == old_title:
                heading.children = [ASTNode(NodeType.TEXT, content=new_title)]
                return True
        return False


def demo() -> None:
    engine = ASTEngine()
    sample = "# 周报\n\n## 本周概览\n\n本周**进展**顺利，也支持~~废弃文本~~。\n\n1. 记录证据\n2. 打包产物\n"
    ast = engine.parser.parse(sample)
    print("=== AST 解析演示 ===")
    for heading in engine.find_nodes(ast, NodeType.HEADING):
        print(f"  {'#' * (heading.level or 1)} {engine._plain_text(heading)}")
    engine.update_heading(ast, "本周概览", "本周概览（已更新）")
    print("\n=== 规范化渲染结果 ===")
    print(engine.parser.render(ast))


if __name__ == "__main__":
    demo()
