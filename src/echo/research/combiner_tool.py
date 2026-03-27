"""Combiner tool module - combines data in various ways"""

from typing import Any, Callable, List, Optional, TypeVar, Dict

T = TypeVar('T')


class CombinerTool:
    _instance: Optional["CombinerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def combine(self, *items: T) -> List[T]:
        """Combine multiple items into a list"""
        return list(items)

    def combine_lists(self, *lists: List[T]) -> List[T]:
        """Combine multiple lists into one"""
        result = []
        for lst in lists:
            result.extend(lst)
        return result

    def zip_combine(self, *lists: List[T]) -> List[Tuple[Any, ...]]:
        """Combine lists element-wise into tuples"""
        return list(zip(*lists))

    def dict_combine(self, *dicts: Dict[str, Any]) -> Dict[str, Any]:
        """Combine multiple dictionaries"""
        result = {}
        for d in dicts:
            result.update(d)
        return result

    def pair_combine(self, items: List[T]) -> List[Tuple[T, T]]:
        """Combine items into consecutive pairs"""
        return [(items[i], items[i + 1]) for i in range(len(items) - 1)]

    def combine_with(self, items: List[T], combiner: Callable[[T, T], T]) -> T:
        """Combine all items using a custom combiner function"""
        if not items:
            return None
        result = items[0]
        for item in items[1:]:
            result = combiner(result, item)
        return result


def get_combiner_tool() -> CombinerTool:
    return CombinerTool()
