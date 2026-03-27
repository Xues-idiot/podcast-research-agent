"""恒等函数工具"""

from typing import Optional, Any


class IdentityTool:
    """恒等函数工具"""

    def identity(self, x: Any) -> Any:
        """返回输入"""
        return x

    def constant(self, x: Any) -> callable:
        """返回常量函数"""
        return lambda _: x


_tool: Optional[IdentityTool] = None


def get_identity_tool() -> IdentityTool:
    global _tool
    if _tool is None:
        _tool = IdentityTool()
    return _tool