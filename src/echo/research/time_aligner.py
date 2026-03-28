"""时间对齐工具"""

from typing import List, Optional


class TimeAligner:
    _instance: Optional["TimeAligner"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def align(self, signal: List[float], shift: int) -> List[float]:
        if shift > 0:
            return [0.0] * shift + signal[:-shift]
        elif shift < 0:
            return signal[-shift:] + [0.0] * (-shift)
        return signal


def get_time_aligner() -> TimeAligner:
    return TimeAligner()
