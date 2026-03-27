"""函数组合工具"""

from typing import Optional, Callable


class Compositor:
    """函数组合工具"""

    def compose(self, *funcs) -> Callable:
        """组合函数"""
        def composed(x):
            result = x
            for func in funcs:
                result = func(result)
            return result
        return composed

    def pipe(self, *funcs) -> Callable:
        """管道函数"""
        return self.compose(*reversed(funcs))


_compositor: Optional[Compositor] = None


def get_compositor() -> Compositor:
    global _compositor
    if _compositor is None:
        _compositor = Compositor()
    return _compositor