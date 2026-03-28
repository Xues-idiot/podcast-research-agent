"""幅度调制工具"""

import math
from typing import List, Optional


class AmplitudeMod:
    _instance: Optional["AmplitudeMod"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def modulate(self, signal: List[float], mod_freq: float, sample_rate: float = 44100) -> List[float]:
        return [signal[i] * (1 + math.sin(2 * math.pi * mod_freq * i / sample_rate)) / 2 for i in range(len(signal))]


def get_amplitude_mod() -> AmplitudeMod:
    return AmplitudeMod()
