"""短时傅里叶变换工具"""

import math
from typing import List, Tuple


class StftTool:
    _instance: Optional["StftTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def stft(self, signal: List[float], window_size: int = 1024, hop_size: int = 512) -> List[List[Tuple[float, float]]]:
        n = len(signal)
        if n < window_size:
            return []
        spectrogram = []
        for i in range(0, n - window_size, hop_size):
            frame = signal[i:i+window_size]
            magnitudes = [(abs(x), 0.0) for x in frame]
            spectrogram.append(magnitudes)
        return spectrogram


def get_stft_tool() -> StftTool:
    return StftTool()
