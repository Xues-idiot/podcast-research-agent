"""最大值查找工具"""

from typing import Optional, List, Any


class MaxFinder:
    """最大值查找工具"""

    def max(self, items: List[Any]) -> Any:
        """最大值"""
        return max(items) if items else None


_max_finder: Optional[MaxFinder] = None


def get_max_finder() -> MaxFinder:
    global _max_finder
    if _max_finder is None:
        _max_finder = MaxFinder()
    return _max_finder