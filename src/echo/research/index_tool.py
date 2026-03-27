"""索引工具"""

from typing import Optional, List, Any


class IndexTool:
    """索引工具"""

    def index(self, items: List[Any], item: Any) -> int:
        """索引"""
        try:
            return items.index(item)
        except ValueError:
            return -1


_index_tool: Optional[IndexTool] = None


def get_index_tool() -> IndexTool:
    global _index_tool
    if _index_tool is None:
        _index_tool = IndexTool()
    return _index_tool