"""翻转工具v2"""

from typing import List, Optional


class FlipTool2:
    _instance: Optional["FlipTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flip(self, signal: List[float]) -> List[float]:
        return list(reversed(signal))


def get_flip_tool2() -> FlipTool2:
    return FlipTool2()
