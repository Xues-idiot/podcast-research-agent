"""类型检测工具"""

from typing import Optional, Any


class TypeDetector:
    """类型检测工具"""

    def is_string(self, value: Any) -> bool:
        """是否为字符串"""
        return isinstance(value, str)

    def is_number(self, value: Any) -> bool:
        """是否为数字"""
        return isinstance(value, (int, float))

    def is_boolean(self, value: Any) -> bool:
        """是否为布尔值"""
        return isinstance(value, bool)

    def is_list(self, value: Any) -> bool:
        """是否为列表"""
        return isinstance(value, list)

    def is_dict(self, value: Any) -> bool:
        """是否为字典"""
        return isinstance(value, dict)


_detector: Optional[TypeDetector] = None


def get_type_detector() -> TypeDetector:
    global _detector
    if _detector is None:
        _detector = TypeDetector()
    return _detector