"""计数器工具"""

from typing import Optional


class Counter:
    """计数器工具"""

    def __init__(self):
        self._counts = {}

    def increment(self, name: str, delta: int = 1) -> int:
        """递增计数"""
        self._counts[name] = self._counts.get(name, 0) + delta
        return self._counts[name]

    def decrement(self, name: str, delta: int = 1) -> int:
        """递减计数"""
        self._counts[name] = self._counts.get(name, 0) - delta
        return self._counts[name]

    def get(self, name: str) -> int:
        """获取计数"""
        return self._counts.get(name, 0)

    def reset(self, name: str):
        """重置计数"""
        if name in self._counts:
            del self._counts[name]

    def clear(self):
        """清空所有计数"""
        self._counts.clear()


_counter: Optional[Counter] = None


def get_counter() -> Counter:
    global _counter
    if _counter is None:
        _counter = Counter()
    return _counter