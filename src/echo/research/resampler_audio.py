"""音频重采样器"""

from typing import List, Optional


class AudioResampler:
    _instance: Optional["AudioResampler"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def resample(self, signal: List[float], from_rate: int, to_rate: int) -> List[float]:
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


def get_audio_resampler() -> AudioResampler:
    return AudioResampler()
