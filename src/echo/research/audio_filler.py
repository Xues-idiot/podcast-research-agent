"""音频填充工具"""

from typing import List, Optional


class AudioFiller:
    _instance: Optional["AudioFiller"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pad(self, signal: List[float], target_length: int, pad_value: float = 0.0) -> List[float]:
        if len(signal) >= target_length:
            return signal[:target_length]
        return signal + [pad_value] * (target_length - len(signal))

    def trim_to(self, signal: List[float], target_length: int) -> List[float]:
        return signal[:target_length]


def get_audio_filler() -> AudioFiller:
    return AudioFiller()
