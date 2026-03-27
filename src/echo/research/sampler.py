"""采样工具"""

import random
from typing import Optional, Any


class Sampler:
    """采样工具"""

    def sample(self, items: list, count: int) -> list:
        """随机采样"""
        return random.sample(items, min(count, len(items)))

    def sample_with_replacement(self, items: list, count: int) -> list:
        """有放回采样"""
        return [random.choice(items) for _ in range(count)]


_sampler: Optional[Sampler] = None


def get_sampler() -> Sampler:
    global _sampler
    if _sampler is None:
        _sampler = Sampler()
    return _sampler