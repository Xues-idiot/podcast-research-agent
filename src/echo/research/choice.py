"""选择工具"""

from typing import Optional, Any


class ChoiceTool:
    """选择工具"""

    def choice(self, *options) -> Any:
        """随机选择"""
        import random
        return random.choice(options)

    def weighted_choice(self, options: list, weights: list) -> Any:
        """加权选择"""
        import random
        return random.choices(options, weights=weights)[0]


_tool: Optional[ChoiceTool] = None


def get_choice_tool() -> ChoiceTool:
    global _tool
    if _tool is None:
        _tool = ChoiceTool()
    return _tool