"""分割工具v2"""

from typing import List, Optional


class SplitTool2:
    _instance: Optional["SplitTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def split(self, signal: List[float], size: int) -> List[List[float]]:
        return [signal[i:i + size] for i in range(0, len(signal), size)]


def get_split_tool2() -> SplitTool2:
    return SplitTool2()
