"""字典工具"""

from typing import Optional, Any


class DictUtils:
    """字典工具"""

    def get_nested(self, data: dict, path: str, default: Any = None) -> Any:
        """获取嵌套值"""
        keys = path.split('.')
        result = data
        for key in keys:
            if isinstance(result, dict) and key in result:
                result = result[key]
            else:
                return default
        return result

    def set_nested(self, data: dict, path: str, value: Any) -> dict:
        """设置嵌套值"""
        keys = path.split('.')
        current = data
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value
        return data

    def flatten(self, data: dict, prefix: str = "") -> dict:
        """扁平化"""
        result = {}
        for key, value in data.items():
            new_key = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                result.update(self.flatten(value, new_key))
            else:
                result[new_key] = value
        return result


_utils: Optional[DictUtils] = None


def get_dict_utils() -> DictUtils:
    global _utils
    if _utils is None:
        _utils = DictUtils()
    return _utils