"""平滑工具v2"""

from typing import List, Optional


class SmoothTool2:
    _instance: Optional["SmoothTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def smooth(self, signal: List[float], window: int = 3) -> List[float]:
        result = []
        for i in range(len(signal)):
            start = max(0, i - window + 1)
            result.append(sum(signal[start:i + 1]) / (i - start + 1))
        return result


def get_smooth_tool2() -> SmoothTool2:
    return SmoothTool2()
