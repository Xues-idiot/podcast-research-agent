"""哇音效果器"""

import math
from typing import List, Optional


class WahEffect:
    _instance: Optional["WahEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], freq: float = 1000, sample_rate: float = 44100) -> List[float]:
        output = list(signal)
        for i in range(len(signal)):
            mod = 0.5 + 0.5 * math.sin(2 * math.pi * 0.5 * i / sample_rate)
            cutoff = freq * (0.5 + 0.5 * mod)
            if i > 0:
                output[i] = 0.7 * output[i] + 0.3 * output[i - 1]
        return output


def get_wah_effect() -> WahEffect:
    return WahEffect()
