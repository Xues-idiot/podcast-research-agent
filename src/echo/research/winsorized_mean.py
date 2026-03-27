"""Winsorized平均计算器"""

import statistics
from typing import List, Optional


class WinsorizedMean:
    _instance: Optional["WinsorizedMean"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def winsorized_mean(self, data: List[float], proportion: float = 0.1) -> Optional[float]:
        if len(data) < 2:
            return None
        try:
            sorted_data = sorted(data)
            n = len(sorted_data)
            k = int(n * proportion)
            if k == 0:
                return statistics.mean(data)
            lower = sorted_data[k]
            upper = sorted_data[n - k - 1]
            trimmed = [max(lower, min(upper, x)) for x in data]
            return statistics.mean(trimmed)
        except:
            return None


def get_winsorized_mean() -> WinsorizedMean:
    return WinsorizedMean()
