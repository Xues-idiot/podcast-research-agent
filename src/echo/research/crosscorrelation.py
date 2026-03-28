"""互相关计算工具"""

from typing import List, Optional


class Crosscorrelation:
    _instance: Optional["Crosscorrelation"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, signal1: List[float], signal2: List[float]) -> List[float]:
        n1, n2 = len(signal1), len(signal2)
        max_len = max(n1, n2)
        result = []
        for lag in range(-max_len + 1, max_len):
            corr = sum(signal1[i] * signal2[i - lag] for i in range(max_len) if 0 <= i < n1 and 0 <= i - lag < n2)
            result.append(corr)
        return result


def get_crosscorrelation() -> Crosscorrelation:
    return Crosscorrelation()
