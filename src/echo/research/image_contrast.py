"""图像对比度调整工具"""

from typing import List, Optional


class ImageContrastTool:
    _instance: Optional["ImageContrastTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def contrast(self, img: List[List[List[float]]], factor: float = 1.0) -> List[List[List[float]]]:
        if not img:
            return img
        return [[[min(1.0, max(0.0, 0.5 + factor * (c - 0.5))) for c in pixel] for pixel in row] for row in img]


def get_image_contrast_tool() -> ImageContrastTool:
    return ImageContrastTool()