"""步骤运行器"""

from typing import Any, Callable, Dict, List, Optional


class StepRunner:
    _instance: Optional["StepRunner"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def run_steps(self, steps: List[Dict[str, Any]], initial_value: Any = None) -> Any:
        result = initial_value
        for step in steps:
            func = step.get("func")
            if func:
                result = func(result)
        return result

    def run_conditional(self, conditions: List[Dict[str, Any]], value: Any) -> Any:
        for condition in conditions:
            if condition.get("when", lambda v: True)(value):
                return condition.get("do", lambda v: v)(value)
        return value


def get_step_runner() -> StepRunner:
    return StepRunner()
