"""图像任意角度旋转工具"""

import math
from typing import List, Optional


class ImageRotateAnyTool:
    _instance: Optional["ImageRotateAnyTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def rotate(self, img: List[List[List[float]]], angle: float) -> List[List[List[float]]]:
        if not img:
            return img
        h, w = len(img), len(img[0])
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        new_w = int(abs(w * cos_a) + abs(h * sin_a))
        new_h = int(abs(h * cos_a) + abs(w * sin_a))
        result = [[0.5 for _ in range(new_w)] for _ in range(new_h)]
        cx, cy = w / 2, h / 2
        nx, ny = new_w / 2, new_h / 2
        for i in range(new_h):
            for j in range(new_w):
                dx = j - nx
                dy = i - ny
                src_x = dx * cos_a - dy * sin_a + cx
                src_y = dx * sin_a + dy * cos_a + cy
                if 0 <= src_x < w and 0 <= src_y < h:
                    ix, iy = int(src_x), int(src_y)
                    result[i][j] = img[iy][ix]
        return result


def get_image_rotate_any_tool() -> ImageRotateAnyTool:
    return ImageRotateAnyTool()