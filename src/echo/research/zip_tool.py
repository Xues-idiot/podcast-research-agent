"""Zip工具"""

from typing import Optional, List, Any


class ZipTool:
    """Zip工具"""

    def zip_lists(self, *lists: List[Any]) -> List[tuple]:
        """合并列表"""
        return list(zip(*lists))


_zip_tool: Optional[ZipTool] = None


def get_zip_tool() -> ZipTool:
    global _zip_tool
    if _zip_tool is None:
        _zip_tool = ZipTool()
    return _zip_tool