"""求和工具"""

from typing import Optional, List


class Summer:
    """求和工具"""

    def sum(self, items: List[float]) -> float:
        """求和"""
        return sum(items)


_summer: Optional[Summer] = None


def get_summer() -> Summer:
    global _summer
    if _summer is None:
        _summer = Summer()
    return _summer