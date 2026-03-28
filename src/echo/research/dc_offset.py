"""直流偏移校正工具"""

from typing import List, Optional


class DcOffset:
    _instance: Optional["DcOffset"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def correct(self, signal: List[float]) -> List[float]:
        if not signal:
            return signal
        offset = sum(signal) / len(signal)
        return [s - offset for s in signal]


def get_dc_offset() -> DcOffset:
    return DcOffset()
