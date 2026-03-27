"""几何平均计算器"""

import statistics
from typing import List, Optional


class GeometricMean:
    _instance: Optional["GeometricMean"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def geometric_mean(self, data: List[float]) -> Optional[float]:
        if len(data) < 2:
            return None
        try:
            return statistics.geometric_mean(data)
        except statistics.StatisticsError:
            return None


def get_geometric_mean() -> GeometricMean:
    return GeometricMean()
