"""空操作工具"""

from typing import Any, Optional


class NoopCallTool:
    _instance: Optional["NoopCallTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def noop(self, *args, **kwargs) -> None:
        pass

    def identity(self, value: Any) -> Any:
        return value


def get_noop_call_tool() -> NoopCallTool:
    return NoopCallTool()