"""克隆工具"""

import copy
from typing import Optional, Any


class ClonerTool:
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


_cloner_tool: Optional[ClonerTool] = None


def get_cloner_tool() -> ClonerTool:
    global _cloner_tool
    if _cloner_tool is None:
        _cloner_tool = ClonerTool()
    return _cloner_tool