"""混合模型工具"""

import random
from typing import List, Callable, Optional, Any


class MixtureModel:
    _instance: Optional["MixtureModel"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sample(self, distributions: List[Callable], weights: List[float]) -> Any:
        if len(distributions) != len(weights):
            return None
        total = sum(weights)
        normalized = [w / total for w in weights]
        idx = random.choices(range(len(distributions)), weights=normalized, k=1)[0]
        return distributions[idx]()


def get_mixture_model() -> MixtureModel:
    return MixtureModel()
