"""环形缓冲区"""

from typing import Optional, Any


class CircularBuffer:
    """环形缓冲区"""

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._size = 0

    def push(self, item: Any):
        """添加"""
        self._buffer[self._head] = item
        self._head = (self._head + 1) % self._capacity
        self._size = min(self._size + 1, self._capacity)

    def to_list(self) -> list:
        """转列表"""
        if self._size < self._capacity:
            return self._buffer[:self._size]
        return self._buffer[self._head:] + self._buffer[:self._head]


_buffer: Optional[CircularBuffer] = None


def get_circular_buffer(capacity: int = 10) -> CircularBuffer:
    global _buffer
    if _buffer is None:
        _buffer = CircularBuffer(capacity)
    return _buffer