"""随机数工具"""

from typing import Optional
import random


class RandomGen:
    """随机数工具"""

    def random_int(self, min_val: int, max_val: int) -> int:
        """随机整数"""
        return random.randint(min_val, max_val)

    def random_float(self, min_val: float = 0.0, max_val: float = 1.0) -> float:
        """随机浮点数"""
        return random.uniform(min_val, max_val)

    def random_bool(self) -> bool:
        """随机布尔"""
        return random.choice([True, False])


_gen: Optional[RandomGen] = None


def get_random_gen() -> RandomGen:
    global _gen
    if _gen is None:
        _gen = RandomGen()
    return _gen