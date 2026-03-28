"""数字格式化工具"""

from typing import Optional


class NumberFmtTool:
    _instance: Optional["NumberFmtTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def format_currency(self, value: float, currency: str = "CNY", locale: str = "zh_CN") -> str:
        """格式化货币"""
        if currency == "CNY":
            return f"¥{value:,.2f}"
        elif currency == "USD":
            return f"${value:,.2f}"
        elif currency == "EUR":
            return f"€{value:,.2f}"
        elif currency == "GBP":
            return f"£{value:,.2f}"
        return f"{value:,.2f} {currency}"

    def format_percent(self, value: float, decimals: int = 2) -> str:
        """格式化百分比"""
        return f"{value * 100:.{decimals}f}%"

    def format_scientific(self, value: float) -> str:
        """科学计数法"""
        return f"{value:.2e}"

    def format_compact(self, value: float) -> str:
        """简化数字(1K, 1M等)"""
        if abs(value) >= 1_000_000:
            return f"{value / 1_000_000:.1f}M"
        elif abs(value) >= 1_000:
            return f"{value / 1_000:.1f}K"
        return str(value)

    def format_with_commas(self, value: float, decimals: int = 0) -> str:
        """千分位格式化"""
        if decimals == 0:
            return f"{int(value):,}"
        return f"{value:,.{decimals}f}"

    def ordinal(self, n: int) -> str:
        """序数词(1st, 2nd, 3rd等)"""
        if 10 <= n % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
        return f"{n}{suffix}"


_num_fmt_instance: Optional[NumberFmtTool] = None


def get_number_fmt_tool() -> NumberFmtTool:
    global _num_fmt_instance
    if _num_fmt_instance is None:
        _num_fmt_instance = NumberFmtTool()
    return _num_fmt_instance