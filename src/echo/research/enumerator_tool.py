"""枚举工具"""

from typing import Optional, List, Any, Tuple


class EnumeratorTool:
    """枚举工具"""

    def enumerate_items(self, items: List[Any], start: int = 0) -> List[Tuple]:
        """枚举"""
        return list(enumerate(items, start))


_enumerator_tool: Optional[EnumeratorTool] = None


def get_enumerator_tool() -> EnumeratorTool:
    global _enumerator_tool
    if _enumerator_tool is None:
        _enumerator_tool = EnumeratorTool()
    return _enumerator_tool