"""视频对比度调整工具"""

from typing import List, Optional


class VideoContrastTool:
    _instance: Optional["VideoContrastTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def contrast(self, frames: List[List[List[float]]], factor: float = 1.0) -> List[List[List[float]]]:
        if not frames:
            return frames
        result = []
        for frame in frames:
            result.append([[min(1.0, max(0.0, 0.5 + factor * (pixel - 0.5))) for pixel in row] for row in frame])
        return result


def get_video_contrast_tool() -> VideoContrastTool:
    return VideoContrastTool()