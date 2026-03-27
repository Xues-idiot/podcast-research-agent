"""Sorter tool for sorting items"""

from typing import Any, Callable, List, Optional, Tuple


class SorterTool:
    _instance: Optional["SorterTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sort(self, items: List[Any], key_func: Callable[[Any], Any] = None, reverse: bool = False) -> List[Any]:
        """Sort items"""
        return sorted(items, key=key_func, reverse=reverse)

    def sort_by_multiple_keys(self, items: List[Any], key_funcs: List[Callable[[Any], Any]]) -> List[Any]:
        """Sort by multiple keys in order"""
        def multi_key(item):
            return tuple(func(item) for func in key_funcs)
        return sorted(items, key=multi_key)

    def sort_stable(self, items: List[Any], key_func: Callable[[Any], Any] = None) -> List[Any]:
        """Stable sort that preserves equal elements order"""
        return sorted(items, key=key_func)

    def partition(self, items: List[Any], predicate: Callable[[Any], bool]) -> Tuple[List[Any], List[Any]]:
        """Partition items by predicate"""
        left = []
        right = []
        for item in items:
            if predicate(item):
                left.append(item)
            else:
                right.append(item)
        return left, right

    def sort_descending(self, items: List[Any], key_func: Callable[[Any], Any] = None) -> List[Any]:
        """Sort in descending order"""
        return sorted(items, key=key_func, reverse=True)

    def nlargest(self, items: List[Any], n: int, key_func: Callable[[Any], Any] = None) -> List[Any]:
        """Get n largest items"""
        return sorted(items, key=key_func, reverse=True)[:n]

    def nsmallest(self, items: List[Any], n: int, key_func: Callable[[Any], Any] = None) -> List[Any]:
        """Get n smallest items"""
        return sorted(items, key=key_func)[:n]

    def process(self, data: Any) -> Any:
        """Process data by sorting"""
        return data


def get_sorter_tool() -> SorterTool:
    return SorterTool()