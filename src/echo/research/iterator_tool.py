"""迭代器工具"""

from typing import Iterator, Iterable, Any, List, Optional


class IteratorTool:
    _instance: Optional["IteratorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chunk_iter(self, iterable: Iterable, size: int) -> Iterator[List[Any]]:
        it = iter(iterable)
        while True:
            chunk = []
            for _ in range(size):
                try:
                    chunk.append(next(it))
                except StopIteration:
                    break
            if chunk:
                yield chunk
            else:
                return

    def flatten_iter(self, iterable: Iterable) -> Iterator[Any]:
        for item in iterable:
            if isinstance(item, (list, tuple)):
                yield from self.flatten_iter(item)
            else:
                yield item


def get_iterator_tool() -> IteratorTool:
    return IteratorTool()
