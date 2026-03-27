"""偏度计算器"""

import statistics
import math
from typing import List, Optional


class SkewnessTool:
    _instance: Optional["SkewnessTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def skewness(self, data: List[float]) -> Optional[float]:
        if len(data) < 3:
            return None
        n = len(data)
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        if stdev == 0:
            return None
        return (sum((x - mean) ** 3 for x in data) / n) / (stdev ** 3)


def get_skewness_tool() -> SkewnessTool:
    return SkewnessTool()
