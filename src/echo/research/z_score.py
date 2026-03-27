"""Z分数计算器"""

import statistics
import math
from typing import Optional


class ZScore:
    _instance: Optional["ZScore"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def z_score(self, x: float, mean: float, stdev: float) -> Optional[float]:
        if stdev == 0:
            return None
        return (x - mean) / stdev

    def percentile_to_z(self, percentile: float) -> Optional[float]:
        if percentile <= 0 or percentile >= 100:
            return None
        return statistics.NormalDist().inv_cdf(percentile / 100)


def get_z_score() -> ZScore:
    return ZScore()
