"""超几何分布计算器"""

import math
from typing import Optional


class Hypergeometric:
    _instance: Optional["Hypergeometric"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def probability(self, N: int, K: int, n: int, k: int) -> float:
        if k < 0 or k > min(n, K) or k > n:
            return 0.0
        return (math.comb(K, k) * math.comb(N - K, n - k)) / math.comb(N, n)


def get_hypergeometric() -> Hypergeometric:
    return Hypergeometric()
