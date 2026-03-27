"""峰度计算器"""

import statistics
import math
from typing import List, Optional


class KurtosisTool:
    _instance: Optional["KurtosisTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def kurtosis(self, data: List[float]) -> Optional[float]:
        if len(data) < 4:
            return None
        n = len(data)
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        if stdev == 0:
            return None
        return (sum((x - mean) ** 4 for x in data) / n) / (stdev ** 4) - 3


def get_kurtosis_tool() -> KurtosisTool:
    return KurtosisTool()
