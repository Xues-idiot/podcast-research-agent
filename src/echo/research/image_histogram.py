"""图像直方图工具"""

from typing import List, Optional


class ImageHistogramTool:
    _instance: Optional["ImageHistogramTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def histogram(self, img: List[List[List[float]]], bins: int = 256) -> List[int]:
        if not img:
            return []
        counts = [0] * bins
        for row in img:
            for pixel in row:
                val = pixel[0] if len(pixel) > 0 else 0
                idx = min(bins - 1, int(val * bins))
                counts[idx] += 1
        return counts


def get_image_histogram_tool() -> ImageHistogramTool:
    return ImageHistogramTool()