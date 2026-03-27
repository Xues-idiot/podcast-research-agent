"""扁平化工具"""

from typing import Optional, Any


class FlattenTool:
    """扁平化工具"""

    def flatten(self, nested: list) -> list:
        """扁平化"""
        result = []
        for item in nested:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    def flatten_once(self, nested: list) -> list:
        """扁平化一层"""
        result = []
        for item in nested:
            if isinstance(item, list):
                result.extend(item)
            else:
                result.append(item)
        return result


_tool: Optional[FlattenTool] = None


def get_flatten_tool() -> FlattenTool:
    global _tool
    if _tool is None:
        _tool = FlattenTool()
    return _tool