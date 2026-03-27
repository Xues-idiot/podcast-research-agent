"""位运算工具"""

from typing import Optional


class BitwiseTool:
    """位运算工具"""

    def and_(self, a: int, b: int) -> int:
        """与"""
        return a & b

    def or_(self, a: int, b: int) -> int:
        """或"""
        return a | b

    def xor(self, a: int, b: int) -> int:
        """异或"""
        return a ^ b

    def not_(self, a: int) -> int:
        """非"""
        return ~a

    def shift_left(self, a: int, bits: int) -> int:
        """左移"""
        return a << bits

    def shift_right(self, a: int, bits: int) -> int:
        """右移"""
        return a >> bits


_tool: Optional[BitwiseTool] = None


def get_bitwise_tool() -> BitwiseTool:
    global _tool
    if _tool is None:
        _tool = BitwiseTool()
    return _tool