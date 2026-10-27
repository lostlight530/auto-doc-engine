"""Regression coverage for artifact-record output and evidence preservation."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from core.artifact_record import build_artifact_record, write_artifact_record


ROOT = Path(__file__).resolve().parents[1]


class TestArtifactRecordOutput(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "research.md"
        self.source.write_text("# Original research\n", encoding="utf-8")

    def test_rejects_source_and_derivative_collisions(self):
        derivative = self.root / "research.html"
        derivative.write_text("<h1>Original derivative</h1>\n", encoding="utf-8")
        record = build_artifact_record(self.source, derivatives={"html": derivative})
        for evidence in (self.source, derivative):
            with self.subTest(evidence=evidence.name):
                original = evidence.read_bytes()
                with self.assertRaisesRegex(ValueError, "must not overwrite input evidence"):
                    write_artifact_record(record, output=evidence)
                self.assertEqual(evidence.read_bytes(), original)

    def test_rejects_local_reference_collisions(self):
        references = {
            key: self.root / f"{key}.txt"
            for key in ("configuration", "provenance", "validation", "source", "disclosure")
        }
        for file in references.values():
            file.write_text(f"Evidence for {file.stem}\n", encoding="utf-8")
        self.source.write_text(
            "---\n"
            f"sources: ['{references['source']}']\n"
            f"disclosure_ref: '{references['disclosure']}'\n"
            "---\n# Original research\n",
            encoding="utf-8",
        )
        record = build_artifact_record(
            self.source,
            configuration_ref=str(references["configuration"]),
            provenance_ref=str(references["provenance"]),
            validation_ref=str(references["validation"]),
        )
        for evidence in references.values():
            with self.subTest(evidence=evidence.name):
                original = evidence.read_bytes()
                with self.assertRaisesRegex(ValueError, "must not overwrite input evidence"):
                    write_artifact_record(record, output=evidence)
                self.assertEqual(evidence.read_bytes(), original)

    def test_existing_legacy_tmp_file_survives_successful_write(self):
        output = self.root / "research.artifact.json"
        old_temp = self.root / "research.artifact.json.tmp"
        old_temp.write_bytes(b"Unrelated evidence in legacy staging path")
        write_artifact_record(build_artifact_record(self.source), output=output)
        self.assertEqual(old_temp.read_bytes(), b"Unrelated evidence in legacy staging path")
        self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["profile"],
                         "auto-doc-engine/artifact-record")

    def test_output_may_be_refreshed_when_not_an_input(self):
        output = self.root / "research.artifact.json"
        write_artifact_record(build_artifact_record(self.source), output=output)
        first = json.loads(output.read_text(encoding="utf-8"))
        self.source.write_text("# Updated research\n", encoding="utf-8")
        write_artifact_record(build_artifact_record(self.source), output=output)
        second = json.loads(output.read_text(encoding="utf-8"))
        self.assertNotEqual(first["source_artifact"]["file_sha256"],
                            second["source_artifact"]["file_sha256"])

    def test_symlink_to_source_is_rejected(self):
        alias = self.root / "alias.json"
        try:
            alias.symlink_to(self.source)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"symlinks unavailable: {exc}")
        with self.assertRaisesRegex(ValueError, "must not overwrite input evidence"):
            write_artifact_record(build_artifact_record(self.source), output=alias)
        self.assertEqual(self.source.read_text(encoding="utf-8"), "# Original research\n")

    def test_hardlink_to_source_is_rejected(self):
        alias = self.root / "alias.json"
        try:
            os.link(self.source, alias)
        except OSError as exc:
            self.skipTest(f"hard links unavailable: {exc}")
        with self.assertRaisesRegex(ValueError, "must not overwrite input evidence"):
            write_artifact_record(build_artifact_record(self.source), output=alias)
        self.assertEqual(alias.read_text(encoding="utf-8"), "# Original research\n")

    def test_cli_rejects_source_output_without_changing_source(self):
        original = self.source.read_bytes()
        result = subprocess.run(
            [sys.executable, "-B", str(ROOT / "core" / "artifact_record.py"),
             str(self.source), "--output", str(self.source)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("must not overwrite input evidence", result.stderr)
        self.assertEqual(self.source.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
