"""排序工具"""

from typing import List, Any, Optional, Callable


class SortTool:
    _instance: Optional["SortTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def bubble_sort(self, items: List[Any], key: Callable = None, reverse: bool = False) -> List[Any]:
        """冒泡排序"""
        result = list(items)
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                a = key(result[j]) if key else result[j]
                b = key(result[j + 1]) if key else result[j + 1]
                if (a > b) == (not reverse):
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

    def quick_sort(self, items: List[Any], key: Callable = None, reverse: bool = False) -> List[Any]:
        """快速排序"""
        if len(items) <= 1:
            return list(items)
        pivot = items[len(items) // 2]
        pivot_val = key(pivot) if key else pivot
        left = [x for x in items if (key(x) if key else x) < pivot_val]
        middle = [x for x in items if (key(x) if key else x) == pivot_val]
        right = [x for x in items if (key(x) if key else x) > pivot_val]
        result = self.quick_sort(left, key, reverse) + middle + self.quick_sort(right, key, reverse)
        if reverse:
            return result[::-1]
        return result

    def insertion_sort(self, items: List[Any], key: Callable = None, reverse: bool = False) -> List[Any]:
        """插入排序"""
        result = list(items)
        for i in range(1, len(result)):
            key_val = key(result[i]) if key else result[i]
            j = i - 1
            while j >= 0 and (key(result[j]) if key else result[j]) > key_val == (not reverse):
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = items[i]
        return result

    def sorted_by(self, items: List[dict], field: str, reverse: bool = False) -> List[dict]:
        """按字段排序字典列表"""
        return sorted(items, key=lambda x: x.get(field), reverse=reverse)


_sort_instance: Optional[SortTool] = None


def get_sort_tool() -> SortTool:
    global _sort_instance
    if _sort_instance is None:
        _sort_instance = SortTool()
    return _sort_instance