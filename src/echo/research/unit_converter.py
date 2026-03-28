"""单位换算工具"""

from typing import Optional, Dict


class UnitConverterTool:
    _instance: Optional["UnitConverterTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        conversions: Dict[str, Dict[str, float]] = {
            "km_to_miles": 0.621371,
            "miles_to_km": 1.60934,
            "m_to_feet": 3.28084,
            "feet_to_m": 0.3048,
            "kg_to_lbs": 2.20462,
            "lbs_to_kg": 0.453592,
            "c_to_f": lambda c: c * 9/5 + 32,
            "f_to_c": lambda f: (f - 32) * 5/9,
            "m_to_inches": 39.3701,
            "inches_to_m": 0.0254,
        }

        key = f"{from_unit}_to_{to_unit}"
        if key in conversions:
            conv = conversions[key]
            return conv(value) if callable(conv) else value * conv
        return value


def get_unit_converter_tool() -> UnitConverterTool:
    return UnitConverterTool()