"""打乱工具"""

import random
from typing import Optional, Any


class Shuffler:
    """打乱工具"""

    def shuffle(self, items: list) -> list:
        """打乱顺序"""
        result = items.copy()
        random.shuffle(result)
        return result

    def shuffle_in_place(self, items: list) -> None:
        """原地打乱"""
        random.shuffle(items)


_shuffler: Optional[Shuffler] = None


def get_shuffler() -> Shuffler:
    global _shuffler
    if _shuffler is None:
        _shuffler = Shuffler()
    return _shuffler