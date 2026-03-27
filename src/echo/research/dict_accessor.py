"""字典访问工具"""

from typing import Optional, Any


class DictAccessor:
    """字典访问工具"""

    def get(self, data: dict, key: str, default: Any = None) -> Any:
        """获取值"""
        return data.get(key, default)

    def get_nested(self, data: dict, path: str, default: Any = None) -> Any:
        """获取嵌套值"""
        keys = path.split(".")
        result = data
        for key in keys:
            if isinstance(result, dict) and key in result:
                result = result[key]
            else:
                return default
        return result


_accessor: Optional[DictAccessor] = None


def get_dict_accessor() -> DictAccessor:
    global _accessor
    if _accessor is None:
        _accessor = DictAccessor()
    return _accessor