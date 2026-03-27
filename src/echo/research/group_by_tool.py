"""按键分组工具"""

from typing import Callable, Dict, List, Optional, TypeVar


T = TypeVar("T")
K = TypeVar("K")


class GroupByTool:
    _instance: Optional["GroupByTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def group_by(self, items: List[T], key_func: Callable[[T], K]) -> Dict[K, List[T]]:
        groups: Dict[K, List[T]] = {}
        for item in items:
            key = key_func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        return groups

    def group_by_multi(self, items: List[T], key_funcs: List[Callable[[T], K]]) -> Dict[K, "GroupByTool"]:
        return self.group_by(items, lambda x: tuple(k(x) for k in key_funcs))


def get_group_by_tool() -> GroupByTool:
    return GroupByTool()
