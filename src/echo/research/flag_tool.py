"""标志工具"""

from typing import Optional


class FlagTool:
    """标志工具"""

    def __init__(self):
        self._flags = {}

    def set_flag(self, name: str, value: bool = True):
        """设置标志"""
        self._flags[name] = value

    def get_flag(self, name: str, default: bool = False) -> bool:
        """获取标志"""
        return self._flags.get(name, default)

    def toggle_flag(self, name: str) -> bool:
        """切换标志"""
        self._flags[name] = not self._flags.get(name, False)
        return self._flags[name]

    def clear_flag(self, name: str):
        """清除标志"""
        if name in self._flags:
            del self._flags[name]


_tool: Optional[FlagTool] = None


def get_flag_tool() -> FlagTool:
    global _tool
    if _tool is None:
        _tool = FlagTool()
    return _tool