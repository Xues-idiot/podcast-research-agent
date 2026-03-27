"""Pipeline walker module - walks through pipeline steps sequentially"""

from typing import Any, Callable, List, Optional


class PipelineWalker:
    _instance: Optional["PipelineWalker"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def walk(self, steps: List[Callable[[Any], Any]], initial_data: Any) -> Any:
        """Walk through pipeline steps sequentially"""
        result = initial_data
        for step in steps:
            result = step(result)
        return result

    def walk_with_index(self, steps: List[Callable[[int, Any], Any]], initial_data: Any) -> Any:
        """Walk through pipeline steps with index"""
        result = initial_data
        for i, step in enumerate(steps):
            result = step(i, result)
        return result

    def walk_until(self, steps: List[Callable[[Any], Any]], initial_data: Any, condition: Callable[[Any], bool]) -> Any:
        """Walk through steps until condition is met"""
        result = initial_data
        for step in steps:
            result = step(result)
            if condition(result):
                break
        return result


def get_pipeline_walker() -> PipelineWalker:
    return PipelineWalker()
