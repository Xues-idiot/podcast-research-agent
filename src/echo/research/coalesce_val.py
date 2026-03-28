"""空值合并工具"""

from typing import List, Any, Optional


class CoalesceTool:
    _instance: Optional["CoalesceTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def coalesce(self, *values: Any) -> Any:
        """返回第一个非None值"""
        for v in values:
            if v is not None:
                return v
        return None

    def if_none(self, value: Any, default: Any) -> Any:
        """None时返回默认值"""
        return value if value is not None else default

    def if_empty(self, items: List[Any], default: Any) -> Any:
        """空列表时返回默认值"""
        return items if items else default

    def or_default(self, value: Any, default: Any) -> Any:
        """为空时返回默认值"""
        return default if not value else value


_coalesce_instance: Optional[CoalesceTool] = None


def get_coalesce_tool() -> CoalesceTool:
    global _coalesce_instance
    if _coalesce_instance is None:
        _coalesce_instance = CoalesceTool()
    return _coalesce_instance