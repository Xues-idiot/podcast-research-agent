"""默认值工具"""

from typing import Optional, Any


class DefaultsTool:
    """默认值工具"""

    def default(self, value: Any, default_val: Any) -> Any:
        """默认值"""
        return value if value is not None else default_val


_defaults_tool: Optional[DefaultsTool] = None


def get_defaults_tool() -> DefaultsTool:
    global _defaults_tool
    if _defaults_tool is None:
        _defaults_tool = DefaultsTool()
    return _defaults_tool