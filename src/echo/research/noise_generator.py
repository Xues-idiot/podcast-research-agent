"""噪声生成器"""

import random
from typing import List, Optional


class NoiseGenerator:
    _instance: Optional["NoiseGenerator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def white(self, length: int) -> List[float]:
        return [random.uniform(-1, 1) for _ in range(length)]

    def pink(self, length: int) -> List[float]:
        white_noise = self.white(length)
        return [w * 0.5 for w in white_noise]

    def brown(self, length: int) -> List[float]:
        noise = []
        value = 0.0
        for _ in range(length):
            value += random.uniform(-0.1, 0.1)
            value = max(-1, min(1, value))
            noise.append(value)
        return noise


def get_noise_generator() -> NoiseGenerator:
    return NoiseGenerator()
