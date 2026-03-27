"""范围映射工具"""

from typing import Optional


class MapRangeTool:
    _instance: Optional["MapRangeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def map_range(
        self,
        value: float,
        in_min: float,
        in_max: float,
        out_min: float,
        out_max: float
    ) -> Optional[float]:
        if in_max == in_min:
            return None
        normalized = (value - in_min) / (in_max - in_min)
        return out_min + (out_max - out_min) * normalized


def get_map_range_tool() -> MapRangeTool:
    return MapRangeTool()
