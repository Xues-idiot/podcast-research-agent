"""扁平化工具"""

from typing import Optional, Any, List


class FlattenerTool:
    """扁平化工具"""

    def flatten(self, nested: List[Any]) -> List[Any]:
        """扁平化"""
        result = []
        for item in nested:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result


_flattener: Optional[FlattenerTool] = None


def get_flattener_tool() -> FlattenerTool:
    global _flattener
    if _flattener is None:
        _flattener = FlattenerTool()
    return _flattener