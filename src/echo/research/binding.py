"""绑定工具"""

from typing import Optional, Callable, Any


class BindingTool:
    """绑定工具"""

    def bind_first(self, func: Callable, first_arg: Any) -> Callable:
        """绑定第一个参数"""
        def bound(*args, **kwargs):
            return func(first_arg, *args, **kwargs)
        return bound

    def bind_last(self, func: Callable, last_arg: Any) -> Callable:
        """绑定最后一个参数"""
        def bound(*args, **kwargs):
            return func(*args, last_arg, **kwargs)
        return bound


_binding_tool: Optional[BindingTool] = None


def get_binding_tool() -> BindingTool:
    global _binding_tool
    if _binding_tool is None:
        _binding_tool = BindingTool()
    return _binding_tool