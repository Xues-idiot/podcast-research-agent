"""图像亮度调整工具"""

from typing import List, Optional


class ImageBrightnessTool:
    _instance: Optional["ImageBrightnessTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def brightness(self, img: List[List[List[float]]], factor: float = 1.0) -> List[List[List[float]]]:
        if not img:
            return img
        return [[[min(1.0, max(0.0, c * factor)) for c in pixel] for pixel in row] for row in img]


def get_image_brightness_tool() -> ImageBrightnessTool:
    return ImageBrightnessTool()