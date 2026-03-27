"""Arranger tool for arranging items"""

from typing import Any, Callable, List, Optional, Tuple


class ArrangerTool:
    _instance: Optional["ArrangerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def arrange_in_grid(self, items: List[Any], num_columns: int) -> List[List[Any]]:
        """Arrange items in a grid"""
        if num_columns <= 0:
            return []
        grid: List[List[Any]] = []
        for i in range(0, len(items), num_columns):
            grid.append(items[i:i + num_columns])
        return grid

    def arrange_in_rows(self, items: List[Any], items_per_row: int) -> List[List[Any]]:
        """Arrange items into rows"""
        return self.arrange_in_grid(items, items_per_row)

    def arrange_in_columns(self, items: List[Any], num_columns: int) -> List[List[Any]]:
        """Arrange items into columns"""
        return self.arrange_in_grid(items, num_columns)

    def stagger(self, items: List[Any], stagger_size: int) -> List[List[Any]]:
        """Stagger items into overlapping groups"""
        if stagger_size <= 0:
            return []
        staggered: List[List[Any]] = []
        for i in range(len(items)):
            start = max(0, i - stagger_size + 1)
            staggered.append(items[start:i + 1])
        return staggered

    def pair_up(self, items: List[Any]) -> List[Tuple[Any, Any]]:
        """Pair up consecutive items"""
        pairs: List[Tuple[Any, Any]] = []
        for i in range(0, len(items) - 1, 2):
            pairs.append((items[i], items[i + 1]))
        return pairs

    def interleave(self, list1: List[Any], list2: List[Any]) -> List[Any]:
        """Interleave two lists"""
        result = []
        max_len = max(len(list1), len(list2))
        for i in range(max_len):
            if i < len(list1):
                result.append(list1[i])
            if i < len(list2):
                result.append(list2[i])
        return result

    def group_consecutive(self, items: List[Any], group_size: int) -> List[List[Any]]:
        """Group consecutive items"""
        if group_size <= 0:
            return []
        groups: List[List[Any]] = []
        for i in range(0, len(items), group_size):
            groups.append(items[i:i + group_size])
        return groups

    def process(self, data: Any) -> Any:
        """Process data by arranging"""
        return data


def get_arranger_tool() -> ArrangerTool:
    return ArrangerTool()