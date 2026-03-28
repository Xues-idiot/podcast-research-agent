"""图像反色工具"""

from typing import List, Optional


class ImageInvertTool:
    _instance: Optional["ImageInvertTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def invert(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        if not img:
            return img
        return [[[1.0 - c for c in pixel] for pixel in row] for row in img]


def get_image_invert_tool() -> ImageInvertTool:
    return ImageInvertTool()