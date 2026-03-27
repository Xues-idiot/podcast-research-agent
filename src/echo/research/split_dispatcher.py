"""Split dispatcher module - dispatches and splits data into parts"""

from typing import Any, Callable, List, Optional, TypeVar, Tuple

T = TypeVar('T')


class SplitDispatcher:
    _instance: Optional["SplitDispatcher"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def split(self, items: List[T], size: int) -> List[List[T]]:
        """Split list into chunks of specified size"""
        return [items[i:i + size] for i in range(0, len(items), size)]

    def split_by(self, items: List[T], predicate: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
        """Split list into two parts based on predicate"""
        matched = []
        unmatched = []
        for item in items:
            if predicate(item):
                matched.append(item)
            else:
                unmatched.append(item)
        return matched, unmatched

    def split_at(self, items: List[T], index: int) -> Tuple[List[T], List[T]]:
        """Split list at specific index"""
        return items[:index], items[index:]

    def split_by_keys(self, data: Dict[str, Any], keys: List[str]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Split dictionary by keys"""
        matched = {k: data.get(k) for k in keys if k in data}
        unmatched = {k: v for k, v in data.items() if k not in keys}
        return matched, unmatched

    def split_lines(self, text: str) -> List[str]:
        """Split text into lines"""
        return text.split('\n')

    def split_by_count(self, items: List[T], count: int) -> List[List[T]]:
        """Split list into specified number of parts"""
        if count <= 0:
            return [items]
        chunk_size = (len(items) + count - 1) // count
        return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def get_split_dispatcher() -> SplitDispatcher:
    return SplitDispatcher()
