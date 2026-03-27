"""自相关工具"""

import statistics
from typing import List, Optional


class Autocorrelation:
    _instance: Optional["Autocorrelation"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def autocorr(self, data: List[float], lag: int = 1) -> Optional[float]:
        if len(data) <= lag:
            return None
        n = len(data)
        mean = statistics.mean(data)
        c0 = sum((x - mean) ** 2 for x in data) / n
        if c0 == 0:
            return None
        clag = sum((data[i] - mean) * (data[i - lag] - mean) for i in range(lag, n)) / n
        return clag / c0


def get_autocorrelation() -> Autocorrelation:
    return Autocorrelation()
