#!/usr/bin/env python3
"""Structural Markdown AST change detection and bounded generation history.

The diff engine uses normalized rendered subtree text plus SHA-256 identities
and sibling-sequence alignment. It reports add/modify/delete/unchanged records;
it is not a patch applier, merge engine, semantic-diff system or proof that
human edits are conflict-free.
"""

from __future__ import annotations

import datetime as dt
import difflib
import hashlib
import os
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.ast_engine import ASTNode, MarkdownParser, NodeType


@dataclass
class ChangeRecord:
    node_id: str
    node_type: str
    old_hash: str
    new_hash: str
    action: str  # add | modify | delete | unchanged
    old_content: str = ""
    new_content: str = ""


def compute_hash(text: str) -> str:
    """Return a compact SHA-256 identity for normalized subtree text."""
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()[:16]


def node_to_text(node: ASTNode) -> str:
    return MarkdownParser().render(ASTNode(NodeType.DOCUMENT, children=[node]))


class DiffTracker:
    """Detect structural changes and optionally persist small generation summaries."""

    def __init__(self, tracker_path: str = "incremental/diff_tracker.yaml"):
        self.tracker_path = Path(tracker_path)
        self.history = self._load_history()

    def _load_history(self) -> Dict:
        if not self.tracker_path.exists():
            return {}
        import yaml

        with self.tracker_path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        if not isinstance(data, dict):
            raise ValueError("diff tracker history must be a YAML mapping")
        return data

    def _save_history(self) -> None:
        """Atomically replace the YAML history file within its directory."""
        import yaml

        self.tracker_path.parent.mkdir(parents=True, exist_ok=True)
        rendered = yaml.safe_dump(self.history, allow_unicode=True, sort_keys=False)
        fd, temp_name = tempfile.mkstemp(
            prefix=f".{self.tracker_path.name}.",
            suffix=".tmp",
            dir=str(self.tracker_path.parent),
            text=True,
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(rendered)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_name, self.tracker_path)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)

    @staticmethod
    def _node_path(parent: str, node: ASTNode, index: int) -> str:
        return f"{parent}/{node.type.value}[{index}]"

    @staticmethod
    def _subtree_records(
        node: ASTNode,
        path: str,
        action: str,
    ) -> List[ChangeRecord]:
        text = node_to_text(node)
        digest = compute_hash(text)
        record = ChangeRecord(
            node_id=path,
            node_type=node.type.value,
            old_hash=digest if action == "delete" else "",
            new_hash=digest if action == "add" else "",
            action=action,
            old_content=text if action == "delete" else "",
            new_content=text if action == "add" else "",
        )
        records = [record]
        for index, child in enumerate(node.children):
            records.extend(
                DiffTracker._subtree_records(
                    child,
                    DiffTracker._node_path(path, child, index),
                    action,
                )
            )
        return records

    def compute_diff(
        self, doc_id: str, old_ast: ASTNode, new_ast: ASTNode
    ) -> List[ChangeRecord]:
        """Return a structural change report for two document ASTs.

        ``doc_id`` is accepted for API continuity; structural paths themselves
        remain rooted at ``root`` so existing consumers keep their identifiers.
        """
        del doc_id

        def recurse(old_node: ASTNode, new_node: ASTNode, path: str) -> List[ChangeRecord]:
            changes: List[ChangeRecord] = []
            old_children = old_node.children
            new_children = new_node.children
            old_text = [node_to_text(child) for child in old_children]
            new_text = [node_to_text(child) for child in new_children]
            old_hashes = [compute_hash(text) for text in old_text]
            new_hashes = [compute_hash(text) for text in new_text]
            matcher = difflib.SequenceMatcher(None, old_hashes, new_hashes, autojunk=False)

            for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                if tag == "equal":
                    for old_index, new_index in zip(range(i1, i2), range(j1, j2)):
                        old_child = old_children[old_index]
                        new_child = new_children[new_index]
                        child_path = self._node_path(path, new_child, new_index)
                        changes.append(
                            ChangeRecord(
                                node_id=child_path,
                                node_type=new_child.type.value,
                                old_hash=old_hashes[old_index],
                                new_hash=new_hashes[new_index],
                                action="unchanged",
                            )
                        )
                        changes.extend(recurse(old_child, new_child, child_path))
                    continue

                if tag == "insert":
                    for new_index in range(j1, j2):
                        child = new_children[new_index]
                        changes.extend(
                            self._subtree_records(
                                child,
                                self._node_path(path, child, new_index),
                                "add",
                            )
                        )
                    continue

                if tag == "delete":
                    for old_index in range(i1, i2):
                        child = old_children[old_index]
                        changes.extend(
                            self._subtree_records(
                                child,
                                self._node_path(path, child, old_index),
                                "delete",
                            )
                        )
                    continue

                # SequenceMatcher replacement: pair same-position nodes first,
                # then report unmatched tails as explicit subtree add/delete.
                pair_count = min(i2 - i1, j2 - j1)
                for offset in range(pair_count):
                    old_index = i1 + offset
                    new_index = j1 + offset
                    old_child = old_children[old_index]
                    new_child = new_children[new_index]
                    new_path = self._node_path(path, new_child, new_index)
                    if old_child.type == new_child.type:
                        changes.append(
                            ChangeRecord(
                                node_id=new_path,
                                node_type=new_child.type.value,
                                old_hash=old_hashes[old_index],
                                new_hash=new_hashes[new_index],
                                action="modify",
                                old_content=old_text[old_index],
                                new_content=new_text[new_index],
                            )
                        )
                        changes.extend(recurse(old_child, new_child, new_path))
                    else:
                        changes.extend(
                            self._subtree_records(
                                old_child,
                                self._node_path(path, old_child, old_index),
                                "delete",
                            )
                        )
                        changes.extend(self._subtree_records(new_child, new_path, "add"))

                for old_index in range(i1 + pair_count, i2):
                    child = old_children[old_index]
                    changes.extend(
                        self._subtree_records(
                            child,
                            self._node_path(path, child, old_index),
                            "delete",
                        )
                    )
                for new_index in range(j1 + pair_count, j2):
                    child = new_children[new_index]
                    changes.extend(
                        self._subtree_records(
                            child,
                            self._node_path(path, child, new_index),
                            "add",
                        )
                    )
            return changes

        return recurse(old_ast, new_ast, "root")

    def record_generation(
        self,
        doc_id: str,
        template: str,
        data_source: str,
        changes: List[ChangeRecord],
        output_path: str,
    ) -> dict:
        """Append one bounded generation summary and persist it atomically."""
        record = {
            "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
            "template": template,
            "data_source": data_source,
            "output": output_path,
            "total_nodes": len(changes),
            "modified": sum(item.action == "modify" for item in changes),
            "added": sum(item.action == "add" for item in changes),
            "deleted": sum(item.action == "delete" for item in changes),
            "unchanged": sum(item.action == "unchanged" for item in changes),
            "changes": [
                {
                    "node_id": item.node_id,
                    "type": item.node_type,
                    "action": item.action,
                    "old_hash": item.old_hash,
                    "new_hash": item.new_hash,
                }
                for item in changes
                if item.action != "unchanged"
            ],
            "semantics": "structural_change_report_not_merge",
        }
        self.history.setdefault(doc_id, []).append(record)
        self.history[doc_id] = self.history[doc_id][-50:]
        self._save_history()
        return record


def demo() -> None:
    parser = MarkdownParser()
    old_doc = "# 周报\n\n## 本周概览\n\n进展顺利。\n"
    new_doc = "# 周报\n\n## 本周概览\n\n进展顺利，完成里程碑。\n\n## 证据\n\n新增来源记录。\n"
    tracker = DiffTracker()
    changes = tracker.compute_diff("weekly_report", parser.parse(old_doc), parser.parse(new_doc))
    print("=== 结构差异演示 ===")
    for change in changes:
        if change.action != "unchanged":
            print(f"  {change.action.upper():8s} [{change.node_type:12s}] {change.node_id}")


if __name__ == "__main__":
    demo()
