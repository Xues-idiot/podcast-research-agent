"""分块工具"""

from typing import Optional, Any


class ChunkMaker:
    """分块工具"""

    def chunk(self, items: list, size: int) -> list:
        """分块"""
        return [items[i:i+size] for i in range(0, len(items), size)]

    def chunk_by_count(self, items: list, count: int) -> list:
        """按数量分块"""
        size = (len(items) + count - 1) // count
        return [items[i*size:(i+1)*size] for i in range(count)]


_maker: Optional[ChunkMaker] = None


def get_chunk_maker() -> ChunkMaker:
    global _maker
    if _maker is None:
        _maker = ChunkMaker()
    return _maker