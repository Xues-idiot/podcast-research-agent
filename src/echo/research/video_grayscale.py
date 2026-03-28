"""视频灰度工具"""

from typing import List, Optional


class VideoGrayscaleTool:
    _instance: Optional["VideoGrayscaleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def grayscale(self, frames: List[List[List[float]]]) -> List[List[List[float]]]:
        if not frames or not frames[0]:
            return frames
        result = []
        for frame in frames:
            gray_frame = []
            for row in frame:
                gray_row = []
                for pixel in row:
                    gray = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2] if len(pixel) >= 3 else pixel[0]
                    gray_row.append([gray, gray, gray])
                gray_frame.append(gray_row)
            result.append(gray_frame)
        return result


def get_video_grayscale_tool() -> VideoGrayscaleTool:
    return VideoGrayscaleTool()