"""卡方检验工具"""

import math
from typing import List, Optional


class ChiSquareTest:
    _instance: Optional["ChiSquareTest"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chi_square(self, observed: List[float], expected: List[float]) -> Optional[float]:
        if len(observed) != len(expected) or len(observed) == 0:
            return None
        chi_sq = sum((o - e) ** 2 / e for o, e in zip(observed, expected) if e != 0)
        return chi_sq


def get_chi_square_test() -> ChiSquareTest:
    return ChiSquareTest()
