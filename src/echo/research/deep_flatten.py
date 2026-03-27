"""深度扁平化工具"""

from typing import Any, List, Optional


class DeepFlatten:
    _instance: Optional["DeepFlatten"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flatten(self, items: List[Any], depth: Optional[int] = None) -> List[Any]:
        result = []

        def _flatten(lst: List[Any], current_depth: int):
            for item in lst:
                if isinstance(item, list):
                    if depth is None or current_depth < depth:
                        _flatten(item, current_depth + 1)
                    else:
                        result.append(item)
                else:
                    result.append(item)

        _flatten(items, 0)
        return result

    def flatten_once(self, items: List[Any]) -> List[Any]:
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(item)
            else:
                result.append(item)
        return result


def get_deep_flatten() -> DeepFlatten:
    return DeepFlatten()
