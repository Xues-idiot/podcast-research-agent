"""重采样工具"""

from typing import List


class Resampler:
    _instance: Optional["Resampler"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def upsample(self, signal: List[float], factor: int) -> List[float]:
        if factor <= 1:
            return signal
        result = []
        for i, val in enumerate(signal):
            result.append(val)
            if i < len(signal) - 1:
                result.append((val + signal[i + 1]) / 2)
        return result

    def downsample(self, signal: List[float], factor: int) -> List[float]:
        if factor <= 1:
            return signal
        return [signal[i] for i in range(0, len(signal), factor)]


def get_resampler() -> Resampler:
    return Resampler()
