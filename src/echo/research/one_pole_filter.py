"""单极滤波器"""

from typing import List, Optional


class OnePoleFilter:
    _instance: Optional["OnePoleFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, signal: List[float], coeff: float = 0.5) -> List[float]:
        result = []
        prev = 0.0
        for s in signal:
            prev = prev + coeff * (s - prev)
            result.append(prev)
        return result


def get_one_pole_filter() -> OnePoleFilter:
    return OnePoleFilter()
