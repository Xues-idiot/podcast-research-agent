"""序列工具"""

from typing import Optional, List, Any


class Sequencer:
    """序列工具"""

    def sequence(self, start: int, stop: int, step: int = 1) -> List[int]:
        """序列"""
        return list(range(start, stop, step))


_sequencer: Optional[Sequencer] = None


def get_sequencer() -> Sequencer:
    global _sequencer
    if _sequencer is None:
        _sequencer = Sequencer()
    return _sequencer