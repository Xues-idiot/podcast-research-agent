""" lookahead限幅器"""

from typing import List, Optional


class LookaheadLimiter:
    _instance: Optional["LookaheadLimiter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def limit(self, signal: List[float], lookahead: int = 100, threshold: float = 0.99) -> List[float]:
        return signal[:lookahead] + [max(-threshold, min(threshold, s)) for s in signal[lookahead:]]


def get_lookahead_limiter() -> LookaheadLimiter:
    return LookaheadLimiter()
