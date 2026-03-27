"""Selection router module - routes and selects items based on criteria"""

from typing import Any, Callable, List, Optional, TypeVar

T = TypeVar('T')


class SelectionRouter:
    _instance: Optional["SelectionRouter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def select(self, items: List[T], predicate: Callable[[T], bool]) -> List[T]:
        """Select items that match the predicate"""
        return [item for item in items if predicate(item)]

    def select_first(self, items: List[T], predicate: Callable[[T], bool]) -> Optional[T]:
        """Select first item matching predicate"""
        for item in items:
            if predicate(item):
                return item
        return None

    def select_nth(self, items: List[T], index: int) -> Optional[T]:
        """Select item at index"""
        return items[index] if 0 <= index < len(items) else None

    def select_unique(self, items: List[T]) -> List[T]:
        """Select unique items while preserving order"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def reject(self, items: List[T], predicate: Callable[[T], bool]) -> List[T]:
        """Reject items that match the predicate"""
        return [item for item in items if not predicate(item)]

    def select_by_index(self, items: List[T], indices: List[int]) -> List[T]:
        """Select items by their indices"""
        return [items[i] for i in indices if 0 <= i < len(items)]


def get_selection_router() -> SelectionRouter:
    return SelectionRouter()
