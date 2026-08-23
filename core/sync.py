#!/usr/bin/env python3
"""Multi-format document synchronization with explicit dependency boundaries.

Markdown copying is implemented with the Python standard library so the core
path is cross-platform. Pandoc/XeLaTeX remain optional environment-dependent
converters. The engine can optionally package successful outputs with the
repository's RO-Crate 1.3 metadata exporter.
"""

from __future__ import annotations

import html as html_lib
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.ro_crate import write_ro_crate


@dataclass(frozen=True)
class SyncTarget:
    format: str
    extension: str
    command: List[str]
    enabled: bool = True
    requires: Optional[str] = None


class SyncEngine:
    """Synchronize one Markdown source into declared output formats."""

    TARGETS = {
        # Kept as a list for backwards-compatible public structure; copying is
        # performed internally rather than relying on a platform-specific `cp`.
        "markdown": SyncTarget("markdown", ".md", []),
        "html": SyncTarget(
            "html",
            ".html",
            ["pandoc", "{input}", "-o", "{output}", "-f", "markdown", "-t", "html", "--standalone"],
            requires="pandoc",
        ),
        "docx": SyncTarget(
            "docx",
            ".docx",
            ["pandoc", "{input}", "-o", "{output}", "-f", "markdown", "-t", "docx"],
            requires="pandoc",
        ),
        "pdf": SyncTarget(
            "pdf",
            ".pdf",
            ["pandoc", "{input}", "-o", "{output}", "-f", "markdown", "-t", "pdf", "--pdf-engine=xelatex"],
            requires="pandoc",
        ),
        "epub": SyncTarget(
            "epub",
            ".epub",
            ["pandoc", "{input}", "-o", "{output}", "-f", "markdown", "-t", "epub"],
            requires="pandoc",
        ),
    }

    def __init__(self, config_path: str = "sync/targets.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        import yaml

        if self.config_path.exists():
            with self.config_path.open("r", encoding="utf-8") as handle:
                return yaml.safe_load(handle) or {}
        return {"targets": ["markdown", "html"]}

    def _pandoc_command(self) -> str:
        return str(self.config.get("custom", {}).get("pandoc_path") or "pandoc")

    def check_availability(self, target: str) -> bool:
        """Return whether the target's declared external executable is available."""
        if target not in self.TARGETS:
            return False
        spec = self.TARGETS[target]
        if not spec.requires:
            return True
        executable = self._pandoc_command() if spec.requires == "pandoc" else spec.requires
        return shutil.which(executable) is not None

    def _build_command(
        self,
        target: str,
        input_path: Path,
        output_path: Path,
        reference_doc: Optional[str],
    ) -> List[str]:
        spec = self.TARGETS[target]
        cmd: List[str] = []
        for index, arg in enumerate(spec.command):
            if index == 0 and spec.requires == "pandoc":
                cmd.append(self._pandoc_command())
            elif arg == "{input}":
                cmd.append(str(input_path))
            elif arg == "{output}":
                cmd.append(str(output_path))
            elif arg == "{reference}" and reference_doc:
                cmd.append(reference_doc)
            elif "{" not in arg:
                cmd.append(arg)
        if target == "docx" and reference_doc:
            cmd.append(f"--reference-doc={reference_doc}")
        return cmd

    def _emit_ro_crate(
        self,
        output_dir: Path,
        results: Dict[str, str],
        *,
        crate_name: Optional[str] = None,
        crate_description: Optional[str] = None,
    ) -> None:
        config = self.config.get("research_object", {})
        payloads: List[str] = []
        for key, value in results.items():
            if key == "ro_crate" or value.startswith(("ERROR:", "WARN:")):
                continue
            path = Path(value)
            if path.is_file():
                try:
                    payloads.append(path.resolve().relative_to(output_dir.resolve()).as_posix())
                except ValueError:
                    continue
        if not payloads:
            results["ro_crate"] = "ERROR: no successful output artifacts to package"
            return
        try:
            crate_path = write_ro_crate(
                output_dir,
                payloads,
                name=crate_name or str(config.get("name") or "auto-doc-engine research artifact set"),
                description=crate_description
                or str(config.get("description") or "Document artifacts generated by auto-doc-engine."),
                authors=list(config.get("authors") or []),
                license_value=config.get("license"),
            )
            results["ro_crate"] = str(crate_path)
        except (OSError, ValueError) as exc:
            results["ro_crate"] = f"ERROR: {exc}"

    def sync(
        self,
        input_path: str,
        targets: Optional[List[str]] = None,
        output_dir: str = "output",
        reference_doc: Optional[str] = None,
        *,
        emit_ro_crate: Optional[bool] = None,
        crate_name: Optional[str] = None,
        crate_description: Optional[str] = None,
    ) -> Dict[str, str]:
        """Synchronize one source and return format -> result-path/error records."""
        if targets is None:
            targets = list(self.config.get("targets", ["markdown"]))
        source = Path(input_path)
        destination = Path(output_dir)
        destination.mkdir(parents=True, exist_ok=True)
        if not source.is_file():
            return {target: f"ERROR: input file not found: {source}" for target in targets}

        if reference_doc is None:
            reference_doc = self.config.get("custom", {}).get("reference_doc")

        results: Dict[str, str] = {}
        for target in targets:
            if target not in self.TARGETS:
                results[target] = f"ERROR: 未知格式 {target}"
                continue
            spec = self.TARGETS[target]
            if not spec.enabled:
                results[target] = f"ERROR: target disabled: {target}"
                continue
            if not self.check_availability(target):
                results[target] = f"ERROR: {spec.requires} 未安装或不可执行"
                continue

            output_path = destination / f"{source.stem}{spec.extension}"
            if target == "markdown":
                try:
                    if source.resolve() != output_path.resolve():
                        shutil.copy2(source, output_path)
                    results[target] = str(output_path)
                except OSError as exc:
                    results[target] = f"ERROR: {exc}"
                continue

            command = self._build_command(target, source, output_path, reference_doc)
            try:
                completed = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=120,
                    check=False,
                )
            except (OSError, subprocess.TimeoutExpired) as exc:
                results[target] = f"ERROR: {exc}"
                continue

            if completed.returncode == 0 and output_path.is_file():
                results[target] = str(output_path)
            else:
                detail = completed.stderr.strip() or completed.stdout.strip() or "converter failed"
                results[target] = f"ERROR: {detail}"

        ro_config = self.config.get("research_object", {})
        should_emit = bool(ro_config.get("emit_ro_crate", False)) if emit_ro_crate is None else emit_ro_crate
        if should_emit:
            self._emit_ro_crate(
                destination,
                results,
                crate_name=crate_name,
                crate_description=crate_description,
            )
        return results

    def sync_with_fallback(
        self,
        input_path: str,
        targets: Optional[List[str]] = None,
        output_dir: str = "output",
        *,
        emit_ro_crate: Optional[bool] = None,
    ) -> Dict[str, str]:
        """Synchronize with the existing HTML fallback for missing Pandoc."""
        if targets is None:
            targets = list(self.config.get("targets", ["markdown"]))
        results: Dict[str, str] = {}
        for target in targets:
            if self.check_availability(target):
                results.update(self.sync(input_path, [target], output_dir, emit_ro_crate=False))
            elif target == "html":
                try:
                    results[target] = self._fallback_html(input_path, output_dir)
                except OSError as exc:
                    results[target] = f"ERROR: {exc}"
            elif target == "docx":
                results[target] = "WARN: Pandoc 未安装，仅保留可生成的其他格式"
            else:
                results[target] = f"ERROR: 无法生成 {target}（依赖未安装）"

        ro_config = self.config.get("research_object", {})
        should_emit = bool(ro_config.get("emit_ro_crate", False)) if emit_ro_crate is None else emit_ro_crate
        if should_emit:
            self._emit_ro_crate(Path(output_dir), results)
        return results

    def _fallback_html(self, input_path: str, output_dir: str) -> str:
        import mistune

        source = Path(input_path)
        if not source.is_file():
            raise FileNotFoundError(source)
        destination = Path(output_dir)
        destination.mkdir(parents=True, exist_ok=True)
        output_path = destination / f"{source.stem}.html"
        markdown = source.read_text(encoding="utf-8")
        body = mistune.html(markdown)
        title = html_lib.escape(source.stem)
        document = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background-color: #f5f5f5; }}
pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
</style>
</head>
<body>
{body}
</body>
</html>"""
        output_path.write_text(document, encoding="utf-8")
        return str(output_path)


def demo() -> None:
    engine = SyncEngine()
    sample = "# 示例报告\n\n| 指标 | 数值 |\n|---|---|\n| 进度 | 90% |\n"
    sample_path = Path("output/_src/_sample2.md")
    sample_path.parent.mkdir(parents=True, exist_ok=True)
    sample_path.write_text(sample, encoding="utf-8")
    print("=== 多格式同步演示 ===")
    results = engine.sync_with_fallback(
        str(sample_path),
        targets=["markdown", "html"],
        output_dir="output",
        emit_ro_crate=True,
    )
    for fmt, path in results.items():
        print(f"  {fmt}: {path}")


if __name__ == "__main__":
    demo()
