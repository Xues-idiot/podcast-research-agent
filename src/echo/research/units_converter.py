"""单位转换工具"""

from typing import Optional


class UnitsConverter:
    """单位转换工具"""

    def length(self, value: float, from_unit: str, to_unit: str) -> float:
        """长度转换"""
        to_meters = {
            "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
            "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
        }
        from_key = from_unit.lower()
        to_key = to_unit.lower()
        if from_key in to_meters and to_key in to_meters:
            return value * to_meters[from_key] / to_meters[to_key]
        return value

    def weight(self, value: float, from_unit: str, to_unit: str) -> float:
        """重量转换"""
        to_kg = {
            "mg": 0.000001, "g": 0.001, "kg": 1, "t": 1000,
            "oz": 0.0283495, "lb": 0.453592
        }
        from_key = from_unit.lower()
        to_key = to_unit.lower()
        if from_key in to_kg and to_key in to_kg:
            return value * to_kg[from_key] / to_kg[to_key]
        return value

    def temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """温度转换"""
        if from_unit.upper() == "C" and to_unit.upper() == "F":
            return value * 9/5 + 32
        elif from_unit.upper() == "F" and to_unit.upper() == "C":
            return (value - 32) * 5/9
        elif from_unit.upper() == "C" and to_unit.upper() == "K":
            return value + 273.15
        elif from_unit.upper() == "K" and to_unit.upper() == "C":
            return value - 273.15
        return value


_converter: Optional[UnitsConverter] = None


def get_units_converter() -> UnitsConverter:
    global _converter
    if _converter is None:
        _converter = UnitsConverter()
    return _converter