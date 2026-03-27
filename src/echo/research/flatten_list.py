"""扁平化工具"""

from typing import List, Any, Optional


class FlattenList:
    _instance: Optional["FlattenList"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flatten(self, items: List[Any]) -> List[Any]:
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    def flatten_once(self, items: List[List[Any]]) -> List[Any]:
        return [item for sublist in items for item in sublist]


def get_flatten_list() -> FlattenList:
    return FlattenList()
