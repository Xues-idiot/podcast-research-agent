"""压缩工具"""

from typing import Optional, Any, List


class ZipTool:
    """压缩工具"""

    def zip_lists(self, *lists: List) -> List[tuple]:
        """压缩列表"""
        return list(zip(*lists))

    def unzip(self, pairs: List[tuple]) -> tuple:
        """解压缩"""
        return tuple(list(x) for x in zip(*pairs))


_zipper: Optional[ZipTool] = None


def get_zip_tool() -> ZipTool:
    global _zipper
    if _zipper is None:
        _zipper = ZipTool()
    return _zipper