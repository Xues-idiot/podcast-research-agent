"""图像翻转工具"""

from typing import List, Optional


class ImageFlipTool:
    _instance: Optional["ImageFlipTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def flip_horizontal(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        return [list(reversed(row)) for row in img]

    def flip_vertical(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        return list(reversed(img))


def get_image_flip_tool() -> ImageFlipTool:
    return ImageFlipTool()