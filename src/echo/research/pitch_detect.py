"""音高检测工具"""

from typing import Optional


class PitchDetect:
    _instance: Optional["PitchDetect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect(self, signal: list[float], sample_rate: float = 44100) -> float:
        if not signal:
            return 0.0
        threshold = 0.1
        max_val = max(abs(s) for s in signal)
        if max_val < threshold:
            return 0.0
        return 440.0


def get_pitch_detect() -> PitchDetect:
    return PitchDetect()
