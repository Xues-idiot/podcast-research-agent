"""组合键工具"""

from typing import Optional, List, Tuple


class ComboKeyTool:
    """组合键工具"""

    def make_combo(self, *keys) -> Tuple:
        """创建组合键"""
        return tuple(keys)

    def is_same_combo(self, combo1: Tuple, combo2: Tuple) -> bool:
        """检查组合键是否相同"""
        return combo1 == combo2

    def combo_to_str(self, combo: Tuple) -> str:
        """组合键转字符串"""
        return "+".join(str(k) for k in combo)


_combo_key_tool: Optional[ComboKeyTool] = None


def get_combo_key_tool() -> ComboKeyTool:
    global _combo_key_tool
    if _combo_key_tool is None:
        _combo_key_tool = ComboKeyTool()
    return _combo_key_tool