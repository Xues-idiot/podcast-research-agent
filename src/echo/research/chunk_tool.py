"""分块工具"""

from typing import Optional, List, Any


class ChunkTool:
    """分块工具"""

    def chunk(self, items: List[Any], size: int) -> List[List[Any]]:
        """分块"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_chunk_tool: Optional[ChunkTool] = None


def get_chunk_tool() -> ChunkTool:
    global _chunk_tool
    if _chunk_tool is None:
        _chunk_tool = ChunkTool()
    return _chunk_tool