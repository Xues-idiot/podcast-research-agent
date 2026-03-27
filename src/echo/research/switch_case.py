"""切换工具"""

from typing import Optional, Any, Dict


class SwitchCase:
    """切换工具"""

    def switch(self, value: Any, cases: Dict[Any, Callable]) -> Any:
        """切换执行"""
        if value in cases:
            return cases[value]()
        if "default" in cases:
            return cases["default"]()


_switch_case: Optional[SwitchCase] = None


def get_switch_case() -> SwitchCase:
    global _switch_case
    if _switch_case is None:
        _switch_case = SwitchCase()
    return _switch_case