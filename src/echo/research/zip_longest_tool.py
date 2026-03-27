"""Zip最长工具"""

from typing import Optional, List, Any, Tuple


class ZipLongestTool:
    """Zip最长工具"""

    def zip_longest(self, *lists: List[Any], fillvalue: Any = None) -> List[Tuple]:
        """Zip最长"""
        max_len = max(len(lst) for lst in lists)
        result = []
        for i in range(max_len):
            result.append(tuple(lst[i] if i < len(lst) else fillvalue for lst in lists))
        return result


_zip_longest_tool: Optional[ZipLongestTool] = None


def get_zip_longest_tool() -> ZipLongestTool:
    global _zip_longest_tool
    if _zip_longest_tool is None:
        _zip_longest_tool = ZipLongestTool()
    return _zip_longest_tool