"""深拷贝工具"""

import copy
from typing import Optional, Any


class DeepCopyTool:
    """深拷贝工具"""

    def deepcopy(self, obj: Any) -> Any:
        """深拷贝"""
        return copy.deepcopy(obj)


_deepcopy_tool: Optional[DeepCopyTool] = None


def get_deepcopy_tool() -> DeepCopyTool:
    global _deepcopy_tool
    if _deepcopy_tool is None:
        _deepcopy_tool = DeepCopyTool()
    return _deepcopy_tool