"""空值检查工具"""

from typing import Optional, Any


class EmptinessChecker:
    """空值检查工具"""

    def is_empty(self, value: Any) -> bool:
        """是否为空"""
        if value is None:
            return True
        if isinstance(value, str):
            return len(value.strip()) == 0
        if isinstance(value, (list, dict, tuple, set)):
            return len(value) == 0
        return False

    def is_not_empty(self, value: Any) -> bool:
        """是否非空"""
        return not self.is_empty(value)


_checker: Optional[EmptinessChecker] = None


def get_emptiness_checker() -> EmptinessChecker:
    global _checker
    if _checker is None:
        _checker = EmptinessChecker()
    return _checker