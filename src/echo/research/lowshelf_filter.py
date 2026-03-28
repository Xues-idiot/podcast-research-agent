"""低搁架滤波器"""

from typing import List, Optional


class LowShelfFilter:
    _instance: Optional["LowShelfFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, signal: List[float], gain: float = 0.0) -> List[float]:
        return signal


def get_low_shelf_filter() -> LowShelfFilter:
    return LowShelfFilter()
