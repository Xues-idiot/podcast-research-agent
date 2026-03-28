"""随机种子工具"""

import random
from typing import Optional


class RandomSeedTool:
    _instance: Optional["RandomSeedTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_seed(self, seed: int) -> None:
        random.seed(seed)

    def get_random(self, start: int = 0, end: int = 100) -> int:
        return random.randint(start, end)

    def get_random_float(self) -> float:
        return random.random()


def get_random_seed_tool() -> RandomSeedTool:
    return RandomSeedTool()