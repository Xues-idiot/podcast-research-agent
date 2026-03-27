"""重新索引工具"""

from typing import List, Any, Dict


class ReindexTool:
    _instance: Optional["ReindexTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def reindex(self, items: List[Any], start: int = 0) -> Dict[int, Any]:
        return {i + start: item for i, item in enumerate(items)}


def get_reindex_tool() -> ReindexTool:
    return ReindexTool()
