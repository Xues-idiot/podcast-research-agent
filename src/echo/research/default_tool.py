"""默认值工具"""

from typing import Optional, Any


class DefaultTool:
    """默认值工具"""

    def default(self, value: Any, default_value: Any) -> Any:
        """默认值"""
        return value if value is not None else default_value

    def nil(self, value: Any, default_value: Any) -> Any:
        """nil时默认值"""
        return default_value if value is None else value


_tool: Optional[DefaultTool] = None


def get_default_tool() -> DefaultTool:
    global _tool
    if _tool is None:
        _tool = DefaultTool()
    return _tool