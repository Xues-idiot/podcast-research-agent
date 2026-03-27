"""重叠添加工具"""

from typing import List


class OverlapAdd:
    _instance: Optional["OverlapAdd"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def overlap_add(self, frames: List[List[float]], hop_size: int) -> List[float]:
        if not frames:
            return []
        n = len(frames)
        frame_len = len(frames[0])
        output_len = n * hop_size + frame_len
        output = [0.0] * output_len
        for i, frame in enumerate(frames):
            offset = i * hop_size
            for j, val in enumerate(frame):
                if offset + j < output_len:
                    output[offset + j] += val
        return output


def get_overlap_add() -> OverlapAdd:
    return OverlapAdd()
