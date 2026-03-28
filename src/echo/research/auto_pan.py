"""自动声像工具"""

import math
from typing import List, Optional


class AutoPan:
    _instance: Optional["AutoPan"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], rate: float = 0.5, sample_rate: float = 44100) -> List[List[float]]:
        left = [signal[i] * (1 + math.sin(2 * math.pi * rate * i / sample_rate)) / 2 for i in range(len(signal))]
        right = [signal[i] * (1 - math.sin(2 * math.pi * rate * i / sample_rate)) / 2 for i in range(len(signal))]
        return [left, right]


def get_auto_pan() -> AutoPan:
    return AutoPan()
