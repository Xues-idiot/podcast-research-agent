"""调和平均计算器"""

import statistics
from typing import List, Optional


class HarmonicMean:
    _instance: Optional["HarmonicMean"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def harmonic_mean(self, data: List[float]) -> Optional[float]:
        if len(data) < 2:
            return None
        try:
            return statistics.harmonic_mean(data)
        except statistics.StatisticsError:
            return None


def get_harmonic_mean() -> HarmonicMean:
    return HarmonicMean()
