"""排列检验工具"""

import random
from typing import List, Optional


class PermutationTest:
    _instance: Optional["PermutationTest"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def permute(self, data: List[float], n: int) -> List[List[float]]:
        result = []
        for _ in range(n):
            shuffled = data[:]
            random.shuffle(shuffled)
            result.append(shuffled)
        return result


def get_permutation_test() -> PermutationTest:
    return PermutationTest()
