"""混响效果器"""

from typing import List, Optional


class Reverb:
    _instance: Optional["Reverb"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: list[float], decay: float = 0.5, delay_ms: int = 50, sample_rate: float = 44100) -> list[float]:
        delay_samples = int(delay_ms * sample_rate / 1000)
        result = list(signal)
        for i in range(delay_samples, len(signal)):
            result[i] += decay * signal[i - delay_samples]
        return result


def get_reverb() -> Reverb:
    return Reverb()
