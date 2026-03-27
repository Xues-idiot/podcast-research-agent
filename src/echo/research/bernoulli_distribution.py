"""伯努利分布工具"""

import random
from typing import Optional


class BernoulliDistribution:
    _instance: Optional["BernoulliDistribution"] = None

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

    def sample(self, p: float) -> int:
        return 1 if random.random() < p else 0


def get_bernoulli_distribution() -> BernoulliDistribution:
    return BernoulliDistribution()
