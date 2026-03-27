"""序列生成工具"""

from typing import Optional, Any


class SequenceGen:
    """序列生成工具"""

    def repeat(self, value: Any, count: int) -> list:
        """重复值"""
        return [value] * count

    def cycle(self, items: list, count: int) -> list:
        """循环"""
        result = []
        for _ in range(count):
            result.extend(items)
        return result


_gen: Optional[SequenceGen] = None


def get_sequence_gen() -> SequenceGen:
    global _gen
    if _gen is None:
        _gen = SequenceGen()
    return _gen