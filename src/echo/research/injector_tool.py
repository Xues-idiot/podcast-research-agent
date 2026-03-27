"""Injector tool module - injects values into data structures"""

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar('T')


class InjectorTool:
    _instance: Optional["InjectorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def inject(self, data: Dict[str, Any], key: str, value: Any) -> Dict[str, Any]:
        """Inject a key-value pair into dictionary"""
        result = data.copy()
        result[key] = value
        return result

    def inject_nested(self, data: Dict[str, Any], keys: List[str], value: Any) -> Dict[str, Any]:
        """Inject value into nested dictionary structure"""
        result = data.copy()
        current = result
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value
        return result

    def merge_inject(self, base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
        """Merge updates into base dictionary"""
        result = base.copy()
        result.update(updates)
        return result

    def inject_many(self, data: Dict[str, Any], items: Dict[str, Any]) -> Dict[str, Any]:
        """Inject multiple key-value pairs"""
        result = data.copy()
        result.update(items)
        return result

    def inject_if(self, data: Dict[str, Any], key: str, value: Any, condition: Callable[[], bool]) -> Dict[str, Any]:
        """Inject value only if condition is true"""
        result = data.copy()
        if condition():
            result[key] = value
        return result


def get_injector_tool() -> InjectorTool:
    return InjectorTool()
