"""集合运算工具"""

from typing import Optional, Any


class Intersector:
    """集合运算工具"""

    def intersection(self, list1: list, list2: list) -> list:
        """交集"""
        return list(set(list1) & set(list2))

    def union(self, list1: list, list2: list) -> list:
        """并集"""
        return list(set(list1) | set(list2))

    def difference(self, list1: list, list2: list) -> list:
        """差集"""
        return list(set(list1) - set(list2))


_tool: Optional[Intersector] = None


def get_intersector() -> Intersector:
    global _tool
    if _tool is None:
        _tool = Intersector()
    return _tool