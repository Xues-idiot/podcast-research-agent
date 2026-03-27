"""采样生成工具"""

import random
from typing import List, Any, Optional


class SampleGen:
    _instance: Optional["SampleGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sample(self, items: List[Any], count: int, replace: bool = False) -> List[Any]:
        if replace:
            return random.choices(items, k=count)
        return random.sample(items, min(count, len(items)))


def get_sample_gen() -> SampleGen:
    return SampleGen()
