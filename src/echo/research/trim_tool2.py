"""修剪工具v2"""

from typing import List, Optional


class TrimTool2:
    _instance: Optional["TrimTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trim(self, signal: List[float], length: int) -> List[float]:
        return signal[:length]


def get_trim_tool2() -> TrimTool2:
    return TrimTool2()
