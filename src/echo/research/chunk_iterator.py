"""分块迭代器"""

from typing import Iterator, Iterable, Any, List, Optional


class ChunkIterator:
    _instance: Optional["ChunkIterator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chunks(self, iterable: Iterable, size: int) -> Iterator[List[Any]]:
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


def get_chunk_iterator() -> ChunkIterator:
    return ChunkIterator()
