"""开关工具"""

from typing import Optional, Any, Dict


class SwitchTool:
    """开关工具"""

    def __init__(self):
        self._cases: Dict[Any, Any] = {}

    def add_case(self, key: Any, value: Any) -> None:
        """添加用例"""
        self._cases[key] = value

    def get(self, key: Any, default: Any = None) -> Any:
        """获取值"""
        return self._cases.get(key, default)


_switch_tool: Optional[SwitchTool] = None


def get_switch_tool() -> SwitchTool:
    global _switch_tool
    if _switch_tool is None:
        _switch_tool = SwitchTool()
    return _switch_tool