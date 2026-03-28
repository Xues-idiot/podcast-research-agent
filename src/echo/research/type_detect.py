"""类型检测工具"""

from typing import Any, Optional


class TypeDetectTool:
    _instance: Optional["TypeDetectTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def detect(self, value: Any) -> str:
        """检测类型"""
        return type(value).__name__

    def is_primitive(self, value: Any) -> bool:
        """是否为原始类型"""
        return isinstance(value, (int, float, str, bool, type(None)))

    def is_collection(self, value: Any) -> bool:
        """是否为集合类型"""
        return isinstance(value, (list, tuple, set, dict))

    def is_sequence(self, value: Any) -> bool:
        """是否为序列类型"""
        return isinstance(value, (list, tuple, str))

    def is_truthy(self, value: Any) -> bool:
        """是否为真值"""
        return bool(value)

    def is_falsy(self, value: Any) -> bool:
        """是否为假值"""
        return not value


_type_detect_instance: Optional[TypeDetectTool] = None


def get_type_detect_tool() -> TypeDetectTool:
    global _type_detect_instance
    if _type_detect_instance is None:
        _type_detect_instance = TypeDetectTool()
    return _type_detect_instance