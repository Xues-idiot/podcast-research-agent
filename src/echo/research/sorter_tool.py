"""排序工具"""

from typing import Optional, Callable, Any


class SortTool:
    """排序工具"""

    def sort_by(self, items: list, key_func: Callable, reverse: bool = False) -> list:
        """按键排序"""
        return sorted(items, key=key_func, reverse=reverse)

    def sort(self, items: list, reverse: bool = False) -> list:
        """排序"""
        return sorted(items, reverse=reverse)


_sorter: Optional[SortTool] = None


def get_sort_tool() -> SortTool:
    global _sorter
    if _sorter is None:
        _sorter = SortTool()
    return _sorter