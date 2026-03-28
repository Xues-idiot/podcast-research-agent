"""置信区间计算器"""

import math
from typing import List, Optional, Tuple


class ConfidenceIntervalCalc:
    _instance: Optional["ConfidenceIntervalCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def confidence_interval(self, data: List[float], confidence: float = 0.95) -> Tuple[float, float]:
        if not data:
            return (0.0, 0.0)
        n = len(data)
        mean = sum(data) / n
        std = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1)) if n > 1 else 0
        z = 1.96 if confidence == 0.95 else 2.576 if confidence == 0.99 else 1.645
        margin = z * std / math.sqrt(n) if n > 0 else 0
        return (mean - margin, mean + margin)


def get_confidence_interval_calc() -> ConfidenceIntervalCalc:
    return ConfidenceIntervalCalc()
