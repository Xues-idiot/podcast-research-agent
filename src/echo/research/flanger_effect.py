"""镶边效果器"""

import math
from typing import List, Optional


class FlangerEffect:
    _instance: Optional["FlangerEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], depth: float = 0.5, rate: float = 0.5, sample_rate: float = 44100) -> List[float]:
        delay_max = int(0.01 * sample_rate)
        output = list(signal)
        for i in range(len(signal)):
            delay = int(depth * delay_max * (0.5 + 0.5 * math.sin(2 * math.pi * rate * i / sample_rate)))
            if i - delay >= 0:
                output[i] += 0.7 * signal[i - delay]
        return output


def get_flanger_effect() -> FlangerEffect:
    return FlangerEffect()
