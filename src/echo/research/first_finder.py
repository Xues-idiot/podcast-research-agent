"""第一个元素工具"""

from typing import Optional, List, Any


class FirstFinder:
    """第一个元素工具"""

    def first(self, items: List[Any]) -> Any:
        """第一个元素"""
        return items[0] if items else None


_first_finder: Optional[FirstFinder] = None


def get_first_finder() -> FirstFinder:
    global _first_finder
    if _first_finder is None:
        _first_finder = FirstFinder()
    return _first_finder