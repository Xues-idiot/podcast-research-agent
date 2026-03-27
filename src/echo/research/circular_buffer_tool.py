"""环形缓冲区工具"""

from typing import Optional, Any, List


class CircularBufferTool:
    """环形缓冲区工具"""

    def __init__(self, capacity: int = 10):
        self._capacity = capacity
        self._buffer: List[Any] = []
        self._index = 0

    def push(self, item: Any) -> None:
        """添加元素"""
        if len(self._buffer) < self._capacity:
            self._buffer.append(item)
        else:
            self._buffer[self._index] = item
        self._index = (self._index + 1) % self._capacity

    def get_all(self) -> List[Any]:
        """获取所有元素"""
        if len(self._buffer) < self._capacity:
            return list(self._buffer)
        return self._buffer[self._index:] + self._buffer[:self._index]


_circular_buffer_tool: Optional[CircularBufferTool] = None


def get_circular_buffer_tool() -> CircularBufferTool:
    global _circular_buffer_tool
    if _circular_buffer_tool is None:
        _circular_buffer_tool = CircularBufferTool()
    return _circular_buffer_tool