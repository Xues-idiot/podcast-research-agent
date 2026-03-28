"""窗函数工具"""

import math
from typing import List, Optional


class WindowFunctions:
    _instance: Optional["WindowFunctions"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def hann(self, n: int) -> List[float]:
        return [0.5 * (1 - math.cos(2 * math.pi * i / (n - 1))) for i in range(n)]

    def hamming(self, n: int) -> List[float]:
        return [0.54 - 0.46 * math.cos(2 * math.pi * i / (n - 1)) for i in range(n)]

    def blackman(self, n: int) -> List[float]:
        a0, a1, a2 = 0.42, 0.5, 0.08
        return [a0 - a1 * math.cos(2 * math.pi * i / (n - 1)) + a2 * math.cos(4 * math.pi * i / (n - 1)) for i in range(n)]


def get_window_functions() -> WindowFunctions:
    return WindowFunctions()
