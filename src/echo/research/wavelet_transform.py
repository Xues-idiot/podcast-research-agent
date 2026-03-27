"""小波变换工具"""

from typing import List, Optional


class WaveletTransform:
    _instance: Optional["WaveletTransform"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def haar_transform(self, signal: List[float]) -> List[float]:
        n = len(signal)
        if n <= 1:
            return signal
        result = []
        for i in range(0, n, 2):
            result.append((signal[i] + signal[i + 1]) / 2)
            result.append((signal[i] - signal[i + 1]) / 2)
        return result[:n // 2] + result[n // 2:]


def get_wavelet_transform() -> WaveletTransform:
    return WaveletTransform()
