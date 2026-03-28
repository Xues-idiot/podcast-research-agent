"""图像复古色调工具"""

from typing import List, Optional


class ImageSepiaTool:
    _instance: Optional["ImageSepiaTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sepia(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        if not img:
            return img
        result = []
        for row in img:
            sepia_row = []
            for pixel in row:
                r = pixel[0] if len(pixel) > 0 else 0
                g = pixel[1] if len(pixel) > 1 else 0
                b = pixel[2] if len(pixel) > 2 else 0
                new_r = min(1.0, 0.393 * r + 0.769 * g + 0.189 * b)
                new_g = min(1.0, 0.349 * r + 0.686 * g + 0.168 * b)
                new_b = min(1.0, 0.272 * r + 0.534 * g + 0.131 * b)
                sepia_row.append([new_r, new_g, new_b])
            result.append(sepia_row)
        return result


def get_image_sepia_tool() -> ImageSepiaTool:
    return ImageSepiaTool()