"""枚举工具"""

from typing import Optional, Any


class EnumeratorTool:
    """枚举工具"""

    def enumerate_items(self, items: list, start: int = 0) -> list:
        """枚举"""
        return list(enumerate(items, start))

    def with_index(self, items: list, start: int = 0) -> list:
        """带索引"""
        return [{"index": i + start, "item": item} for i, item in enumerate(items)]


_enumerator: Optional[EnumeratorTool] = None


def get_enumerator_tool() -> EnumeratorTool:
    global _enumerator
    if _enumerator is None:
        _enumerator = EnumeratorTool()
    return _enumerator