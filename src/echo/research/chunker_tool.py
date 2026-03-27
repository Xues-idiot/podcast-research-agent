"""分块工具"""

from typing import Optional, List, Any


class ChunkerTool:
    """分块工具"""

    def chunk(self, items: List[Any], size: int) -> List[List[Any]]:
        """分块"""
        return [items[i:i+size] for i in range(0, len(items), size)]


_chunker_tool: Optional[ChunkerTool] = None


def get_chunker_tool() -> ChunkerTool:
    global _chunker_tool
    if _chunker_tool is None:
        _chunker_tool = ChunkerTool()
    return _chunker_tool