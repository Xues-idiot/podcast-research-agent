"""开关工具"""

from typing import Optional, Any, Callable


class SwitchTool:
    """开关工具"""

    def switch(self, value: Any, cases: dict, default: Any = None) -> Any:
        """switch语句"""
        return cases.get(value, default)


_tool: Optional[SwitchTool] = None


def get_switch_tool() -> SwitchTool:
    global _tool
    if _tool is None:
        _tool = SwitchTool()
    return _tool