"""区间限制工具"""

from typing import Optional


class ClampTool:
    _instance: Optional["ClampTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        if value < min_val:
            return min_val
        if value > max_val:
            return max_val
        return value

    def in_range(self, value: float, min_val: float, max_val: float) -> bool:
        return min_val <= value <= max_val


def get_clamp_tool() -> ClampTool:
    return ClampTool()
