"""平铺工具"""

from typing import List, Optional


class TileTool:
    _instance: Optional["TileTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def tile(self, signal: List[float], times: int) -> List[float]:
        return signal * times


def get_tile_tool() -> TileTool:
    return TileTool()
