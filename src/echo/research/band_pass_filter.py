"""带通滤波器"""

from typing import List


class BandPassFilter:
    _instance: Optional["BandPassFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, data: List[float], low: float, high: float) -> List[float]:
        if len(data) == 0:
            return []
        from echo.research.low_pass_filter import get_low_pass_filter
        from echo.research.high_pass_filter import get_high_pass_filter
        lp = get_low_pass_filter()
        hp = get_high_pass_filter()
        filtered = hp.filter(data, 0.7)
        return lp.filter(filtered, 0.7)


def get_band_pass_filter() -> BandPassFilter:
    return BandPassFilter()
