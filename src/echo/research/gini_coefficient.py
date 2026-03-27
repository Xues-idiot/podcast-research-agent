"""基尼系数计算器"""

from typing import List, Optional


class GiniCoefficient:
    _instance: Optional["GiniCoefficient"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def gini(self, data: List[float]) -> Optional[float]:
        if len(data) < 2:
            return None
        sorted_data = sorted(data)
        n = len(sorted_data)
        cumsum = sum((i + 1) * x for i, x in enumerate(sorted_data))
        total = sum(sorted_data)
        if total == 0:
            return None
        return (2 * cumsum) / (n * total) - (n + 1) / n


def get_gini_coefficient() -> GiniCoefficient:
    return GiniCoefficient()
