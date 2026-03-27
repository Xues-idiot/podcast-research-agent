"""Transform tool module - transforms data using various operations"""

from typing import Any, Callable, Dict, List, Optional, TypeVar

T = TypeVar('T')
R = TypeVar('R')


class TransformTool:
    _instance: Optional["TransformTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def transform(self, data: Any, transformer: Callable[[Any], Any]) -> Any:
        """Transform data using a custom transformer function"""
        return transformer(data)

    def map_values(self, items: List[T], mapper: Callable[[T], R]) -> List[R]:
        """Map each item to a new value"""
        return [mapper(item) for item in items]

    def flat_map(self, items: List[List[T]]) -> List[T]:
        """Flatten a list of lists"""
        return [item for sublist in items for item in sublist]

    def transform_dict(self, data: Dict[str, Any], transformer: Callable[[str, Any], tuple]) -> Dict[str, Any]:
        """Transform dictionary keys and values"""
        return dict(transformer(k, v) for k, v in data.items())

    def pipe_transform(self, data: Any, transforms: List[Callable[[Any], Any]]) -> Any:
        """Apply a series of transforms to data"""
        result = data
        for transform in transforms:
            result = transform(result)
        return result


def get_transform_tool() -> TransformTool:
    return TransformTool()
