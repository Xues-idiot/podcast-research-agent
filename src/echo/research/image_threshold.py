"""图像阈值工具"""

from typing import List, Optional


class ImageThresholdTool:
    _instance: Optional["ImageThresholdTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def threshold(self, img: List[List[List[float]]], value: float = 0.5) -> List[List[List[float]]]:
        if not img:
            return img
        return [[[1.0 if c > value else 0.0 for c in pixel] for pixel in row] for row in img]


def get_image_threshold_tool() -> ImageThresholdTool:
    return ImageThresholdTool()