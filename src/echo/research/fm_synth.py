"""FM合成器"""

import math
from typing import List, Optional


class FmSynth:
    _instance: Optional["FmSynth"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def synthesize(self, carrier_freq: float, mod_freq: float, mod_index: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [math.sin(2 * math.pi * carrier_freq * i / sample_rate + mod_index * math.sin(2 * math.pi * mod_freq * i / sample_rate)) for i in range(n)]


def get_fm_synth() -> FmSynth:
    return FmSynth()
