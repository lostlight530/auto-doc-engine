#!/usr/bin/env python3
"""Contract tests for SARIF document-health export."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.doctor import run_doctor
from core.sarif import FINGERPRINT_KEY, SARIF_SCHEMA, main, report_to_sarif


class TestSarifExport(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.docs = Path(self._tmp.name) / "docs"
        self.docs.mkdir()

    def test_report_maps_findings_to_sarif_210(self):
        (self.docs / "a.md").write_text("# A\n\nSee [ghost](ghost.md).\n", encoding="utf-8")
        payload = report_to_sarif(run_doctor(str(self.docs), with_readability=False))

        self.assertEqual(payload["version"], "2.1.0")
        self.assertEqual(payload["$schema"], SARIF_SCHEMA)
        run = payload["runs"][0]
        self.assertEqual(run["tool"]["driver"]["name"], "auto-doc-engine doctor")
        finding = next(r for r in run["results"] if r["ruleId"] == "doc.link.dangling")
        self.assertEqual(finding["level"], "error")
        self.assertIn(FINGERPRINT_KEY, finding["partialFingerprints"])
        self.assertEqual(finding["properties"]["target"], "ghost.md")

    def test_partial_fingerprint_is_stable(self):
        (self.docs / "a.md").write_text("# A\n\nSee [ghost](ghost.md).\n", encoding="utf-8")
        report = run_doctor(str(self.docs), with_readability=False)
        first = report_to_sarif(report)["runs"][0]["results"]
        second = report_to_sarif(report)["runs"][0]["results"]
        self.assertEqual(
            [r["partialFingerprints"] for r in first],
            [r["partialFingerprints"] for r in second],
        )

    def test_cli_writes_sidecar_and_preserves_gate_exit_code(self):
        (self.docs / "a.md").write_text("# A\n\nSee [ghost](ghost.md).\n", encoding="utf-8")
        out = Path(self._tmp.name) / "doctor.sarif"
        self.assertEqual(main([str(self.docs), "--no-readability", "-o", str(out)]), 1)
        payload = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(payload["version"], "2.1.0")
        self.assertTrue(payload["runs"][0]["results"])


if __name__ == "__main__":
    unittest.main()
