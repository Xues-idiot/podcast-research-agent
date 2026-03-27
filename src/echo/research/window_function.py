"""窗函数工具"""

import math
from typing import List


class WindowFunction:
    _instance: Optional["WindowFunction"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def hamming(self, n: int) -> List[float]:
        return [0.54 - 0.46 * math.cos(2 * math.pi * i / (n - 1)) for i in range(n)]

    def hanning(self, n: int) -> List[float]:
        return [0.5 - 0.5 * math.cos(2 * math.pi * i / (n - 1)) for i in range(n)]

    def blackman(self, n: int) -> List[float]:
        return [0.42 - 0.5 * math.cos(2 * math.pi * i / (n - 1)) + 0.08 * math.cos(4 * math.pi * i / (n - 1)) for i in range(n)]


def get_window_function() -> WindowFunction:
    return WindowFunction()
