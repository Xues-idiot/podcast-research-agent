"""管道构建器"""

from typing import Any, Callable, List, Optional


class PipelineBuilder:
    _instance: Optional["PipelineBuilder"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._steps: List[Callable] = []

    def add(self, func: Callable) -> "PipelineBuilder":
        self._steps.append(func)
        return self

    def build(self) -> Callable:
        def pipeline(value: Any) -> Any:
            result = value
            for step in self._steps:
                result = step(result)
            return result
        return pipeline


def get_pipeline_builder() -> PipelineBuilder:
    return PipelineBuilder()
