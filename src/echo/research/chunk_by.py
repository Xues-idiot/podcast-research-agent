"""滑动计数工具"""

from typing import List, Any, Callable, Optional


class ChunkBy:
    _instance: Optional["ChunkBy"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chunk_by_size(self, items: List[Any], size: int) -> List[List[Any]]:
        return [items[i:i + size] for i in range(0, len(items), size)]

    def chunk_by_pred(self, items: List[Any], pred: Callable) -> List[List[Any]]:
        result = []
        current = []
        for item in items:
            if pred(item) and current:
                result.append(current)
                current = []
            else:
                current.append(item)
        if current:
            result.append(current)
        return result


def get_chunk_by() -> ChunkBy:
    return ChunkBy()
