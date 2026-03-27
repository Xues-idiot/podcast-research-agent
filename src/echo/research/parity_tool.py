"""奇偶工具"""

from typing import Optional


class ParityTool:
    """奇偶工具"""

    def is_even(self, value: int) -> bool:
        """是否为偶数"""
        return value % 2 == 0

    def is_odd(self, value: int) -> bool:
        """是否为奇数"""
        return value % 2 != 0

    def make_even(self, value: int) -> int:
        """转为偶数"""
        return value if self.is_even(value) else value + 1

    def make_odd(self, value: int) -> int:
        """转为奇数"""
        return value if self.is_odd(value) else value + 1


_parity_tool: Optional[ParityTool] = None


def get_parity_tool() -> ParityTool:
    global _parity_tool
    if _parity_tool is None:
        _parity_tool = ParityTool()
    return _parity_tool