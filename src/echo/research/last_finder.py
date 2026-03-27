"""最后一个元素工具"""

from typing import Optional, List, Any


class LastFinder:
    """最后一个元素工具"""

    def last(self, items: List[Any]) -> Any:
        """最后一个元素"""
        return items[-1] if items else None


_last_finder: Optional[LastFinder] = None


def get_last_finder() -> LastFinder:
    global _last_finder
    if _last_finder is None:
        _last_finder = LastFinder()
    return _last_finder