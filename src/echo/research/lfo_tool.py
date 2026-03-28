"""低频振荡器工具"""

import math
from typing import List, Optional


class LfoTool:
    _instance: Optional["LfoTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sine(self, freq: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [math.sin(2 * math.pi * freq * i / sample_rate) for i in range(n)]

    def triangle(self, freq: float, duration_ms: int, sample_rate: float = 44100) -> List[float]:
        n = int(duration_ms * sample_rate / 1000)
        return [2 * abs(2 * (freq * i / sample_rate % 1) - 1) - 1 for i in range(n)]


def get_lfo_tool() -> LfoTool:
    return LfoTool()
