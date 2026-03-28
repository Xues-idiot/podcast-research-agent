"""短时傅里叶变换处理器"""

import math
from typing import List, Optional


class StftProcessor:
    _instance: Optional["StftProcessor"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def process(self, signal: List[float], window_size: int = 1024, hop_size: int = 512) -> List[List[complex]]:
        n_frames = (len(signal) - window_size) // hop_size + 1
        result = []
        for i in range(n_frames):
            frame = signal[i * hop_size:i * hop_size + window_size]
            windowed = [frame[j] * 0.5 * (1 - math.cos(2 * math.pi * j / window_size)) for j in range(window_size)]
            spectrum = [complex(x, 0) for x in windowed]
            result.append(spectrum)
        return result


def get_stft_processor() -> StftProcessor:
    return StftProcessor()
