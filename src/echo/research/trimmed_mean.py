"""截断平均计算器"""

import statistics
from typing import List, Optional


class TrimmedMean:
    _instance: Optional["TrimmedMean"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trimmed_mean(self, data: List[float], proportion: float = 0.1) -> Optional[float]:
        if len(data) < 4:
            return None
        try:
            return statistics.mean(statistics.quantiles(data, n=10)[int(proportion * 10):int((1 - proportion) * 10)])
        except:
            return None


def get_trimmed_mean() -> TrimmedMean:
    return TrimmedMean()
