"""分块生成工具"""

from typing import List, Any, Callable, Optional


class ChunkGen:
    _instance: Optional["ChunkGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chunk_by_size(self, items: List[Any], size: int) -> List[List[Any]]:
        return [items[i:i+size] for i in range(0, len(items), size)]

    def chunk_by_func(self, items: List[Any], func: Callable) -> List[List[Any]]:
        chunks = []
        current = []
        current_key = None
        for item in items:
            key = func(item)
            if current_key is None:
                current_key = key
            if key != current_key:
                chunks.append(current)
                current = []
                current_key = key
            current.append(item)
        if current:
            chunks.append(current)
        return chunks


def get_chunk_gen() -> ChunkGen:
    return ChunkGen()
