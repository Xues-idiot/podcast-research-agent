"""平滑工具"""

from typing import List, Optional


class SmoothingTool:
    _instance: Optional["SmoothingTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def moving_average(self, data: List[float], window: int = 3) -> List[float]:
        if not data or window <= 0:
            return []
        result = []
        for i in range(len(data)):
            start = max(0, i - window + 1)
            result.append(sum(data[start:i + 1]) / (i - start + 1))
        return result


def get_smoothing_tool() -> SmoothingTool:
    return SmoothingTool()
