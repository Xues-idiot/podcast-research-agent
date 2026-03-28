"""双二阶滤波器工具"""

from typing import List, Optional


class BiquadFilterTool:
    _instance: Optional["BiquadFilterTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, signal: List[float], b0: float, b1: float, b2: float, a1: float, a2: float) -> List[float]:
        result = []
        x1, x2, y1, y2 = 0.0, 0.0, 0.0, 0.0
        for x in signal:
            y = b0 * x + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2
            x2, x1 = x1, x
            y2, y1 = y1, y
            result.append(y)
        return result


def get_biquad_filter_tool() -> BiquadFilterTool:
    return BiquadFilterTool()
