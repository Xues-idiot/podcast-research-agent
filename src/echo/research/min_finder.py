"""最小值查找工具"""

from typing import Optional, List, Any


class MinFinder:
    """最小值查找工具"""

    def min(self, items: List[Any]) -> Any:
        """最小值"""
        return min(items) if items else None


_min_finder: Optional[MinFinder] = None


def get_min_finder() -> MinFinder:
    global _min_finder
    if _min_finder is None:
        _min_finder = MinFinder()
    return _min_finder