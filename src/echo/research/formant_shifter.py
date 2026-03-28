"""共振峰变换工具"""

from typing import List, Optional


class FormantShifter:
    _instance: Optional["FormantShifter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shift(self, signal: List[float], factor: float) -> List[float]:
        return signal


def get_formant_shifter() -> FormantShifter:
    return FormantShifter()
