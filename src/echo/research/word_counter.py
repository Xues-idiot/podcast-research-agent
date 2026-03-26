"""文本统计工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TextStats:
    """文本统计结果"""
    char_count: int
    word_count: int
    chinese_char_count: int
    english_word_count: int
    line_count: int
    paragraph_count: int
    avg_line_length: float
    reading_time_seconds: int


class TextStatsCalculator:
    """计算文本统计信息"""

    def calculate(self, text: str) -> TextStats:
        """计算统计信息"""
        if not text:
            return TextStats(
                char_count=0, word_count=0, chinese_char_count=0,
                english_word_count=0, line_count=0, paragraph_count=0,
                avg_line_length=0.0, reading_time_seconds=0
            )

        lines = [l for l in text.split("\n") if l.strip()]
        paragraphs = [p for p in text.split("\n\n") if p.strip()]

        chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        english_words = len([w for w in text.split() if w.isascii()])

        # 粗略估算阅读时间: 中文字符0.3秒/字，英文单词0.5秒/词
        reading_time = chinese_chars * 0.3 + english_words * 0.5

        return TextStats(
            char_count=len(text),
            word_count=len(text.split()),
            chinese_char_count=chinese_chars,
            english_word_count=english_words,
            line_count=len(lines),
            paragraph_count=len(paragraphs),
            avg_line_length=sum(len(l) for l in lines) / len(lines) if lines else 0,
            reading_time_seconds=int(reading_time)
        )


_calculator: Optional[TextStatsCalculator] = None


def get_text_stats_calculator() -> TextStatsCalculator:
    global _calculator
    if _calculator is None:
        _calculator = TextStatsCalculator()
    return _calculator