"""图像灰度工具"""

from typing import List, Optional


class ImageGrayscaleTool:
    _instance: Optional["ImageGrayscaleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def grayscale(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        if not img:
            return img
        result = []
        for row in img:
            gray_row = []
            for pixel in row:
                gray = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2] if len(pixel) >= 3 else pixel[0]
                gray_row.append([gray, gray, gray])
            result.append(gray_row)
        return result


def get_image_grayscale_tool() -> ImageGrayscaleTool:
    return ImageGrayscaleTool()