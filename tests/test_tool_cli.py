#!/usr/bin/env python3
"""Contract tests for the opt-in, allowlisted local Tool/CLI/Agent surface."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from agent_tools import PROFILE, list_tool_names, tool_definitions, execute_tool_call
from tool_cli import _html_report, _human


ROOT = Path(__file__).resolve().parents[1]


class TestToolContract(unittest.TestCase):
    def test_registry_declarations_are_allowlisted(self):
        declarations = tool_definitions()
        names = [item["function"]["name"] for item in declarations]
        self.assertEqual(sorted(names), list_tool_names())
        self.assertEqual(len(names), 2)
        for item in declarations:
            schema = item["function"]["parameters"]
            self.assertEqual(item["type"], "function")
            self.assertFalse(schema["additionalProperties"])

    def test_unknown_and_invalid_arguments_fail_closed(self):
        unknown = execute_tool_call("arbitrary_python", {})
        self.assertEqual(unknown["error"]["code"], "UNKNOWN_TOOL")
        self.assertFalse(unknown["remote_provider_called"])
        self.assertFalse(unknown["scientific_validity_claim"])
        name = list_tool_names()[0]
        malformed = execute_tool_call(name, "{broken")
        self.assertEqual(malformed["error"]["code"], "INVALID_ARGUMENT")
        hidden = execute_tool_call(name, {"unsafe_cmd": "rm -rf /"})
        self.assertEqual(hidden["error"]["code"], "INVALID_ARGUMENT")

    def test_nested_relation_preflight_fails_before_execution(self):
        from agent_plan import run_plan
        invalid_relations = [
            ["not-an-object"],
            [{"relation": "uses"}],
            [{"relation": "uses", "target": 17}],
            [{"relation": "unknown", "target": "docs/a.md"}],
            [{"relation": "uses", "target": "docs/a.md", "extra": True}],
        ]
        for relations in invalid_relations:
            arguments = {"artifact_record": "not-opened.json", "relations": relations}
            with self.subTest(relations=relations):
                direct = execute_tool_call("artifact_lineage", arguments)
                self.assertEqual(direct["error"]["code"], "INVALID_ARGUMENT")
                plan = {"steps": [{"tool": "artifact_lineage", "arguments": arguments}]}
                preview = run_plan(plan)
                self.assertEqual(preview["error"]["code"], "INVALID_PLAN")
                self.assertFalse(preview["approval_granted"])
        valid = {"steps": [{"tool": "artifact_lineage", "arguments": {
            "artifact_record": "not-opened.json",
            "relations": [{"relation": "uses", "target": "docs/a.md"}],
        }}]}
        self.assertEqual(run_plan(valid)["status"], "approval_required")

    def test_cli_registry_machine_json_and_offline_html(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tool_cli.py"), "list"],
            text=True, capture_output=True, check=True, cwd=ROOT,
        )
        parsed = json.loads(proc.stdout)
        self.assertEqual(parsed["profile"], PROFILE)
        self.assertEqual(len(parsed["result"]["tools"]), 2)
        self.assertNotIn("\x1b", proc.stdout)
        self.assertEqual(proc.stderr, "")
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "report.html"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "list",
                 "--format", "html", "--output", str(path)],
                text=True, capture_output=True, check=True, cwd=ROOT,
            )
            self.assertEqual(proc.stdout, "")
            report = path.read_text(encoding="utf-8")
            self.assertIn("<!doctype html>", report)
            self.assertIn("@media(prefers-color-scheme:dark)", report)
            self.assertNotIn("<script", report)
            malicious = _html_report({"profile": PROFILE, "tool": "<script>alert(1)</script>",
                                      "status": "error", "result": None, "error": None})
            self.assertNotIn("<script>alert(1)</script>", malicious)
            self.assertIn("&lt;script&gt;", malicious)
            self.assertNotIn("\x1b", _human(parsed, color=False))

    def test_cli_invalid_arguments_machine_failure(self):
        name = list_tool_names()[0]
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tool_cli.py"), "invoke", name,
             "--args", '{"unexpected":true}'],
            text=True, capture_output=True, cwd=ROOT,
        )
        self.assertEqual(proc.returncode, 1)
        parsed = json.loads(proc.stdout)
        self.assertEqual(parsed["error"]["code"], "INVALID_ARGUMENT")


    def test_cli_output_cannot_replace_source_or_request_inputs(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.json"
            source.write_text("{\"profile\":\"auto-doc-engine/artifact-record\"}", encoding="utf-8")
            original = source.read_bytes()
            arguments = {"artifact_record": str(source)}
            request_file = Path(temp) / "request.json"
            request_file.write_text(json.dumps(arguments), encoding="utf-8")
            request_original = request_file.read_bytes()
            base = [sys.executable, str(ROOT / "tool_cli.py"), "invoke", "artifact_lineage"]
            for options, destination in (
                (["--args", json.dumps(arguments)], source),
                (["--args-file", str(request_file)], request_file),
            ):
                completed = subprocess.run(
                    base + options + ["--output", str(destination)],
                    cwd=ROOT, text=True, capture_output=True,
                )
                self.assertEqual(completed.returncode, 2, completed.stderr)
                self.assertIn("must not overwrite an input file", completed.stderr)
                self.assertEqual(source.read_bytes(), original)
                self.assertEqual(request_file.read_bytes(), request_original)

            plan_file = Path(temp) / "plan.json"
            plan_file.write_text(json.dumps({"steps": [
                {"tool": "artifact_lineage", "arguments": arguments}
            ]}), encoding="utf-8")
            plan_original = plan_file.read_bytes()
            preview = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "plan",
                 "--plan-file", str(plan_file), "--output", str(plan_file)],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(preview.returncode, 2, preview.stderr)
            self.assertIn("must not overwrite an input file", preview.stderr)
            self.assertEqual(plan_file.read_bytes(), plan_original)
            self.assertEqual(source.read_bytes(), original)



    def test_cli_document_inspect_preserves_markdown(self):
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp) / "docs"
            nested = docs / "nested"
            nested.mkdir(parents=True)
            document = nested / "a.md"
            linked = nested / "b.md"
            document.write_text("# A\\n\\nSee [B](b.md).\\n".replace("\\n", "\n"), encoding="utf-8")
            linked.write_text("# B\\n\\nSee [A](a.md).\\n".replace("\\n", "\n"), encoding="utf-8")
            original = document.read_bytes()
            args = {"docs_dir": str(docs), "with_readability": False}
            args_file = Path(temp) / "args.json"
            args_file.write_text(json.dumps(args), encoding="utf-8")
            plan_file = Path(temp) / "plan.json"
            plan_file.write_text(json.dumps({"steps": [
                {"tool": "document_inspect", "arguments": args}
            ]}), encoding="utf-8")

            for options in (
                ["invoke", "document_inspect", "--args", json.dumps(args)],
                ["invoke", "document_inspect", "--args-file", str(args_file)],
                ["plan", "--plan-file", str(plan_file)],
                ["plan", "--plan-file", str(plan_file), "--approve"],
            ):
                with self.subTest(options=options):
                    completed = subprocess.run(
                        [sys.executable, str(ROOT / "tool_cli.py"), *options,
                         "--output", str(document)],
                        cwd=ROOT, text=True, capture_output=True,
                    )
                    self.assertEqual(completed.returncode, 2, completed.stderr)
                    self.assertIn("must not overwrite an inspected Markdown document",
                                  completed.stderr)
                    self.assertEqual(document.read_bytes(), original)

            report = docs / "inspection.json"
            completed = subprocess.run(
                [sys.executable, str(ROOT / "tool_cli.py"), "invoke",
                 "document_inspect", "--args", json.dumps(args),
                 "--output", str(report)],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(report.is_file())
            self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["tool"],
                             "document_inspect")
            self.assertEqual(document.read_bytes(), original)


    def test_ro_crate_cli_rejects_payload_as_metadata_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            payload = root / "source.md"
            payload.write_bytes(b"Original research payload\n")
            initial = payload.read_bytes()
            proc = subprocess.run(
                [sys.executable, str(ROOT / "core" / "ro_crate.py"), str(root),
                 payload.name, "--name", "Research", "--description", "Test export",
                 "--output", str(payload)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 1)
            self.assertIn("must not overwrite an input payload", proc.stderr)
            self.assertEqual(payload.read_bytes(), initial)


class TestRepoIntegration(unittest.TestCase):
    def test_document_diagnostics_on_real_markdown_files(self):
        with tempfile.TemporaryDirectory() as temp:
            docs = Path(temp)
            (docs / "a.md").write_text("# A\n\nSee [B](b.md).\n", encoding="utf-8")
            (docs / "b.md").write_text("# B\n\nSee [A](a.md).\n", encoding="utf-8")
            value = execute_tool_call("document_inspect",
                                     {"docs_dir": str(docs), "with_readability": False})
            self.assertEqual(value["status"], "ok", value.get("error"))
            self.assertEqual(value["result"]["report"]["doc_count"], 2)
            self.assertEqual(value["result"]["diagnostic_exit_code"], 0)

    def test_lineage_requires_correct_source_profile(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "wrong.json"
            path.write_text('{"profile":"incorrect"}', encoding="utf-8")
            value = execute_tool_call("artifact_lineage", {"artifact_record": str(path)})
            self.assertEqual(value["status"], "error")
            self.assertEqual(value["error"]["code"], "EXECUTION_FAILED")



    def test_handoff_cli_preserves_source_when_output_collides(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.json"
            original = json.dumps({"profile": "auto-doc-engine/artifact-record"}).encode("utf-8")
            source.write_bytes(original)
            command = [sys.executable, str(ROOT / "core" / "artifact_lineage.py"), str(source)]
            rejected = subprocess.run(
                command + ["--output", str(source)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn("lineage output must not overwrite", rejected.stderr)
            self.assertEqual(source.read_bytes(), original)

            output = Path(temp) / "handoff.json"
            accepted = subprocess.run(
                command + ["--output", str(output)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            self.assertTrue(output.is_file())
            self.assertEqual(source.read_bytes(), original)

    def test_lineage_cli_never_overwrites_resolved_local_target(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source.json"
            target = Path(temp) / "dataset.json"
            source.write_text(
                json.dumps({"profile": "auto-doc-engine/artifact-record"}),
                encoding="utf-8",
            )
            original = b'{"dataset": "intact"}'
            target.write_bytes(original)
            completed = subprocess.run(
                [sys.executable, str(ROOT / "core" / "artifact_lineage.py"),
                 str(source), "--relation", f"uses={target}",
                 "--output", str(target)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("resolved local relation target", completed.stderr)
            self.assertEqual(target.read_bytes(), original)

    def test_handoff_cli_does_not_clobber_legacy_temp_name(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "handoff.json"
            source = Path(temp) / "handoff.json.tmp"
            original = json.dumps({"profile": "auto-doc-engine/artifact-record"}).encode("utf-8")
            source.write_bytes(original)
            command = [sys.executable, str(ROOT / "core" / "artifact_lineage.py"), str(source)]
            completed = subprocess.run(
                command + ["--output", str(output)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(output.is_file())
            self.assertEqual(source.read_bytes(), original)



    def test_maintenance_report_output_cannot_overwrite_inspected_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "maintenance").mkdir()
            config = root / "maintenance" / "cadence.yaml"
            config.write_text(json.dumps({
                "project_profile_prefix": "auto-doc-engine/",
                "canonical_paths": [],
                "scan_paths": [],
                "forbidden_governance_paths": [],
                "history_patterns": [],
                "cadences": {"daily": {"calibration_max_age_days": 0}},
            }), encoding="utf-8")
            manifest = root / "MANIFEST.yaml"
            manifest.write_text('calibrated: "2026-10-01"\n', encoding="utf-8")
            existing = root / "research-notes.json"
            existing.write_text('{"private":"must survive"}', encoding="utf-8")

            command = [
                sys.executable, str(ROOT / "core" / "maintenance_cadence.py"),
                "daily", "--root", str(root), "--config", "maintenance/cadence.yaml",
                "--as-of", "2026-10-26",
            ]
            for protected in (config, manifest, existing):
                with self.subTest(protected=protected.name):
                    original = protected.read_bytes()
                    attempt = subprocess.run(
                        command + ["--output", str(protected)],
                        cwd=ROOT, capture_output=True, text=True,
                    )
                    self.assertNotEqual(attempt.returncode, 0)
                    self.assertIn("not an existing maintenance report", attempt.stderr)
                    self.assertEqual(protected.read_bytes(), original)

            report = root / "maintenance-report.json"
            for _ in range(2):
                allowed = subprocess.run(
                    command + ["--output", str(report)],
                    cwd=ROOT, capture_output=True, text=True,
                )
                self.assertEqual(allowed.returncode, 0, allowed.stderr)
                self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["profile"],
                                 "auto-doc-engine/maintenance-report")
            self.assertEqual(config.read_text(encoding="utf-8"),
                             json.dumps({
                                "project_profile_prefix": "auto-doc-engine/",
                                "canonical_paths": [],
                                "scan_paths": [],
                                "forbidden_governance_paths": [],
                                "history_patterns": [],
                                "cadences": {"daily": {"calibration_max_age_days": 0}},
                             }))


if __name__ == "__main__":
    unittest.main()
