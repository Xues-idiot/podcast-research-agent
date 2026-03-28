"""偏移工具v2"""

from typing import List, Optional


class ShiftTool:
    _instance: Optional["ShiftTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shift(self, signal: List[float], samples: int) -> List[float]:
        if samples > 0:
            return [0.0] * samples + signal[:-samples]
        elif samples < 0:
            return signal[-samples:] + [0.0] * (-samples)
        return signal


def get_shift_tool() -> ShiftTool:
    return ShiftTool()
