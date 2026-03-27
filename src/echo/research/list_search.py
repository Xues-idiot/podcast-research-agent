"""列表搜索工具"""

from typing import Optional, Any


class ListSearch:
    """列表搜索工具"""

    def find_first(self, items: list, predicate) -> Any:
        """查找第一个匹配"""
        for item in items:
            if predicate(item):
                return item
        return None

    def find_all(self, items: list, predicate) -> list:
        """查找所有匹配"""
        return [item for item in items if predicate(item)]

    def find_index(self, items: list, predicate) -> int:
        """查找索引"""
        for i, item in enumerate(items):
            if predicate(item):
                return i
        return -1


_search: Optional[ListSearch] = None


def get_list_search() -> ListSearch:
    global _search
    if _search is None:
        _search = ListSearch()
    return _search