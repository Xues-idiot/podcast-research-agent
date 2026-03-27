"""累加器"""

from typing import Optional


class Accumulator:
    """累加器"""

    def __init__(self):
        self._total = 0
        self._count = 0

    def add(self, value: float) -> float:
        """添加并返回累加和"""
        self._total += value
        self._count += 1
        return self._total

    def get_total(self) -> float:
        """获取累加和"""
        return self._total

    def get_count(self) -> int:
        """获取计数"""
        return self._count

    def get_average(self) -> float:
        """获取平均值"""
        return self._total / self._count if self._count else 0

    def reset(self):
        """重置"""
        self._total = 0
        self._count = 0


_accumulator: Optional[Accumulator] = None


def get_accumulator() -> Accumulator:
    global _accumulator
    if _accumulator is None:
        _accumulator = Accumulator()
    return _accumulator