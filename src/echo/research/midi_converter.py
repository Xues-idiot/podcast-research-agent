"""MIDI转频率工具"""

from typing import Optional


class MidiConverter:
    _instance: Optional["MidiConverter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def midi_to_freq(self, midi_note: int) -> float:
        return 440.0 * (2 ** ((midi_note - 69) / 12))

    def freq_to_midi(self, freq: float) -> int:
        return int(round(69 + 12 * (freq / 440.0) ** (12)))


def get_midi_converter() -> MidiConverter:
    return MidiConverter()
