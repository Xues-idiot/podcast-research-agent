"""谓词分块工具"""

from typing import Callable, List, Optional, TypeVar


T = TypeVar("T")


class ChunkByPredicate:
    _instance: Optional["ChunkByPredicate"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def chunk_by(self, items: List[T], predicate: Callable[[T], bool]) -> List[List[T]]:
        result = []
        current_chunk = []

        for item in items:
            if not current_chunk:
                current_chunk.append(item)
            elif predicate(item) == predicate(current_chunk[0]):
                current_chunk.append(item)
            else:
                result.append(current_chunk)
                current_chunk = [item]

        if current_chunk:
            result.append(current_chunk)

        return result

    def chunk_while(self, items: List[T], predicate: Callable[[T, T], bool]) -> List[List[T]]:
        if not items:
            return []

        result = []
        current_chunk = [items[0]]

        for item in items[1:]:
            if predicate(current_chunk[-1], item):
                current_chunk.append(item)
            else:
                result.append(current_chunk)
                current_chunk = [item]

        if current_chunk:
            result.append(current_chunk)

        return result


def get_chunk_by_predicate() -> ChunkByPredicate:
    return ChunkByPredicate()
