"""打乱生成工具"""

import random
from typing import List, Any, Optional


class ShuffleGen:
    _instance: Optional["ShuffleGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shuffle(self, items: List[Any]) -> List[Any]:
        result = items.copy()
        random.shuffle(result)
        return result


def get_shuffle_gen() -> ShuffleGen:
    return ShuffleGen()
