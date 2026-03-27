"""负二项分布工具"""

import math
from typing import Optional


class NegativeBinomial:
    _instance: Optional["NegativeBinomial"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pmf(self, k: int, r: int, p: float) -> float:
        if k < r:
            return 0.0
        return math.comb(k - 1, r - 1) * (p ** r) * ((1 - p) ** (k - r))

    def mean(self, r: int, p: float) -> float:
        return r / p


def get_negative_binomial() -> NegativeBinomial:
    return NegativeBinomial()
