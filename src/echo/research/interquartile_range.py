"""四分位距计算器"""

import statistics
from typing import List, Optional


class InterquartileRange:
    _instance: Optional["InterquartileRange"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def iqr(self, data: List[float]) -> Optional[float]:
        if len(data) < 4:
            return None
        try:
            quartiles = statistics.quantiles(data, n=4)
            return quartiles[2] - quartiles[0]
        except statistics.StatisticsError:
            return None


def get_interquartile_range() -> InterquartileRange:
    return InterquartileRange()
