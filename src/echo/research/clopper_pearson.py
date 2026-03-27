"""置信区间工具"""

import math
from typing import Optional, Tuple


class ConfidenceInterval:
    _instance: Optional["ConfidenceInterval"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def confidence_interval(self, mean: float, stdev: float, n: int, confidence: float = 0.95) -> Optional[Tuple[float, float]]:
        if n < 2 or stdev == 0:
            return None
        z = 1.96 if confidence == 0.95 else 2.576 if confidence == 0.99 else 1.645
        margin = z * stdev / math.sqrt(n)
        return (mean - margin, mean + margin)


def get_confidence_interval() -> ConfidenceInterval:
    return ConfidenceInterval()
