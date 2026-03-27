"""文本指标计算工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TextMetrics:
    """文本指标"""
    char_count: int
    word_count: int
    line_count: int
    paragraph_count: int
    avg_word_length: float
    avg_sentence_length: float
    readability_score: float


class TextMetricsCalculator:
    """文本指标计算"""

    def calculate(self, text: str) -> TextMetrics:
        """计算指标"""
        if not text:
            return TextMetrics(0, 0, 0, 0, 0.0, 0.0, 0.0)

        char_count = len(text)
        words = text.split()
        word_count = len(words)
        line_count = len([l for l in text.split('\n') if l.strip()])
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])

        avg_word_length = sum(len(w) for w in words) / word_count if word_count else 0

        import re
        sentences = re.split(r'[。！？.!?]+', text)
        sentences = [s for s in sentences if s.strip()]
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0

        readability = self._calculate_readability(text, avg_sentence_length, avg_word_length)

        return TextMetrics(
            char_count=char_count,
            word_count=word_count,
            line_count=line_count,
            paragraph_count=paragraph_count,
            avg_word_length=round(avg_word_length, 2),
            avg_sentence_length=round(avg_sentence_length, 2),
            readability_score=round(readability, 2)
        )

    def _calculate_readability(self, text: str, avg_sentence_len: float, avg_word_len: float) -> float:
        """简单可读性评分"""
        return 100 - (avg_sentence_len * 0.5 + avg_word_len * 5)


_calculator: Optional[TextMetricsCalculator] = None


def get_text_metrics_calculator() -> TextMetricsCalculator:
    global _calculator
    if _calculator is None:
        _calculator = TextMetricsCalculator()
    return _calculator