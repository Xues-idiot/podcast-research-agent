"""组合计算器"""

import math
from typing import Optional


class CombinationCalc:
    _instance: Optional["CombinationCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def combination(self, n: int, r: int) -> int:
        if r > n or r < 0:
            return 0
        return math.comb(n, r)

    def permutation(self, n: int, r: int) -> int:
        if r > n or r < 0:
            return 0
        return math.perm(n, r)


def get_combination_calc() -> CombinationCalc:
    return CombinationCalc()
