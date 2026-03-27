"""双二阶滤波器"""

from typing import List


class BiquadFilter:
    _instance: Optional["BiquadFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], b0: float = 1.0, b1: float = 0.0, b2: float = 0.0, a1: float = 0.0, a2: float = 0.0) -> List[float]:
        if len(data) == 0:
            return []
        result = []
        x1, x2, y1, y2 = 0.0, 0.0, 0.0, 0.0
        for x in data:
            y = b0 * x + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2
            x2, x1 = x1, x
            y2, y1 = y1, y
            result.append(y)
        return result


def get_biquad_filter() -> BiquadFilter:
    return BiquadFilter()
