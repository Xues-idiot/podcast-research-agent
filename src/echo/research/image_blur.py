"""图像模糊工具"""

from typing import List, Optional


class ImageBlurTool:
    _instance: Optional["ImageBlurTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def blur(self, img: List[List[List[float]]], radius: int = 3) -> List[List[List[float]]]:
        if not img or not img[0] or radius <= 0:
            return img
        h, w = len(img), len(img[0])
        result = [[0.0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                count = 0
                total = 0.0
                for di in range(-radius, radius + 1):
                    for dj in range(-radius, radius + 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < h and 0 <= nj < w:
                            total += img[ni][nj][0]
                            count += 1
                result[i][j] = [total / count if count > 0 else img[i][j][0]] * 3
        return result


def get_image_blur_tool() -> ImageBlurTool:
    return ImageBlurTool()