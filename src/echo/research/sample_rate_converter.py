"""采样率转换器"""

from typing import List, Optional


class SampleRateConverter:
    _instance: Optional["SampleRateConverter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, signal: List[float], from_rate: float, to_rate: float) -> List[float]:
        if from_rate == to_rate:
            return signal
        ratio = to_rate / from_rate
        n = int(len(signal) * ratio)
        result = []
        for i in range(n):
            src_idx = i / ratio
            idx = int(src_idx)
            frac = src_idx - idx
            if idx + 1 < len(signal):
                result.append(signal[idx] * (1 - frac) + signal[idx + 1] * frac)
            else:
                result.append(signal[idx])
        return result


def get_sample_rate_converter() -> SampleRateConverter:
    return SampleRateConverter()
