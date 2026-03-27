"""协方差计算器"""

from typing import List, Optional


class CovarianceCalc:
    _instance: Optional["CovarianceCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def covariance(self, x: List[float], y: List[float]) -> float:
        if len(x) != len(y) or len(x) < 2:
            return 0.0
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / (n - 1)


def get_covariance_calc() -> CovarianceCalc:
    return CovarianceCalc()
