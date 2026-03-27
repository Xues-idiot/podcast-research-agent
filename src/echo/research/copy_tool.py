"""复制工具"""

from typing import Optional, Any


class CopyTool:
    """复制工具"""

    def copy(self, obj: Any) -> Any:
        """复制"""
        if isinstance(obj, list):
            return list(obj)
        if isinstance(obj, dict):
            return dict(obj)
        return obj


_copy_tool: Optional[CopyTool] = None


def get_copy_tool() -> CopyTool:
    global _copy_tool
    if _copy_tool is None:
        _copy_tool = CopyTool()
    return _copy_tool