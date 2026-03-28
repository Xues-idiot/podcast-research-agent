"""深拷贝工具"""

from typing import Any, Optional
import copy


class CopyDeepTool:
    _instance: Optional["CopyDeepTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def deep_copy(self, obj: Any) -> Any:
        """深拷贝"""
        return copy.deepcopy(obj)

    def shallow_copy(self, obj: Any) -> Any:
        """浅拷贝"""
        if isinstance(obj, list):
            return [x for x in obj]
        if isinstance(obj, dict):
            return {k: v for k, v in obj.items()}
        return obj

    def recursive_copy(self, obj: Any) -> Any:
        """递归拷贝"""
        return copy.deepcopy(obj)


_copy_instance: Optional[CopyDeepTool] = None


def get_copy_deep_tool() -> CopyDeepTool:
    global _copy_instance
    if _copy_instance is None:
        _copy_instance = CopyDeepTool()
    return _copy_instance