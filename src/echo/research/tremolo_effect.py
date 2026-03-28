"""颤音效果器"""

import math
from typing import List, Optional


class TremoloEffect:
    _instance: Optional["TremoloEffect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], depth: float = 0.5, rate: float = 5.0, sample_rate: float = 44100) -> List[float]:
        output = []
        for i in range(len(signal)):
            mod = 1.0 - depth * (1.0 + math.sin(2 * math.pi * rate * i / sample_rate)) / 2
            output.append(signal[i] * mod)
        return output


def get_tremolo_effect() -> TremoloEffect:
    return TremoloEffect()
