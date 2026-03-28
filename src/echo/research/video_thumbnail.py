"""视频缩略图提取工具"""

from typing import List, Optional


class VideoThumbnailTool:
    _instance: Optional["VideoThumbnailTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def extract(self, frames: List[List[List[float]]], indices: List[int]) -> List[List[List[float]]]:
        if not frames:
            return []
        return [frames[i] for i in indices if 0 <= i < len(frames)]


def get_video_thumbnail_tool() -> VideoThumbnailTool:
    return VideoThumbnailTool()