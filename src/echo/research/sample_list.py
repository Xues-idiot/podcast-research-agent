"""采样工具"""

import random
from typing import List, Any, Optional


class SampleList:
    _instance: Optional["SampleList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sample(self, items: List[Any], n: int, replace: bool = False) -> List[Any]:
        if replace:
            return random.choices(items, k=n)
        return random.sample(items, min(n, len(items)))

    def sample_one(self, items: List[Any]) -> Any:
        if not items:
            return None
        return random.choice(items)


def get_sample_list() -> SampleList:
    return SampleList()
