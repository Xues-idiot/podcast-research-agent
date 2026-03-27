"""循环数组缓冲"""

from typing import List, Any, Optional


class BufferCircular:
    _instance: Optional["BufferCircular"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_data"):
            self._data: List[Any] = []
            self._size: int = 64

    def write(self, item: Any) -> None:
        if len(self._data) >= self._size:
            self._data.pop(0)
        self._data.append(item)

    def read(self) -> List[Any]:
        return self._data[:]


def get_buffer_circular() -> BufferCircular:
    return BufferCircular()
