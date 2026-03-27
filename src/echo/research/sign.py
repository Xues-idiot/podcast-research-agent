"""符号工具"""

from typing import Optional


class SignTool:
    """符号工具"""

    def sign(self, value: float) -> int:
        """获取符号"""
        if value > 0:
            return 1
        elif value < 0:
            return -1
        return 0

    def abs(self, value: float) -> float:
        """绝对值"""
        return abs(value)


_tool: Optional[SignTool] = None


def get_sign_tool() -> SignTool:
    global _tool
    if _tool is None:
        _tool = SignTool()
    return _tool