"""伯努利分布计算器"""

from typing import Optional


class BernoulliCalc:
    _instance: Optional["BernoulliCalc"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pmf(self, k: int, p: float) -> float:
        if k == 0:
            return 1 - p
        elif k == 1:
            return p
        return 0.0

    def mean(self, p: float) -> float:
        return p

    def variance(self, p: float) -> float:
        return p * (1 - p)


def get_bernoulli_calc() -> BernoulliCalc:
    return BernoulliCalc()
