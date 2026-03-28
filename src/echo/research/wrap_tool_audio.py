"""包裹工具v2"""

from typing import List, Optional


class WrapTool2:
    _instance: Optional["WrapTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def wrap(self, signal: List[float], length: int) -> List[float]:
        if not signal:
            return []
        result = []
        for i in range(length):
            result.append(signal[i % len(signal)])
        return result


def get_wrap_tool2() -> WrapTool2:
    return WrapTool2()
