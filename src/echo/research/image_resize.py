"""图像缩放工具"""

from typing import List, Optional, Tuple


class ImageResizeTool:
    _instance: Optional["ImageResizeTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def resize(self, img: List[List[List[float]]], target_h: int, target_w: int) -> List[List[List[float]]]:
        if not img or not img[0]:
            return img
        src_h = len(img)
        src_w = len(img[0])
        result = []
        for i in range(target_h):
            src_i = int(i * src_h / target_h)
            row = []
            for j in range(target_w):
                src_j = int(j * src_w / target_w)
                row.append(img[src_i][src_j])
            result.append(row)
        return result


def get_image_resize_tool() -> ImageResizeTool:
    return ImageResizeTool()