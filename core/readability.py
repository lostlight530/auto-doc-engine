#!/usr/bin/env python3
"""Descriptive readability heuristics for mixed Latin/CJK prose.

The module reports Coleman-Liau and sentence-length signals without turning them
into writing-quality, accessibility or scientific-validity claims. It is used
by ``core.doctor`` as optional descriptive evidence.

Fenced code delimited by backticks or tildes is excluded before analysis.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional

CLI_WARN_GRADE = 16.0
LATIN_AVG_WORDS_WARN = 30.0
CJK_AVG_CHARS_WARN = 60.0
MIN_LATIN_WORDS = 20
MIN_CJK_SENTENCES = 2

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
LETTER_RE = re.compile(r"[A-Za-z]")
LATIN_SENTENCE_RE = re.compile(r"[.!?]+")
CJK_CHAR_RE = re.compile(r"[一-鿿㐀-䶿]")
CJK_SENTENCE_RE = re.compile(r"[。！？!?]+")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")


@dataclass
class ReadabilityReport:
    coleman_liau: Optional[float] = None
    latin_words: int = 0
    latin_sentences: int = 0
    latin_avg_words_per_sentence: Optional[float] = None
    cjk_chars: int = 0
    cjk_sentences: int = 0
    cjk_avg_chars_per_sentence: Optional[float] = None
    warnings: List[str] = field(default_factory=list)


def strip_fenced_code(text: str) -> str:
    """Remove CommonMark-style fenced code regions using a bounded line scan."""
    kept: List[str] = []
    fence_char: Optional[str] = None
    fence_len = 0
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            char = marker[0]
            if fence_char is None:
                fence_char = char
                fence_len = len(marker)
                continue
            if char == fence_char and len(marker) >= fence_len:
                fence_char = None
                fence_len = 0
                continue
        if fence_char is None:
            kept.append(line)
    return "\n".join(kept)


def coleman_liau_index(text: str) -> Optional[float]:
    """Return Coleman-Liau grade estimate for a sufficiently large Latin sample."""
    words = WORD_RE.findall(text)
    if len(words) < MIN_LATIN_WORDS:
        return None
    letters = len(LETTER_RE.findall(text))
    sentences = max(len([part for part in LATIN_SENTENCE_RE.split(text) if WORD_RE.search(part)]), 1)
    letters_per_100 = letters / len(words) * 100
    sentences_per_100 = sentences / len(words) * 100
    return 0.0588 * letters_per_100 - 0.296 * sentences_per_100 - 15.8


def analyze(text: str) -> ReadabilityReport:
    """Compute descriptive Latin/CJK readability metrics for document prose."""
    body = strip_fenced_code(text)
    report = ReadabilityReport()

    words = WORD_RE.findall(body)
    report.latin_words = len(words)
    latin_sentences = [part for part in LATIN_SENTENCE_RE.split(body) if WORD_RE.search(part)]
    report.latin_sentences = len(latin_sentences)
    if report.latin_words >= MIN_LATIN_WORDS:
        report.coleman_liau = coleman_liau_index(body)
        if latin_sentences:
            report.latin_avg_words_per_sentence = report.latin_words / len(latin_sentences)
        if report.coleman_liau is not None and report.coleman_liau > CLI_WARN_GRADE:
            report.warnings.append(
                f"Coleman-Liau grade {report.coleman_liau:.1f} exceeds heuristic threshold {CLI_WARN_GRADE}"
            )
        if (
            report.latin_avg_words_per_sentence is not None
            and report.latin_avg_words_per_sentence > LATIN_AVG_WORDS_WARN
        ):
            report.warnings.append(
                f"Latin average sentence length {report.latin_avg_words_per_sentence:.1f} words "
                f"exceeds heuristic threshold {LATIN_AVG_WORDS_WARN}"
            )

    report.cjk_chars = len(CJK_CHAR_RE.findall(body))
    cjk_sentences = [part for part in CJK_SENTENCE_RE.split(body) if CJK_CHAR_RE.search(part)]
    report.cjk_sentences = len(cjk_sentences)
    if report.cjk_sentences >= MIN_CJK_SENTENCES:
        report.cjk_avg_chars_per_sentence = report.cjk_chars / report.cjk_sentences
        if report.cjk_avg_chars_per_sentence > CJK_AVG_CHARS_WARN:
            report.warnings.append(
                f"CJK average sentence length {report.cjk_avg_chars_per_sentence:.1f} chars "
                f"exceeds heuristic threshold {CJK_AVG_CHARS_WARN}"
            )
    return report


def demo() -> None:
    sample = (
        "This is a short sentence. This one is also quite short. "
        "Short sentences keep this sample easy to inspect. We prefer clear writing. "
        "Readers can compare descriptive metrics without treating them as quality scores. "
        "这一句话很短。这句话也不长。短句更清楚。\n"
        "~~~python\nprint('excluded')\n~~~\n"
    )
    report = analyze(sample)
    print("=== 可读性指标演示 ===")
    print("Coleman-Liau:", report.coleman_liau)
    print("Latin avg words/sentence:", report.latin_avg_words_per_sentence)
    print("CJK avg chars/sentence:", report.cjk_avg_chars_per_sentence)
    print("warnings:", report.warnings)


if __name__ == "__main__":
    demo()
