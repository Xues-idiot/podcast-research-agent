"""恒等工具"""

from typing import Optional, Any


class IdentityTool:
    """恒等工具"""

    def identity(self, value: Any) -> Any:
        """返回原值"""
        return value


_identity_tool: Optional[IdentityTool] = None


def get_identity_tool() -> IdentityTool:
    global _identity_tool
    if _identity_tool is None:
        _identity_tool = IdentityTool()
    return _identity_tool