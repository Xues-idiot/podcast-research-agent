"""重复工具"""

from typing import List, Any, Optional


class RepeatList:
    _instance: Optional["RepeatList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def repeat(self, item: Any, n: int) -> List[Any]:
        return [item] * n

    def cycle(self, items: List[Any], n: int) -> List[Any]:
        result = []
        for _ in range(n):
            result.extend(items)
        return result

    def replicate(self, item: Any, n: int) -> List[Any]:
        return self.repeat(item, n)


def get_repeat_list() -> RepeatList:
    return RepeatList()
