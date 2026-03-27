"""重复工具"""

from typing import Optional, List, Any


class RepeatTool:
    """重复工具"""

    def repeat(self, item: Any, times: int) -> List[Any]:
        """重复"""
        return [item] * times


_repeat_tool: Optional[RepeatTool] = None


def get_repeat_tool() -> RepeatTool:
    global _repeat_tool
    if _repeat_tool is None:
        _repeat_tool = RepeatTool()
    return _repeat_tool