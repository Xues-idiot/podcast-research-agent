"""立体声分析器"""

from typing import List, Optional


class StereoAnalyzer:
    _instance: Optional["StereoAnalyzer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def correlation(self, left: List[float], right: List[float]) -> float:
        if not left or not right:
            return 0.0
        n = min(len(left), len(right))
        sum_lr = sum(left[i] * right[i] for i in range(n))
        sum_l = sum(left[i] for i in range(n))
        sum_r = sum(right[i] for i in range(n))
        sum_l2 = sum(left[i] ** 2 for i in range(n))
        sum_r2 = sum(right[i] ** 2 for i in range(n))
        denom = math.sqrt((sum_l2 - sum_l ** 2 / n) * (sum_r2 - sum_r ** 2 / n))
        import math
        return sum_lr / denom if denom > 0 else 0.0

    import math


def get_stereo_analyzer() -> StereoAnalyzer:
    return StereoAnalyzer()
