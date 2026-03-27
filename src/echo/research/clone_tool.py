"""克隆工具"""

import copy
from typing import Optional, Any


class CloneTool:
    """克隆工具"""

    def shallow_clone(self, obj: Any) -> Any:
        """浅克隆"""
        if isinstance(obj, list):
            return list(obj)
        if isinstance(obj, dict):
            return dict(obj)
        return obj

    def deep_clone(self, obj: Any) -> Any:
        """深克隆"""
        return copy.deepcopy(obj)


_clone_tool: Optional[CloneTool] = None


def get_clone_tool() -> CloneTool:
    global _clone_tool
    if _clone_tool is None:
        _clone_tool = CloneTool()
    return _clone_tool