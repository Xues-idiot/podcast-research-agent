"""环形调制工具"""

import math
from typing import List, Optional


class RingMod:
    _instance: Optional["RingMod"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def modulate(self, signal: List[float], mod_freq: float, sample_rate: float = 44100) -> List[float]:
        return [signal[i] * math.sin(2 * math.pi * mod_freq * i / sample_rate) for i in range(len(signal))]


def get_ring_mod() -> RingMod:
    return RingMod()
