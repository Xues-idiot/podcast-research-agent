"""图像边缘检测工具"""

from typing import List, Optional


class ImageEdgeTool:
    _instance: Optional["ImageEdgeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sobel(self, img: List[List[List[float]]]) -> List[List[List[float]]]:
        if not img or len(img) < 3 or len(img[0]) < 3:
            return img
        h, w = len(img), len(img[0])
        gx = [[0.0] * w for _ in range(h)]
        gy = [[0.0] * w for _ in range(h)]
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                val = img[i][j][0] if img[i][j] else 0
                gx[i][j] = (img[i-1][j+1][0] if img[i-1][j+1] else 0) - (img[i-1][j-1][0] if img[i-1][j-1] else 0) + 2 * ((img[i][j+1][0] if img[i][j+1] else 0) - (img[i][j-1][0] if img[i][j-1] else 0)) + (img[i+1][j+1][0] if img[i+1][j+1] else 0) - (img[i+1][j-1][0] if img[i+1][j-1] else 0)
                gy[i][j] = (img[i+1][j-1][0] if img[i+1][j-1] else 0) - (img[i-1][j-1][0] if img[i-1][j-1] else 0) + 2 * ((img[i+1][j][0] if img[i+1][j] else 0) - (img[i-1][j][0] if img[i-1][j] else 0)) + (img[i+1][j+1][0] if img[i+1][j+1] else 0) - (img[i-1][j+1][0] if img[i-1][j+1] else 0)
        result = []
        for i in range(h):
            row = []
            for j in range(w):
                mag = min(1.0, (gx[i][j] ** 2 + gy[i][j] ** 2) ** 0.5 / 4)
                row.append([mag, mag, mag])
            result.append(row)
        return result


def get_image_edge_tool() -> ImageEdgeTool:
    return ImageEdgeTool()