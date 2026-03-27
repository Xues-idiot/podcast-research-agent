"""深度扁平化"""

from typing import List, Any


class FlattenDeep:
    _instance: Optional["FlattenDeep"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flatten(self, items: List[Any]) -> List[Any]:
        result = []
        for item in items:
            if isinstance(item, (list, tuple)):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result


def get_flatten_deep() -> FlattenDeep:
    return FlattenDeep()
