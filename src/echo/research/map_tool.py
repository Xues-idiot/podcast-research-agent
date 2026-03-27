"""映射工具"""

from typing import Optional, List, Any, Callable


class MapTool:
    """映射工具"""

    def map_items(self, items: List[Any], func: Callable) -> List[Any]:
        """映射"""
        return [func(item) for item in items]


_map_tool: Optional[MapTool] = None


def get_map_tool() -> MapTool:
    global _map_tool
    if _map_tool is None:
        _map_tool = MapTool()
    return _map_tool