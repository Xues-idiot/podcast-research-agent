"""打乱工具"""

import random
from typing import List, Any, Optional


class ShuffleList:
    _instance: Optional["ShuffleList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def shuffle(self, items: List[Any]) -> List[Any]:
        result = items.copy()
        random.shuffle(result)
        return result

    def shuffle_inplace(self, items: List[Any]) -> None:
        random.shuffle(items)


def get_shuffle_list() -> ShuffleList:
    return ShuffleList()
