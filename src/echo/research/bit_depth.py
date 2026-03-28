"""位深转换工具"""

import math
from typing import List, Optional


class BitDepth:
    _instance: Optional["BitDepth"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reduce(self, signal: List[float], bits: int) -> List[float]:
        levels = 2 ** bits
        return [math.floor(s * levels) / levels if s >= 0 else math.ceil(s * levels) / levels for s in signal]


def get_bit_depth() -> BitDepth:
    return BitDepth()
