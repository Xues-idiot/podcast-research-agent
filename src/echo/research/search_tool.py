"""搜索工具"""

from typing import List, Any, Optional, Callable


class SearchTool:
    _instance: Optional["SearchTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def linear_search(self, items: List[Any], target: Any) -> int:
        """线性搜索"""
        for i, item in enumerate(items):
            if item == target:
                return i
        return -1

    def binary_search(self, items: List[Any], target: Any) -> int:
        """二分搜索(需有序列表)"""
        left, right = 0, len(items) - 1
        while left <= right:
            mid = (left + right) // 2
            if items[mid] == target:
                return mid
            elif items[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def binary_search_range(self, items: List[tuple], target: Any, key: Callable = None) -> int:
        """基于范围的二分搜索"""
        if key is None:
            key = lambda x: x
        left, right = 0, len(items) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            val = key(items[mid])
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def find_all(self, items: List[Any], predicate: Callable[[Any], bool]) -> List[int]:
        """查找所有满足条件的索引"""
        return [i for i, item in enumerate(items) if predicate(item)]

    def find_min(self, items: List[Any], key: Callable = None) -> Any:
        """找最小值"""
        if not items:
            return None
        return min(items, key=key)

    def find_max(self, items: List[Any], key: Callable = None) -> Any:
        """找最大值"""
        if not items:
            return None
        return max(items, key=key)


_search_instance: Optional[SearchTool] = None


def get_search_tool() -> SearchTool:
    global _search_instance
    if _search_instance is None:
        _search_instance = SearchTool()
    return _search_instance