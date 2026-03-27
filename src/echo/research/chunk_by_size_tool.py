"""按大小分块工具"""

from typing import Optional, List, Any


class ChunkBySizeTool:
    """按大小分块工具"""

    def chunk_by_size(self, items: List[Any], size: int) -> List[List[Any]]:
        """按大小分块"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_chunk_by_size_tool: Optional[ChunkBySizeTool] = None


def get_chunk_by_size_tool() -> ChunkBySizeTool:
    global _chunk_by_size_tool
    if _chunk_by_size_tool is None:
        _chunk_by_size_tool = ChunkBySizeTool()
    return _chunk_by_size_tool