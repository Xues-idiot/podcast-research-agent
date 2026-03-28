"""反转工具"""

from typing import List, Any, Optional


class ReverseItemsTool:
    _instance: Optional["ReverseItemsTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reverse_list(self, items: List[Any]) -> List[Any]:
        """反转列表"""
        return list(reversed(items))

    def reverse_string(self, s: str) -> str:
        """反转字符串"""
        return s[::-1]

    def reverse_tuple(self, t: tuple) -> tuple:
        """反转元组"""
        return t[::-1]

    def reverse_dict(self, d: dict) -> dict:
        """反转字典(键值互换)"""
        return {v: k for k, v in d.items()}

    def palindrome_check(self, s: str) -> bool:
        """回文检查"""
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]


_reverse_instance: Optional[ReverseItemsTool] = None


def get_reverse_items_tool() -> ReverseItemsTool:
    global _reverse_instance
    if _reverse_instance is None:
        _reverse_instance = ReverseItemsTool()
    return _reverse_instance