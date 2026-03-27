"""列表数学工具"""

from typing import Optional


class ListMath:
    """列表数学工具"""

    def sum(self, items: list) -> float:
        """求和"""
        return sum(items)

    def product(self, items: list) -> float:
        """求积"""
        result = 1
        for i in items:
            result *= i
        return result

    def average(self, items: list) -> float:
        """平均值"""
        return sum(items) / len(items) if items else 0

    def min(self, items: list):
        """最小值"""
        return min(items) if items else None

    def max(self, items: list):
        """最大值"""
        return max(items) if items else None


_math: Optional[ListMath] = None


def get_list_math() -> ListMath:
    global _math
    if _math is None:
        _math = ListMath()
    return _math