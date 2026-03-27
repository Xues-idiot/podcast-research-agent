"""位运算工具"""

from typing import Optional


class BitwiseTool:
    """位运算工具"""

    def and_(self, a: int, b: int) -> int:
        """按位与"""
        return a & b

    def or_(self, a: int, b: int) -> int:
        """按位或"""
        return a | b

    def xor(self, a: int, b: int) -> int:
        """按位异或"""
        return a ^ b

    def shift_left(self, value: int, bits: int) -> int:
        """左移"""
        return value << bits

    def shift_right(self, value: int, bits: int) -> int:
        """右移"""
        return value >> bits


_bitwise_tool: Optional[BitwiseTool] = None


def get_bitwise_tool() -> BitwiseTool:
    global _bitwise_tool
    if _bitwise_tool is None:
        _bitwise_tool = BitwiseTool()
    return _bitwise_tool