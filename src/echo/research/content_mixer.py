"""多内容混合器"""

from typing import Optional


class ContentMixer:
    """混合多个内容源"""

    def mix_sequential(self, contents: list[str], separator: str = "\n\n---\n\n") -> str:
        """顺序混合"""
        return separator.join(c for c in contents if c)

    def mix_interleave(self, contents: list[str], segment_size: int = 3) -> str:
        """交错混合"""
        if not contents:
            return ""

        lines_list = [c.split("\n") for c in contents]
        result = []
        max_segments = max(len(lines) // segment_size + 1 for lines in lines_list)

        for seg_idx in range(max_segments):
            for lines in lines_list:
                start = seg_idx * segment_size
                end = start + segment_size
                result.extend(lines[start:end])

        return "\n".join(result)

    def mix_summary(self, contents: list[str], weights: Optional[list[float]] = None) -> str:
        """加权混合"""
        if not contents:
            return ""

        if weights is None:
            weights = [1.0] * len(contents)

        total_weight = sum(weights)
        normalized = [w / total_weight for w in weights]

        result_parts = []
        for content, weight in zip(contents, normalized):
            if not content:
                continue
            lines = content.split("\n")
            keep_count = max(1, int(len(lines) * weight))
            result_parts.extend(lines[:keep_count])

        return "\n".join(result_parts)


_mixer: Optional[ContentMixer] = None


def get_content_mixer() -> ContentMixer:
    global _mixer
    if _mixer is None:
        _mixer = ContentMixer()
    return _mixer