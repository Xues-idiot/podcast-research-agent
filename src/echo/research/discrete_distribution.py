"""离散分布工具"""

import random
from typing import List, Optional


class DiscreteDistribution:
    _instance: Optional["DiscreteDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sample(self, values: List[float], probabilities: List[float]) -> Optional[float]:
        if len(values) != len(probabilities):
            return None
        if sum(probabilities) != 1.0:
            probabilities = [p / sum(probabilities) for p in probabilities]
        return random.choices(values, weights=probabilities, k=1)[0]


def get_discrete_distribution() -> DiscreteDistribution:
    return DiscreteDistribution()
