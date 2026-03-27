"""奇偶工具"""

from typing import Optional


class EvenOddTool:
    """奇偶工具"""

    def is_even(self, n: int) -> bool:
        """是否偶数"""
        return n % 2 == 0

    def is_odd(self, n: int) -> bool:
        """是否奇数"""
        return n % 2 != 0


_tool: Optional[EvenOddTool] = None


def get_evenodd_tool() -> EvenOddTool:
    global _tool
    if _tool is None:
        _tool = EvenOddTool()
    return _tool