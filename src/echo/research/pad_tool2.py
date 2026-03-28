"""填充工具v2"""

from typing import List, Optional


class PadTool2:
    _instance: Optional["PadTool2"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pad(self, signal: List[float], length: int, value: float = 0.0) -> List[float]:
        if len(signal) >= length:
            return signal[:length]
        return signal + [value] * (length - len(signal))


def get_pad_tool2() -> PadTool2:
    return PadTool2()
