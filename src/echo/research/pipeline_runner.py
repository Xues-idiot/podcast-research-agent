"""管道运行器"""

from typing import List, Callable, Any, Optional


class PipelineRunner:
    _instance: Optional["PipelineRunner"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pipe(self, value: Any, *functions: Callable) -> Any:
        result = value
        for func in functions:
            result = func(result)
        return result


def get_pipeline_runner() -> PipelineRunner:
    return PipelineRunner()
