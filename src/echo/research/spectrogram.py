"""频谱分析器"""

import math
from typing import List, Optional


class Spectrogram:
    _instance: Optional["Spectrogram"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, signal: List[float], window_size: int = 256) -> List[List[float]]:
        if len(signal) < window_size:
            return []
        spectrogram = []
        for i in range(0, len(signal) - window_size, window_size // 2):
            window = signal[i:i+window_size]
            magnitudes = [abs(x) for x in window]
            spectrogram.append(magnitudes)
        return spectrogram


def get_spectrogram() -> Spectrogram:
    return Spectrogram()
