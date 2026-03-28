"""范围映射工具"""

from typing import List, Optional, Callable


class RangeMapTool:
    _instance: Optional["RangeMapTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def map_value(self, value: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        """将值从一个范围映射到另一个范围"""
        if in_max == in_min:
            return (out_min + out_max) / 2
        return out_min + (value - in_min) / (in_max - in_min) * (out_max - out_min)

    def map_range(self, values: List[float], in_min: float, in_max: float, out_min: float, out_max: float) -> List[float]:
        """批量范围映射"""
        return [self.map_value(v, in_min, in_max, out_min, out_max) for v in values]

    def clamp(self, value: float, min_val: float, max_val: float) -> float:
        """限制值在范围内"""
        return max(min_val, min(max_val, value))

    def wrap(self, value: float, min_val: float, max_val: float) -> float:
        """值环绕"""
        range_val = max_val - min_val
        if range_val == 0:
            return min_val
        return min_val + ((value - min_val) % range_val)


def get_range_map_tool() -> RangeMapTool:
    return RangeMapTool()