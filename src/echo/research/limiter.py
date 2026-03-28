"""限幅器"""

from typing import List, Optional


class Limiter:
    _instance: Optional["Limiter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def limit(self, signal: List[float], threshold: float = 0.99) -> List[float]:
        return [max(-threshold, min(threshold, s)) for s in signal]


def get_limiter() -> Limiter:
    return Limiter()
