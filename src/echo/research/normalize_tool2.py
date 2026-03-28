"""归一化工具v2"""

from typing import List, Optional


class NormalizeTool2:
    _instance: Optional["NormalizeTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def normalize(self, signal: List[float], target: float = 1.0) -> List[float]:
        if not signal:
            return signal
        max_val = max(abs(s) for s in signal)
        if max_val == 0:
            return signal
        factor = target / max_val
        return [s * factor for s in signal]


def get_normalize_tool2() -> NormalizeTool2:
    return NormalizeTool2()
