"""随机选择工具"""

import random
from typing import Optional


class RandomPicker:
    """随机选择工具"""

    def pick_one(self, items: list) -> any:
        """随机选一个"""
        if not items:
            return None
        return random.choice(items)

    def pick_multiple(self, items: list, count: int) -> list:
        """随机选多个"""
        if not items or count <= 0:
            return []
        return random.sample(items, min(count, len(items)))

    def shuffle(self, items: list) -> list:
        """打乱顺序"""
        result = items.copy()
        random.shuffle(result)
        return result


_picker: Optional[RandomPicker] = None


def get_random_picker() -> RandomPicker:
    global _picker
    if _picker is None:
        _picker = RandomPicker()
    return _picker