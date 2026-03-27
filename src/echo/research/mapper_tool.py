"""映射工具"""

from typing import Optional, Callable, Any


class MapperTool:
    """映射工具"""

    def map(self, items: list, func: Callable) -> list:
        """映射"""
        return [func(item) for item in items]

    def flat_map(self, items: list, func: Callable) -> list:
        """扁平映射"""
        result = []
        for item in items:
            mapped = func(item)
            if isinstance(mapped, list):
                result.extend(mapped)
            else:
                result.append(mapped)
        return result


_mapper: Optional[MapperTool] = None


def get_mapper_tool() -> MapperTool:
    global _mapper
    if _mapper is None:
        _mapper = MapperTool()
    return _mapper