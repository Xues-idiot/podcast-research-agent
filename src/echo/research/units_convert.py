"""单位转换工具"""

from typing import Optional


class UnitsConvertTool:
    _instance: Optional["UnitsConvertTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def length_mm_to_cm(self, mm: float) -> float:
        return mm / 10

    def length_cm_to_m(self, cm: float) -> float:
        return cm / 100

    def length_m_to_km(self, m: float) -> float:
        return m / 1000

    def length_inch_to_cm(self, inch: float) -> float:
        return inch * 2.54

    def length_foot_to_m(self, foot: float) -> float:
        return foot * 0.3048

    def length_mile_to_km(self, mile: float) -> float:
        return mile * 1.60934

    def weight_g_to_kg(self, g: float) -> float:
        return g / 1000

    def weight_kg_to_t(self, kg: float) -> float:
        return kg / 1000

    def weight_lb_to_kg(self, lb: float) -> float:
        return lb * 0.453592

    def weight_oz_to_g(self, oz: float) -> float:
        return oz * 28.3495

    def temperature_c_to_f(self, c: float) -> float:
        return c * 9/5 + 32

    def temperature_f_to_c(self, f: float) -> float:
        return (f - 32) * 5/9

    def temperature_c_to_k(self, c: float) -> float:
        return c + 273.15

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """通用转换"""
        conversions = {
            ("mm", "cm"): self.length_mm_to_cm,
            ("cm", "m"): self.length_cm_to_m,
            ("m", "km"): self.length_m_to_km,
            ("in", "cm"): self.length_inch_to_cm,
            ("ft", "m"): self.length_foot_to_m,
            ("mi", "km"): self.length_mile_to_km,
            ("g", "kg"): self.weight_g_to_kg,
            ("kg", "t"): self.weight_kg_to_t,
            ("lb", "kg"): self.weight_lb_to_kg,
            ("oz", "g"): self.weight_oz_to_g,
            ("c", "f"): self.temperature_c_to_f,
            ("f", "c"): self.temperature_f_to_c,
            ("c", "k"): self.temperature_c_to_k,
        }
        key = (from_unit.lower(), to_unit.lower())
        if key in conversions:
            return conversions[key](value)
        return value


_units_instance: Optional[UnitsConvertTool] = None


def get_units_convert_tool() -> UnitsConvertTool:
    global _units_instance
    if _units_instance is None:
        _units_instance = UnitsConvertTool()
    return _units_instance