"""粒子合成器"""

import random
from typing import List, Optional


class GranularSynth:
    _instance: Optional["GranularSynth"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def process(self, source: List[float], grain_size: int = 1000, num_grains: int = 50) -> List[float]:
        result = []
        for _ in range(num_grains):
            start = random.randint(0, max(0, len(source) - grain_size))
            grain = source[start:start + grain_size]
            result.extend(grain)
        return result


def get_granular_synth() -> GranularSynth:
    return GranularSynth()
