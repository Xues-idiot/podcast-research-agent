"""希尔伯特变换工具"""

import math
from typing import List, Optional


class HilbertTransform:
    _instance: Optional["HilbertTransform"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def hilbert(self, signal: List[float]) -> List[float]:
        n = len(signal)
        result = []
        for i in range(n):
            total = 0.0
            for j in range(n):
                if i != j:
                    total += signal[j] / (math.pi * (i - j))
            result.append(total)
        return result


def get_hilbert_transform() -> HilbertTransform:
    return HilbertTransform()
