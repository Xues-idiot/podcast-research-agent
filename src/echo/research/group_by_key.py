"""按键分组工具"""

from typing import List, Any, Callable, Dict


class GroupByKey:
    _instance: Optional["GroupByKey"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def group(self, items: List[Any], key_func: Callable) -> Dict[Any, List[Any]]:
        groups: Dict[Any, List[Any]] = {}
        for item in items:
            key = key_func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        return groups


def get_group_by_key() -> GroupByKey:
    return GroupByKey()
