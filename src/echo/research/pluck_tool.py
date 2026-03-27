"""提取工具"""

from typing import List, Any, Callable


class PluckTool:
    _instance: Optional["PluckTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pluck(self, items: List[Any], key: str) -> List[Any]:
        return [item[key] if hasattr(item, key) else None for item in items]


def get_pluck_tool() -> PluckTool:
    return PluckTool()
