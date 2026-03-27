"""组合计算器"""

from typing import Optional
import math


class CombinationCalculator:
    _instance: Optional["CombinationCalculator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def combinations(self, n: int, r: int) -> Optional[int]:
        if n < 0 or r < 0:
            return None
        if r > n:
            return None
        try:
            return math.comb(n, r)
        except ValueError:
            return None

    def permutations(self, n: int, r: int) -> Optional[int]:
        if n < 0 or r < 0:
            return None
        if r > n:
            return None
        try:
            return math.perm(n, r)
        except ValueError:
            return None


def get_combination_calculator() -> CombinationCalculator:
    return CombinationCalculator()
