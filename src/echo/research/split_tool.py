"""分割工具"""

from typing import Optional, List


class SplitTool:
    """分割工具"""

    def split(self, text: str, delimiter: str = None) -> List[str]:
        """分割"""
        return text.split(delimiter)


_split_tool: Optional[SplitTool] = None


def get_split_tool() -> SplitTool:
    global _split_tool
    if _split_tool is None:
        _split_tool = SplitTool()
    return _split_tool