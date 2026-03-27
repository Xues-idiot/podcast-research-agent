"""统计收集器"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class StatsSummary:
    """统计摘要"""
    total_chars: int
    total_words: int
    total_lines: int
    avg_line_length: float
    max_line_length: int
    min_line_length: int


class StatsCollector:
    """统计收集器"""

    def collect(self, text: str) -> StatsSummary:
        """收集统计"""
        if not text:
            return StatsSummary(0, 0, 0, 0.0, 0, 0)

        lines = [l for l in text.split('\n') if l]
        words = text.split()
        line_lengths = [len(l) for l in lines]

        return StatsSummary(
            total_chars=len(text),
            total_words=len(words),
            total_lines=len(lines),
            avg_line_length=sum(line_lengths) / len(line_lengths) if line_lengths else 0,
            max_line_length=max(line_lengths) if line_lengths else 0,
            min_line_length=min(line_lengths) if line_lengths else 0
        )


_collector: Optional[StatsCollector] = None


def get_stats_collector() -> StatsCollector:
    global _collector
    if _collector is None:
        _collector = StatsCollector()
    return _collector