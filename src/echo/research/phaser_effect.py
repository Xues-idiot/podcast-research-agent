"""移相效果器"""

import math
from typing import List, Optional


class PhaserEffect:
    _instance: Optional["PhaserEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], depth: float = 0.5, rate: float = 0.5, sample_rate: float = 44100) -> List[float]:
        output = list(signal)
        for i in range(len(signal)):
            mod = math.sin(2 * math.pi * rate * i / sample_rate)
            phase_shift = depth * mod
            if i > 0:
                output[i] += phase_shift * output[i - 1]
        return output


def get_phaser_effect() -> PhaserEffect:
    return PhaserEffect()
