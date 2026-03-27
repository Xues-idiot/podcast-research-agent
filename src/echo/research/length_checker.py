"""长度检查工具"""

from typing import Optional, List, Any


class LengthChecker:
    """长度检查工具"""

    def length(self, items: List[Any]) -> int:
        """长度"""
        return len(items)


_length_checker: Optional[LengthChecker] = None


def get_length_checker() -> LengthChecker:
    global _length_checker
    if _length_checker is None:
        _length_checker = LengthChecker()
    return _length_checker