"""音高修正工具"""

from typing import List, Optional


class PitchCorrect:
    _instance: Optional["PitchCorrect"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def correct(self, signal: List[float], semitones: float = 0.0) -> List[float]:
        return signal


def get_pitch_correct() -> PitchCorrect:
    return PitchCorrect()
