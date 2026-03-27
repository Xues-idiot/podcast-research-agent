"""KS检验工具"""

import statistics
import math
from typing import List, Optional


class KolmogorovSmirnov:
    _instance: Optional["KolmogorovSmirnov"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def ks_statistic(self, data: List[float], cdf) -> Optional[float]:
        if len(data) < 1:
            return None
        sorted_data = sorted(data)
        n = len(sorted_data)
        max_diff = 0
        for i, x in enumerate(sorted_data):
            expected = (i + 1) / n
            actual = cdf(x)
            diff = abs(expected - actual)
            max_diff = max(max_diff, diff)
        return max_diff


def get_kolmogorov_smirnov() -> KolmogorovSmirnov:
    return KolmogorovSmirnov()
