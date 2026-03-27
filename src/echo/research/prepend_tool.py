"""前置工具"""

from typing import Optional, List, Any


class PrependTool:
    """前置工具"""

    def prepend(self, items: List[Any], item: Any) -> List[Any]:
        """前置元素"""
        return [item] + items


_prepend_tool: Optional[PrependTool] = None


def get_prepend_tool() -> PrependTool:
    global _prepend_tool
    if _prepend_tool is None:
        _prepend_tool = PrependTool()
    return _prepend_tool