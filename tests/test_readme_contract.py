"""Truth-contract checks for the Chinese README's evidence boundary."""

from pathlib import Path
import unittest


README_ZH = Path(__file__).resolve().parents[1] / "README_zh.md"


class ChineseReadmeContractTests(unittest.TestCase):
    def setUp(self):
        self.readme = README_ZH.read_text(encoding="utf-8")

    def test_capability_states_and_current_module_paths_are_explicit(self):
        for marker in ("已实现", "可选", "实验性", "当前未集成"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.readme)

        for path in (
            "core/renderer.py",
            "core/ast_engine.py",
            "core/incremental.py",
            "core/sync.py",
        ):
            with self.subTest(path=path):
                self.assertIn(path, self.readme)

    def test_readme_rejects_unsupported_or_obsolete_claims(self):
        for claim in ("彻底解决", "精准无损", "不可篡改", "一键分发"):
            with self.subTest(claim=claim):
                self.assertNotIn(claim, self.readme)

        self.assertNotIn(
            "├── incremental/",
            self.readme,
            "README must not claim a tracked incremental/ directory",
        )


if __name__ == "__main__":
    unittest.main()