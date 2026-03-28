"""增益工具v2"""

from typing import List, Optional


class GainTool2:
    _instance: Optional["GainTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], db: float) -> List[float]:
        factor = 10 ** (db / 20)
        return [s * factor for s in signal]


def get_gain_tool2() -> GainTool2:
    return GainTool2()
