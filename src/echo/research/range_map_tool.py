"""范围映射工具"""

from typing import Optional


class RangeMapTool:
    _instance: Optional["RangeMapTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def map_range(self, value: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        if in_max == in_min:
            return out_min
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        return max(min_val, min(max_val, value))


def get_range_map_tool() -> RangeMapTool:
    return RangeMapTool()
