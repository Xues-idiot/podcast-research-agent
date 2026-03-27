"""删除工具"""

from typing import Optional, List, Any


class DeleteTool:
    """删除工具"""

    def delete(self, items: List[Any], index: int) -> List[Any]:
        """删除元素"""
        if 0 <= index < len(items):
            return items[:index] + items[index+1:]
        return list(items)


_delete_tool: Optional[DeleteTool] = None


def get_delete_tool() -> DeleteTool:
    global _delete_tool
    if _delete_tool is None:
        _delete_tool = DeleteTool()
    return _delete_tool