"""管道工具"""

from typing import Optional, Callable, Any


class PipelineTool:
    """管道工具"""

    def pipe(self, value: Any, *funcs: Callable) -> Any:
        """管道处理"""
        result = value
        for func in funcs:
            result = func(result)
        return result

    def compose(self, *funcs: Callable) -> Callable:
        """组合函数"""
        def composed(value):
            return self.pipe(value, *funcs)
        return composed


_pipeline: Optional[PipelineTool] = None


def get_pipeline_tool() -> PipelineTool:
    global _pipeline
    if _pipeline is None:
        _pipeline = PipelineTool()
    return _pipeline