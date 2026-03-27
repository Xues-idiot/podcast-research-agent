"""深度扁平化工具"""

from typing import Optional, List, Any


class FlattenDeepTool:
    """深度扁平化工具"""

    def flatten_deep(self, items: List[Any]) -> List[Any]:
        """深度扁平化"""
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(self.flatten_deep(item))
            else:
                result.append(item)
        return result


_flatten_deep_tool: Optional[FlattenDeepTool] = None


def get_flatten_deep_tool() -> FlattenDeepTool:
    global _flatten_deep_tool
    if _flatten_deep_tool is None:
        _flatten_deep_tool = FlattenDeepTool()
    return _flatten_deep_tool