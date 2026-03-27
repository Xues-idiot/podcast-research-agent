"""切换工具"""

from typing import Optional, Any


class FlipFlopTool:
    """切换工具"""

    def __init__(self):
        self._state = False

    def toggle(self) -> bool:
        """切换状态"""
        self._state = not self._state
        return self._state

    def get(self) -> bool:
        """获取状态"""
        return self._state


_tool: Optional[FlipFlopTool] = None


def get_flipflop_tool() -> FlipFlopTool:
    global _tool
    if _tool is None:
        _tool = FlipFlopTool()
    return _tool