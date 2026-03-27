"""熵计算器"""

import math
from typing import List, Optional


class EntropyCalculator:
    _instance: Optional["EntropyCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def entropy(self, data: List[float]) -> Optional[float]:
        if len(data) == 0:
            return None
        total = sum(data)
        if total == 0:
            return None
        probabilities = [x / total for x in data if x > 0]
        return -sum(p * math.log2(p) for p in probabilities if p > 0)


def get_entropy_calculator() -> EntropyCalculator:
    return EntropyCalculator()
