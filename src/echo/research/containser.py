"""包含检查工具"""

from typing import Optional, Any, List


class ContainserTool:
    """包含检查工具"""

    def contains(self, text: str, substring: str) -> bool:
        """检查是否包含子串"""
        return substring in text

    def contains_any(self, text: str, substrings: List[str]) -> bool:
        """检查是否包含任意子串"""
        return any(sub in text for sub in substrings)

    def contains_all(self, text: str, substrings: List[str]) -> bool:
        """检查是否包含所有子串"""
        return all(sub in text for sub in substrings)


_containser_tool: Optional[ContainserTool] = None


def get_containser_tool() -> ContainserTool:
    global _containser_tool
    if _containser_tool is None:
        _containser_tool = ContainserTool()
    return _containser_tool