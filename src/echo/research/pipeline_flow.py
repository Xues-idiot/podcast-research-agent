"""管道工具"""

from typing import Any, Callable, List, Optional


class PipelineFlow:
    _instance: Optional["PipelineFlow"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pipeline(self, value: Any, *funcs: Callable) -> Any:
        result = value
        for func in funcs:
            result = func(result)
        return result

    def compose(self, *funcs: Callable) -> Callable:
        def composed(value):
            result = value
            for func in reversed(funcs):
                result = func(result)
            return result
        return composed

    def pipe(self, value: Any) -> "PipelineBuilder":
        return PipelineBuilder(value)


class PipelineBuilder:
    def __init__(self, value: Any):
        self._value = value
        self._steps: List[Callable] = []

    def pipe(self, func: Callable) -> "PipelineBuilder":
        self._steps.append(func)
        return self

    def execute(self) -> Any:
        result = self._value
        for step in self._steps:
            result = step(result)
        return result


def get_pipeline_flow() -> PipelineFlow:
    return PipelineFlow()
