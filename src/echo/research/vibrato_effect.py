""" vibrato效果器"""

import math
from typing import List, Optional


class VibratoEffect:
    _instance: Optional["VibratoEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], depth: float = 0.5, rate: float = 5.0, sample_rate: float = 44100) -> List[float]:
        output = list(signal)
        max_delay = int(0.05 * sample_rate)
        for i in range(len(signal)):
            delay = int(max_delay * depth * math.sin(2 * math.pi * rate * i / sample_rate))
            if i - delay >= 0:
                output[i] = signal[i - delay]
        return output


def get_vibrato_effect() -> VibratoEffect:
    return VibratoEffect()
