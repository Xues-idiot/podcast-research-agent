"""颤音调制器"""

import math
from typing import List, Optional


class Tremolo:
    _instance: Optional["Tremolo"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], depth: float = 0.5, rate: float = 5.0, sample_rate: float = 44100) -> List[float]:
        return [signal[i] * (1 - depth * (1 - math.sin(2 * math.pi * rate * i / sample_rate)) / 2) for i in range(len(signal))]


def get_tremolo() -> Tremolo:
    return Tremolo()
