"""扁平化工具"""

from typing import Optional, List, Any


class FlattenerTool:
    """扁平化工具"""

    def flatten(self, items: List[Any]) -> List[Any]:
        """扁平化"""
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result


_flattener_tool: Optional[FlattenerTool] = None


def get_flattener_tool() -> FlattenerTool:
    global _flattener_tool
    if _flattener_tool is None:
        _flattener_tool = FlattenerTool()
    return _flattener_tool