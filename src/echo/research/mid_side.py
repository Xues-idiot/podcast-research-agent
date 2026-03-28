"""Mid-Side编码工具"""

from typing import List, Optional


class MidSide:
    _instance: Optional["MidSide"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def encode(self, left: List[float], right: List[float]) -> tuple[List[float], List[float]]:
        mid = [(l + r) / 2 for l, r in zip(left, right)]
        side = [(l - r) / 2 for l, r in zip(left, right)]
        return mid, side

    def decode(self, mid: List[float], side: List[float]) -> tuple[List[float], List[float]]:
        left = [m + s for m, s in zip(mid, side)]
        right = [m - s for m, s in zip(mid, side)]
        return left, right


def get_mid_side() -> MidSide:
    return MidSide()
