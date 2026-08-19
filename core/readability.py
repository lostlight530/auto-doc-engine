#!/usr/bin/env python3
"""
Readability metrics — 可读性指标（报告态，不是门禁）

Stdlib-only readability heuristics for mixed Chinese/English prose:

- **Coleman-Liau index** for Latin text (character based; no NLP dependency).
- **Average sentence length** for Latin text (words per sentence).
- **Average sentence length** for CJK text (characters per sentence; Chinese
  text gets sentence-length statistics only, no grade-level claim).

Boundaries / 边界:
- These are report-mode signals consumed by ``core/doctor.py``; they warn but
  never block a build by themselves.
- Fenced code blocks are excluded before counting.
- Metrics are only reported when a document has enough material
  (``MIN_LATIN_WORDS`` Latin words / ``MIN_CJK_SENTENCES`` CJK sentences),
  otherwise the corresponding value is ``None``.
"""

import re
from dataclasses import dataclass, field
from typing import List, Optional

# Heuristic thresholds; documented as signals, not gates.
CLI_WARN_GRADE = 16.0          # Coleman-Liau grade level warning threshold
LATIN_AVG_WORDS_WARN = 30.0    # Latin words per sentence warning threshold
CJK_AVG_CHARS_WARN = 60.0      # CJK characters per sentence warning threshold
MIN_LATIN_WORDS = 20           # below this, Latin metrics are unreliable
MIN_CJK_SENTENCES = 2          # below this, CJK metrics are unreliable

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
LETTER_RE = re.compile(r"[A-Za-z]")
LATIN_SENTENCE_RE = re.compile(r"[.!?]+")
CJK_CHAR_RE = re.compile(r"[一-鿿㐀-䶿]")
CJK_SENTENCE_RE = re.compile(r"[。！？!?]+")


@dataclass
class ReadabilityReport:
    """Readability metrics for one document body."""

    coleman_liau: Optional[float] = None
    latin_words: int = 0
    latin_sentences: int = 0
    latin_avg_words_per_sentence: Optional[float] = None
    cjk_chars: int = 0
    cjk_sentences: int = 0
    cjk_avg_chars_per_sentence: Optional[float] = None
    warnings: List[str] = field(default_factory=list)


def strip_fenced_code(text: str) -> str:
    """Remove fenced code blocks (line-based scan, keeps all other lines)."""
    kept = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            kept.append(line)
    return "\n".join(kept)


def coleman_liau_index(text: str) -> Optional[float]:
    """Coleman-Liau grade level for Latin text; None when sample is too small."""
    words = WORD_RE.findall(text)
    if len(words) < MIN_LATIN_WORDS:
        return None
    letters = len(LETTER_RE.findall(text))
    sentences = max(len([s for s in LATIN_SENTENCE_RE.split(text) if s.strip()]), 1)
    l_per_100 = letters / len(words) * 100
    s_per_100 = sentences / len(words) * 100
    return 0.0588 * l_per_100 - 0.296 * s_per_100 - 15.8


def analyze(text: str) -> ReadabilityReport:
    """Compute readability metrics for a document body (frontmatter excluded)."""
    body = strip_fenced_code(text)
    report = ReadabilityReport()

    # Latin metrics
    words = WORD_RE.findall(body)
    report.latin_words = len(words)
    latin_sentences = [s for s in LATIN_SENTENCE_RE.split(body) if WORD_RE.search(s)]
    report.latin_sentences = len(latin_sentences)
    if report.latin_words >= MIN_LATIN_WORDS:
        report.coleman_liau = coleman_liau_index(body)
        if latin_sentences:
            report.latin_avg_words_per_sentence = report.latin_words / len(latin_sentences)
        if report.coleman_liau is not None and report.coleman_liau > CLI_WARN_GRADE:
            report.warnings.append(
                f"Coleman-Liau grade {report.coleman_liau:.1f} exceeds {CLI_WARN_GRADE}"
            )
        if (report.latin_avg_words_per_sentence is not None
                and report.latin_avg_words_per_sentence > LATIN_AVG_WORDS_WARN):
            report.warnings.append(
                f"Latin average sentence length {report.latin_avg_words_per_sentence:.1f} words "
                f"exceeds {LATIN_AVG_WORDS_WARN}"
            )

    # CJK metrics (sentence length only)
    cjk_chars = CJK_CHAR_RE.findall(body)
    report.cjk_chars = len(cjk_chars)
    cjk_sentences = [s for s in CJK_SENTENCE_RE.split(body) if CJK_CHAR_RE.search(s)]
    report.cjk_sentences = len(cjk_sentences)
    if report.cjk_sentences >= MIN_CJK_SENTENCES:
        report.cjk_avg_chars_per_sentence = report.cjk_chars / report.cjk_sentences
        if report.cjk_avg_chars_per_sentence > CJK_AVG_CHARS_WARN:
            report.warnings.append(
                f"CJK average sentence length {report.cjk_avg_chars_per_sentence:.1f} chars "
                f"exceeds {CJK_AVG_CHARS_WARN}"
            )

    return report


def demo() -> None:
    sample = (
        "This is a short sentence. This one is also quite short. "
        "Short sentences keep the grade level low and readable. "
        "We prefer clear writing. Readers appreciate simple text. "
        "这一句话很短。这句话也不长。短句更清楚。\n"
    )
    report = analyze(sample)
    print("=== 可读性指标演示 ===")
    print(f"Coleman-Liau: {report.coleman_liau:.2f}")
    print(f"Latin avg words/sentence: {report.latin_avg_words_per_sentence:.1f}")
    print(f"CJK avg chars/sentence: {report.cjk_avg_chars_per_sentence:.1f}")
    print(f"warnings: {report.warnings}")


if __name__ == '__main__':
    demo()
