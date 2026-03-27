"""分支切换工具"""

from typing import Callable, Any, Dict


class SwitchCaseTool:
    _instance: Optional["SwitchCaseTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def switch(self, value: Any, cases: Dict[Any, Callable], default: Callable = None) -> Any:
        if value in cases:
            return cases[value]()
        if default:
            return default()
        return None


def get_switch_case_tool() -> SwitchCaseTool:
    return SwitchCaseTool()
