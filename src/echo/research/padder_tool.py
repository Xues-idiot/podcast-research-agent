"""填充工具"""

from typing import Optional


class PadderTool:
    """填充工具"""

    def pad_left(self, text: str, width: int, char: str = " ") -> str:
        """左填充"""
        return text.rjust(width, char)

    def pad_right(self, text: str, width: int, char: str = " ") -> str:
        """右填充"""
        return text.ljust(width, char)


_padder_tool: Optional[PadderTool] = None


def get_padder_tool() -> PadderTool:
    global _padder_tool
    if _padder_tool is None:
        _padder_tool = PadderTool()
    return _padder_tool