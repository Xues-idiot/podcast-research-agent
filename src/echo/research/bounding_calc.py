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
        if len(data) < 2:
            return (data[0] if data else 0.0, data[0] if data else 0.0)
        mean = sum(data) / len(data)
        n = len(data)
        stderr = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1)) / math.sqrt(n)
        z = 1.96 if confidence == 0.95 else 2.576 if confidence == 0.99 else 1.645
        margin = z * stderr
        return (mean - margin, mean + margin)


def get_confidence_interval_calc() -> ConfidenceIntervalCalc:
    return ConfidenceIntervalCalc()
