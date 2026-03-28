"""调和平均计算器"""

from typing import List, Optional


class HarmonicMeanCalc:
    _instance: Optional["HarmonicMeanCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def harmonic_mean(self, values: List[float]) -> float:
        if not values:
            return 0.0
        n = len(values)
        if any(v == 0 for v in values):
            return 0.0
        return n / sum(1 / v for v in values)


def get_harmonic_mean_calc() -> HarmonicMeanCalc:
    return HarmonicMeanCalc()
