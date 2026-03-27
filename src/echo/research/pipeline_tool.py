"""管道工具"""

from typing import Optional, Callable, Any


class PipelineTool:
    """管道工具"""

    def pipe(self, value: Any, *funcs: Callable) -> Any:
        """管道执行"""
        result = value
        for func in funcs:
            result = func(result)
        return result


_pipeline_tool: Optional[PipelineTool] = None


def get_pipeline_tool() -> PipelineTool:
    global _pipeline_tool
    if _pipeline_tool is None:
        _pipeline_tool = PipelineTool()
    return _pipeline_tool