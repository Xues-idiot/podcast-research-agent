"""蹦床工具"""

from typing import Any, Callable, Optional


class TrampolineTool:
    _instance: Optional["TrampolineTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trampoline(self, func: Callable, *args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    def bounce(self, func: Callable) -> Callable:
        def bounced(*args, **kwargs):
            return self.trampoline(func, *args, **kwargs)
        return bounced


def get_trampoline_tool() -> TrampolineTool:
    return TrampolineTool()
