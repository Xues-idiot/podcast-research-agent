"""位 crushers效果器"""

import math
from typing import List, Optional


class Bitcrusher:
    _instance: Optional["Bitcrusher"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def apply(self, signal: List[float], bits: int = 8) -> List[float]:
        levels = 2 ** bits
        return [math.floor(s * levels) / levels if s >= 0 else math.ceil(s * levels) / levels for s in signal]


def get_bitcrusher() -> Bitcrusher:
    return Bitcrusher()
