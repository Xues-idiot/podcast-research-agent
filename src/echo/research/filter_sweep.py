"""滤波器扫描工具"""

import math
from typing import List, Optional


class FilterSweep:
    _instance: Optional["FilterSweep"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sweep(self, signal: List[float], start_freq: float, end_freq: float, sample_rate: float = 44100) -> List[float]:
        n = len(signal)
        output = list(signal)
        for i in range(n):
            t = i / n
            cutoff = start_freq * (end_freq / start_freq) ** t
            if i > 0:
                output[i] = 0.3 * output[i] + 0.7 * output[i - 1]
        return output


def get_filter_sweep() -> FilterSweep:
    return FilterSweep()
