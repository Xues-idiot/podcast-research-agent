"""字典工具集合"""
from typing import Any, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class DictResult:
    result: Dict[Any, Any]
    count: int


def dict_get(d: Dict[Any, Any], key: Any, default: Any = None) -> Any:
    """获取字典值"""
    return d.get(key, default)


def dict_set(d: Dict[Any, Any], key: Any, value: Any) -> Dict[Any, Any]:
    """设置字典值"""
    result = dict(d)
    result[key] = value
    return result


def dict_delete(d: Dict[Any, Any], key: Any) -> Dict[Any, Any]:
    """删除字典键"""
    result = dict(d)
    if key in result:
        del result[key]
    return result


def dict_keys(d: Dict[Any, Any]) -> List[Any]:
    """获取所有键"""
    return list(d.keys())


def dict_values(d: Dict[Any, Any]) -> List[Any]:
    """获取所有值"""
    return list(d.values())


def dict_items(d: Dict[Any, Any]) -> List[tuple]:
    """获取所有键值对"""
    return list(d.items())


def dict_merge(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """合并多个字典"""
    result = {}
    for d in dicts:
        result.update(d)
    return result


def dict_filter(d: Dict[Any, Any], keys: List[Any]) -> Dict[Any, Any]:
    """保留指定键"""
    return {k: v for k, v in d.items() if k in keys}


def dict_exclude(d: Dict[Any, Any], keys: List[Any]) -> Dict[Any, Any]:
    """排除指定键"""
    return {k: v for k, v in d.items() if k not in keys}


def dict_invert(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """反转字典键值"""
    return {v: k for k, v in d.items()}


def dict_flatten(d: Dict[Any, Any], separator: str = ".") -> Dict[str, Any]:
    """扁平化嵌套字典"""
    result = {}
    def _flatten(obj, prefix=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                _flatten(v, f"{prefix}{separator}{k}" if prefix else k)
        else:
            result[prefix] = obj
    _flatten(d)
    return result

