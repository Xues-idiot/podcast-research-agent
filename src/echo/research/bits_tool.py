"""位运算工具"""

from typing import Optional


class BitsTool:
    _instance: Optional["BitsTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def and_(self, a: int, b: int) -> int:
        return a & b

    def or_(self, a: int, b: int) -> int:
        return a | b

    def xor(self, a: int, b: int) -> int:
        return a ^ b

    def not_(self, a: int) -> int:
        return ~a

    def lshift(self, a: int, b: int) -> int:
        return a << b

    def rshift(self, a: int, b: int) -> int:
        return a >> b


def get_bits_tool() -> BitsTool:
    return BitsTool()
