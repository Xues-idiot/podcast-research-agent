"""相干函数"""

from typing import List, Optional


class CoherenceFunction:
    _instance: Optional["CoherenceFunction"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def coherence(self, signal1: List[float], signal2: List[float]) -> Optional[float]:
        if len(signal1) != len(signal2) or len(signal1) < 2:
            return None
        n = len(signal1)
        sum_12 = sum(s1 * s2 for s1, s2 in zip(signal1, signal2)) / n
        sum_1_sq = sum(s ** 2 for s in signal1) / n
        sum_2_sq = sum(s ** 2 for s in signal2) / n
        if sum_1_sq == 0 or sum_2_sq == 0:
            return None
        return (sum_12 ** 2) / (sum_1_sq * sum_2_sq)


def get_coherence_function() -> CoherenceFunction:
    return CoherenceFunction()
