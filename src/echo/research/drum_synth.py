"""鼓机合成器"""

import math
from typing import List, Optional


class DrumSynth:
    _instance: Optional["DrumSynth"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def kick(self, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [math.sin(2 * math.pi * 60 * math.exp(-i / (n * 0.1)) * i / sample_rate) * math.exp(-i / (n * 0.2)) for i in range(n)]

    def snare(self, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        import random
        return [random.uniform(-1, 1) * math.exp(-i / (n * 0.1)) for i in range(n)]


def get_drum_synth() -> DrumSynth:
    return DrumSynth()
