"""步进音序器"""

from typing import List, Optional


class StepSequencer:
    _instance: Optional["StepSequencer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def sequence(self, steps: List[float], num_repeats: int) -> List[float]:
        result = []
        for _ in range(num_repeats):
            result.extend(steps)
        return result


def get_step_sequencer() -> StepSequencer:
    return StepSequencer()
