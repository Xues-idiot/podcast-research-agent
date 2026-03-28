"""合唱效果器"""

import math
import random
from typing import List, Optional


class ChorusEffect:
    _instance: Optional["ChorusEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], depth: float = 0.5, rate: float = 1.0, sample_rate: float = 44100) -> List[float]:
        delay_max = int(0.03 * sample_rate)
        output = list(signal)
        for i in range(len(signal)):
            delay = int(depth * delay_max * (0.5 + 0.5 * math.sin(2 * math.pi * rate * i / sample_rate)))
            if i - delay >= 0:
                output[i] += 0.5 * signal[i - delay]
        return output


def get_chorus_effect() -> ChorusEffect:
    return ChorusEffect()
