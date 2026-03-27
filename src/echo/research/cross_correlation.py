"""互相关工具"""

from typing import List, Optional


class CrossCorrelation:
    _instance: Optional["CrossCorrelation"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def cross_corr(self, x: List[float], y: List[float], lag: int = 0) -> Optional[float]:
        if len(x) != len(y) or len(x) < abs(lag):
            return None
        if lag >= 0:
            return sum(x[i] * y[i + lag] for i in range(len(x) - lag))
        return sum(x[i - lag] * y[i] for i in range(-lag, len(x)))


def get_cross_correlation() -> CrossCorrelation:
    return CrossCorrelation()
