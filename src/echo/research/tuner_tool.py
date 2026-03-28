"""调音器工具"""

from typing import Optional


class TunerTool:
    _instance: Optional["TunerTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_note(self, freq: float) -> tuple[str, float]:
        note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        if freq <= 0:
            return "A", 440.0
        semitones = 12 * (freq ** (1 / 12)) / 440 ** (1 / 12)
        note_num = int(round(semitones)) + 69
        octave = note_num // 12 - 1
        note = note_names[note_num % 12]
        return note, octave


def get_tuner_tool() -> TunerTool:
    return TunerTool()
