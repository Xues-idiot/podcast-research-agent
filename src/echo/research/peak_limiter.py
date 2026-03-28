"""峰值限幅器"""

from typing import List, Optional


class PeakLimiter:
    _instance: Optional["PeakLimiter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def limit(self, signal: List[float], threshold: float = 0.99) -> List[float]:
        return [max(-threshold, min(threshold, s)) for s in signal]


def get_peak_limiter() -> PeakLimiter:
    return PeakLimiter()
