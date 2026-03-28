"""音频切片工具"""

from typing import List, Optional, Tuple


class AudioSlicer:
    _instance: Optional["AudioSlicer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def slice(self, signal: List[float], start_ms: int, end_ms: int, sample_rate: float = 44100) -> List[float]:
        start = int(start_ms * sample_rate / 1000)
        end = int(end_ms * sample_rate / 1000)
        return signal[start:end]


def get_audio_slicer() -> AudioSlicer:
    return AudioSlicer()
