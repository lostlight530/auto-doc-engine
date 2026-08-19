#!/usr/bin/env python3
"""Tests for readability metrics (core/readability.py)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.readability import analyze, coleman_liau_index, strip_fenced_code


class TestStripFencedCode(unittest.TestCase):
    def test_fenced_blocks_are_removed(self):
        text = "Intro text.\n\n```python\nprint('code words here')\n```\n\nOutro text.\n"
        stripped = strip_fenced_code(text)
        self.assertNotIn("print", stripped)
        self.assertIn("Intro text.", stripped)
        self.assertIn("Outro text.", stripped)


class TestColemanLiau(unittest.TestCase):
    def test_simple_english_scores_low(self):
        text = ("The cat sat on the mat. The dog ran to the door. "
                "A bird can fly up high. The sun is hot today. "
                "We like to read books. It is fun to play games. ")
        grade = coleman_liau_index(text)
        self.assertIsNotNone(grade)
        self.assertLess(grade, 8.0)

    def test_complex_english_scores_higher_than_simple(self):
        simple = ("The cat sat on the mat. The dog ran fast. "
                  "We like books. It is fun. The sun is hot. Birds fly high. ")
        complex_text = (
            "Notwithstanding the aforementioned considerations, the institutional "
            "infrastructure necessitates comprehensive reevaluation. "
            "Pharmaceutical conglomerates demonstrate disproportionate influence "
            "over regulatory apparatuses. Consequently, interdisciplinary "
            "collaboration among governmental organizations facilitates "
            "transparency. Nevertheless, implementation remains problematic. "
        )
        self.assertGreater(coleman_liau_index(complex_text), coleman_liau_index(simple))

    def test_too_short_sample_returns_none(self):
        self.assertIsNone(coleman_liau_index("Too short."))


class TestAnalyze(unittest.TestCase):
    def test_latin_metrics_and_long_sentence_warning(self):
        sentence = " ".join(["word"] * 40) + "."
        text = f"{sentence} {sentence} {sentence}"
        report = analyze(text)
        self.assertEqual(report.latin_sentences, 3)
        self.assertGreater(report.latin_avg_words_per_sentence, 30)
        self.assertTrue(any("sentence length" in w for w in report.warnings))

    def test_cjk_sentence_length_only(self):
        text = "这一句很短。这一句也不长。句子都很清楚。"
        report = analyze(text)
        self.assertIsNone(report.coleman_liau)
        self.assertEqual(report.cjk_sentences, 3)
        # 5 + 6 + 6 CJK characters across 3 sentences.
        self.assertAlmostEqual(report.cjk_avg_chars_per_sentence, 17 / 3, places=1)
        self.assertEqual(report.warnings, [])

    def test_cjk_long_sentences_warn(self):
        long_sentence = "这" * 70 + "。"
        report = analyze(long_sentence * 2)
        self.assertTrue(any("CJK" in w for w in report.warnings))

    def test_mixed_document_reports_both_tracks(self):
        text = ("Short sentences are good. They keep text clear. "
                "Readers like simple words. This is easy to read. We enjoy it. "
                "短句很好。也很清楚。")
        report = analyze(text)
        self.assertIsNotNone(report.coleman_liau)
        self.assertIsNotNone(report.cjk_avg_chars_per_sentence)

    def test_code_blocks_do_not_inflate_metrics(self):
        text = ("Real prose here. More prose follows. "
                "Short and clear writing wins. Readers are happy. Keep it simple.\n\n"
                "```python\n" + "identifier_" + "x" * 200 + " = 1\n```\n")
        report = analyze(text)
        self.assertLess(report.latin_words, 40)


if __name__ == '__main__':
    unittest.main()
