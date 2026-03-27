"""唯一生成工具"""

from typing import List, Any, Optional


class UniqueGen:
    _instance: Optional["UniqueGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def unique(self, items: List[Any]) -> List[Any]:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result


def get_unique_gen() -> UniqueGen:
    return UniqueGen()
