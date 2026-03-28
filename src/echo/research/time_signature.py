"""拍号工具"""

from typing import Tuple, Optional


class TimeSignature:
    _instance: Optional["TimeSignature"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def beats_per_bar(self, numerator: int, denominator: int) -> int:
        return numerator

    def beat_unit(self, numerator: int, denominator: int) -> int:
        return denominator


def get_time_signature() -> TimeSignature:
    return TimeSignature()
