"""环形缓冲区"""

from typing import List, Any, Optional


class RingBuffer:
    _instance: Optional["RingBuffer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_buffer"):
            self._buffer: List[Any] = []
            self._size: int = 10
            self._index: int = 0

    def push(self, item: Any) -> None:
        if len(self._buffer) < self._size:
            self._buffer.append(item)
        else:
            self._buffer[self._index] = item
        self._index = (self._index + 1) % self._size

    def get_all(self) -> List[Any]:
        if len(self._buffer) < self._size:
            return self._buffer[:]
        return self._buffer[self._index:] + self._buffer[:self._index]


def get_ring_buffer() -> RingBuffer:
    return RingBuffer()
