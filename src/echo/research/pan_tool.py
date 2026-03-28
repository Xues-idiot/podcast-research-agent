"""声像工具"""

from typing import List, Optional


class PanTool:
    _instance: Optional["PanTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pan(self, signal: List[float], pan_value: float) -> List[List[float]]:
        left = []
        right = []
        for sample in signal:
            left.append(sample * (1 - pan_value) ** 0.5)
            right.append(sample * (1 + pan_value) ** 0.5)
        return [left, right]


def get_pan_tool() -> PanTool:
    return PanTool()
