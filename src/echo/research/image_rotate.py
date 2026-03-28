"""图像旋转工具"""

from typing import List, Optional


class ImageRotateTool:
    _instance: Optional["ImageRotateTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rotate_90(self, img: List[List[List[float]]], clockwise: bool = True) -> List[List[List[float]]]:
        if not img or not img[0]:
            return img
        if clockwise:
            return [list(row) for row in zip(*reversed(img))]
        return [list(row) for row in zip(*img)]

    def rotate_180(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        return [list(reversed(list(reversed(row)))) for row in reversed(img)]

    def rotate_270(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        return self.rotate_90(img, clockwise=False)


def get_image_rotate_tool() -> ImageRotateTool:
    return ImageRotateTool()