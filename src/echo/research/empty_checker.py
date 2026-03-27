"""空检查工具"""

from typing import Optional, Any


class EmptyChecker:
    """空检查工具"""

    def is_empty(self, value: Any) -> bool:
        """是否为空"""
        if value is None:
            return True
        if isinstance(value, (str, list, dict, tuple, set)):
            return len(value) == 0
        return False


_empty_checker: Optional[EmptyChecker] = None


def get_empty_checker() -> EmptyChecker:
    global _empty_checker
    if _empty_checker is None:
        _empty_checker = EmptyChecker()
    return _empty_checker