"""更新工具"""

from typing import Optional, Any, Dict


class UpdateTool:
    """更新工具"""

    def update(self, data: Dict, updates: Dict) -> Dict:
        """更新字典"""
        result = dict(data)
        result.update(updates)
        return result


_update_tool: Optional[UpdateTool] = None


def get_update_tool() -> UpdateTool:
    global _update_tool
    if _update_tool is None:
        _update_tool = UpdateTool()
    return _update_tool