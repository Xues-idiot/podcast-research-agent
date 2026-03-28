"""增益减少工具"""

from typing import List, Optional


class GainReducer:
    _instance: Optional["GainReducer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reduce(self, signal: List[float], amount: float) -> List[float]:
        return [s * (1 - amount) for s in signal]


def get_gain_reducer() -> GainReducer:
    return GainReducer()
