"""环形调制器"""

import math
from typing import List, Optional


class RingModulator:
    _instance: Optional["RingModulator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def modulate(self, carrier: List[float], modulator_freq: float, sample_rate: float = 44100) -> List[float]:
        return [carrier[i] * math.sin(2 * math.pi * modulator_freq * i / sample_rate) for i in range(len(carrier))]


def get_ring_modulator() -> RingModulator:
    return RingModulator()
