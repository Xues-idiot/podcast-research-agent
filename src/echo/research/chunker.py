"""分块工具"""

from typing import Optional, Any


class ChunkerTool:
    """分块工具"""

    def chunk_list(self, items: list, size: int) -> list:
        """列表分块"""
        return [items[i:i+size] for i in range(0, len(items), size)]

    def chunk_dict(self, data: dict, size: int) -> list:
        """字典分块"""
        items = list(data.items())
        return [dict(items[i:i+size]) for i in range(0, len(items), size)]


_chunker: Optional[ChunkerTool] = None


def get_chunker_tool() -> ChunkerTool:
    global _chunker
    if _chunker is None:
        _chunker = ChunkerTool()
    return _chunker