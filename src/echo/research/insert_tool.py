"""插入工具"""

from typing import Optional, List, Any


class InsertTool:
    """插入工具"""

    def insert(self, items: List[Any], index: int, item: Any) -> List[Any]:
        """插入元素"""
        return items[:index] + [item] + items[index:]


_insert_tool: Optional[InsertTool] = None


def get_insert_tool() -> InsertTool:
    global _insert_tool
    if _insert_tool is None:
        _insert_tool = InsertTool()
    return _insert_tool