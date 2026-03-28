"""管道执行工具"""

from typing import List, Callable, Any, Optional


class PipeExecTool:
    _instance: Optional["PipeExecTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pipe(self, value: Any, funcs: List[Callable]) -> Any:
        result = value
        for func in funcs:
            result = func(result)
        return result


def get_pipe_exec_tool() -> PipeExecTool:
    return PipeExecTool()