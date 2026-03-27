"""陷波滤波器"""

from typing import List, Optional


class NotchFilter:
    _instance: Optional["NotchFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], freq: float, sample_rate: float = 1.0) -> List[float]:
        if len(data) == 0:
            return []
        w0 = 2 * 3.14159 * freq / sample_rate
        alpha = 0.1
        b0 = 1.0
        b1 = -2 * 0.9 * (1 - alpha) * (1 - alpha) / (1 + alpha)
        b2 = (1 + alpha) * (1 + alpha) - 4 * 0.81 * (1 - alpha) * (1 - alpha)
        from echo.research.biquad_filter import get_biquad_filter
        return get_biquad_filter().filter(data, b0, b1, b2, b1, b2)


def get_notch_filter() -> NotchFilter:
    return NotchFilter()
