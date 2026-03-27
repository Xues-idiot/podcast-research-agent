"""列表工具"""

from typing import Optional


class ListUtils:
    """列表工具"""

    def unique(self, items: list) -> list:
        """去重保持顺序"""
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def chunk(self, items: list, chunk_size: int) -> list[list]:
        """分块"""
        return [items[i:i+chunk_size] for i in range(0, len(items), chunk_size)]

    def flatten(self, nested: list[list]) -> list:
        """扁平化"""
        return [item for sublist in nested for item in sublist]

    def intersection(self, list1: list, list2: list) -> list:
        """交集"""
        return list(set(list1) & set(list2))

    def union(self, list1: list, list2: list) -> list:
        """并集"""
        return list(set(list1) | set(list2))

    def difference(self, list1: list, list2: list) -> list:
        """差集"""
        return list(set(list1) - set(list2))


_utils: Optional[ListUtils] = None


def get_list_utils() -> ListUtils:
    global _utils
    if _utils is None:
        _utils = ListUtils()
    return _utils