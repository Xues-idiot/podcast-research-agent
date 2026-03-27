"""Z分数计算器"""

import statistics
from typing import List, Optional


class ZScoreCalc:
    _instance: Optional["ZScoreCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def z_score(self, value: float, data: List[float]) -> float:
        if len(data) < 2:
            return 0.0
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        if stdev == 0:
            return 0.0
        return (value - mean) / stdev

    def z_scores(self, data: List[float]) -> List[float]:
        if len(data) < 2:
            return [0.0] * len(data)
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        if stdev == 0:
            return [0.0] * len(data)
        return [(x - mean) / stdev for x in data]


def get_z_score_calc() -> ZScoreCalc:
    return ZScoreCalc()
