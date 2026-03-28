"""减法合成器"""

import math
from typing import List, Optional


class SubtractiveSynth:
    _instance: Optional["SubtractiveSynth"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def synthesize(self, freq: float, duration_ms: int, harmonics: List[float], sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        result = [0.0] * n
        for i, amp in enumerate(harmonics):
            if i == 0:
                continue
            for j in range(n):
                result[j] += amp * math.sin(2 * math.pi * freq * (i + 1) * j / sample_rate)
        return result


def get_subtractive_synth() -> SubtractiveSynth:
    return SubtractiveSynth()
