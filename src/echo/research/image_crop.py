"""图像裁剪工具"""

from typing import List, Optional


class ImageCropTool:
    _instance: Optional["ImageCropTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def crop(self, img: List[List[List[float]]], x: int, y: int, w: int, h: int) -> List[List[List[float]]]:
        if not img:
            return img
        return [[img[y + i][x + j] for j in range(min(w, len(img[0]) - x))] for i in range(min(h, len(img) - y))]


def get_image_crop_tool() -> ImageCropTool:
    return ImageCropTool()