"""信号重采样工具"""

from typing import List, Optional


class SignalResampler:
    _instance: Optional["SignalResampler"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def upsample(self, signal: List[float], factor: int) -> List[float]:
        n = len(signal)
        result = [0.0] * (n * factor)
        for i in range(n):
            result[i * factor] = signal[i]
        return result

    def downsample(self, signal: List[float], factor: int) -> List[float]:
        return [signal[i] for i in range(0, len(signal), factor)]


def get_signal_resampler() -> SignalResampler:
    return SignalResampler()
