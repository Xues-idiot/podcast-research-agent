"""视频缩放工具"""

from typing import List, Optional, Tuple


class VideoScaleTool:
    _instance: Optional["VideoScaleTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def scale(self, frames: List[List[List[float]]], target_size: Tuple[int, int]) -> List[List[List[float]]]:
        if not frames or not frames[0]:
            return frames
        target_h, target_w = target_size
        src_h = len(frames[0])
        src_w = len(frames[0][0]) if src_h > 0 else 0
        if src_h == 0 or src_w == 0:
            return frames
        result = []
        for frame in frames:
            scaled = []
            for i in range(target_h):
                src_i = int(i * src_h / target_h)
                row = []
                for j in range(target_w):
                    src_j = int(j * src_w / target_w)
                    row.append(frame[src_i][src_j])
                scaled.append(row)
            result.append(scaled)
        return result


def get_video_scale_tool() -> VideoScaleTool:
    return VideoScaleTool()