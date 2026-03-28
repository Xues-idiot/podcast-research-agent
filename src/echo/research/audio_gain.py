"""音频增益工具"""

from typing import List, Optional


class AudioGain:
    _instance: Optional["AudioGain"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], gain_db: float) -> List[float]:
        factor = 10 ** (gain_db / 20)
        return [s * factor for s in signal]


def get_audio_gain() -> AudioGain:
    return AudioGain()
