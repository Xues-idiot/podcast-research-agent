"""按大小分块工具"""

from typing import List, Optional, TypeVar


T = TypeVar("T")


class ChunkBySize:
    _instance: Optional["ChunkBySize"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chunk(self, items: List[T], size: int) -> List[List[T]]:
        return [items[i:i + size] for i in range(0, len(items), size)]

    def chunk_with_padding(self, items: List[T], size: int, pad: Optional[T] = None) -> List[List[T]]:
        result = []
        for i in range(0, len(items), size):
            chunk = items[i:i + size]
            if len(chunk) < size and pad is not None:
                chunk.extend([pad] * (size - len(chunk)))
            result.append(chunk)
        return result


def get_chunk_by_size() -> ChunkBySize:
    return ChunkBySize()
