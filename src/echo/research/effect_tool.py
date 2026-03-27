"""副作用工具"""

from typing import Any, Callable, Optional


class EffectTool:
    _instance: Optional["EffectTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def side_effect(self, func: Callable, *args, **kwargs) -> Any:
        return func(*args, **kwargs)

    def tap(self, value: Any, func: Callable) -> Any:
        func(value)
        return value

    def trace(self, label: str, value: Any) -> Any:
        print(f"{label}: {value}")
        return value


def get_effect_tool() -> EffectTool:
    return EffectTool()
