"""相关性计算器"""

import statistics
from typing import List, Optional


class CorrelationTool:
    _instance: Optional["CorrelationTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pearson(self, x: List[float], y: List[float]) -> Optional[float]:
        if len(x) != len(y) or len(x) < 2:
            return None
        try:
            return statistics.correlation(x, y)
        except statistics.StatisticsError:
            return None

    def spearman(self, x: List[float], y: List[float]) -> Optional[float]:
        if len(x) != len(y) or len(x) < 2:
            return None
        try:
            return statistics.spearmanr(x, y).correlation
        except statistics.StatisticsError:
            return None


def get_correlation_tool() -> CorrelationTool:
    return CorrelationTool()
