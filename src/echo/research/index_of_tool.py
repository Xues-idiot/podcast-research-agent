"""索引查找工具"""

from typing import Optional, List, Any


class IndexOfTool:
    """索引查找工具"""

    def index_of(self, items: List[Any], item: Any) -> int:
        """查找索引"""
        try:
            return items.index(item)
        except ValueError:
            return -1


_index_of_tool: Optional[IndexOfTool] = None


def get_index_of_tool() -> IndexOfTool:
    global _index_of_tool
    if _index_of_tool is None:
        _index_of_tool = IndexOfTool()
    return _index_of_tool