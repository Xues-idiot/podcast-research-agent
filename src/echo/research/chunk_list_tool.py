"""列表分块工具"""

from typing import Optional, List, Any


class ChunkListTool:
    """列表分块工具"""

    def chunk_list(self, items: List[Any], size: int) -> List[List[Any]]:
        """分块列表"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_chunk_list_tool: Optional[ChunkListTool] = None


def get_chunk_list_tool() -> ChunkListTool:
    global _chunk_list_tool
    if _chunk_list_tool is None:
        _chunk_list_tool = ChunkListTool()
    return _chunk_list_tool