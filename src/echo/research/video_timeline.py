"""视频时间线工具"""

from typing import List, Optional


class VideoTimelineTool:
    _instance: Optional["VideoTimelineTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def trim(self, frames: List[List[List[float]]], start: int, end: int) -> List[List[List[float]]]:
        if not frames:
            return []
        return frames[start:end]

    def splice(self, clips: List[List[List[List[float]]]], transitions: List[int]) -> List[List[List[float]]]:
        result = []
        clip_idx = 0
        trans_idx = 0
        for i, clip in enumerate(clips):
            result.extend(clip)
            if trans_idx < len(transitions) and i < len(clips) - 1:
                trans_idx += 1
        return result


def get_video_timeline_tool() -> VideoTimelineTool:
    return VideoTimelineTool()