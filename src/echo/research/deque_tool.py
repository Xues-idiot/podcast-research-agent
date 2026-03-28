"""双端队列工具"""

from typing import List, Any, Optional


class DequeTool:
    _instance: Optional["DequeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._items: List[Any] = []

    def append_left(self, item: Any) -> None:
        """左侧添加"""
        self._items.insert(0, item)

    def append_right(self, item: Any) -> None:
        """右侧添加"""
        self._items.append(item)

    def pop_left(self) -> Any:
        """左侧移除"""
        if not self._items:
            return None
        return self._items.pop(0)

    def pop_right(self) -> Any:
        """右侧移除"""
        if not self._items:
            return None
        return self._items.pop()

    def peek_left(self) -> Any:
        """查看左侧"""
        return self._items[0] if self._items else None

    def peek_right(self) -> Any:
        """查看右侧"""
        return self._items[-1] if self._items else None

    def size(self) -> int:
        """大小"""
        return len(self._items)

    def is_empty(self) -> bool:
        """是否空"""
        return len(self._items) == 0

    def clear(self) -> None:
        """清空"""
        self._items.clear()

    def rotate(self, n: int) -> None:
        """旋转n步"""
        if not self._items:
            return
        n = n % len(self._items)
        if n > 0:
            self._items = self._items[-n:] + self._items[:-n]
        elif n < 0:
            self._items = self._items[-n:] + self._items[:-n]


_deque_instance: Optional[DequeTool] = None


def get_deque_tool() -> DequeTool:
    global _deque_instance
    if _deque_instance is None:
        _deque_instance = DequeTool()
    return _deque_instance