"""窗口工具v2"""

from typing import List, Optional


class WindowTool2:
    _instance: Optional["WindowTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply_window(self, signal: List[float], window_size: int) -> List[float]:
        if len(signal) < window_size:
            return signal
        import math
        result = []
        for i in range(window_size):
            w = 0.5 * (1 - math.cos(2 * math.pi * i / window_size))
            result.append(signal[i] * w)
        return result


def get_window_tool2() -> WindowTool2:
    return WindowTool2()
