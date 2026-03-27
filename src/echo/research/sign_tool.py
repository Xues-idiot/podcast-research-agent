"""符号工具"""

from typing import Optional


class SignTool:
    """符号工具"""

    def sign(self, value: float) -> int:
        """获取符号"""
        if value > 0:
            return 1
        if value < 0:
            return -1
        return 0

    def is_positive(self, value: float) -> bool:
        """是否为正"""
        return value > 0

    def is_negative(self, value: float) -> bool:
        """是否为负"""
        return value < 0

    def abs_value(self, value: float) -> float:
        """绝对值"""
        return abs(value)


_sign_tool: Optional[SignTool] = None


def get_sign_tool() -> SignTool:
    global _sign_tool
    if _sign_tool is None:
        _sign_tool = SignTool()
    return _sign_tool