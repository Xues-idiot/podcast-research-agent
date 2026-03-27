"""数字格式化工具"""

from typing import Optional


class NumberFormatter:
    """数字格式化工具"""

    def format_currency(self, amount: float, currency: str = "CNY") -> str:
        """格式化货币"""
        symbols = {"CNY": "¥", "USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}
        symbol = symbols.get(currency, currency)
        return f"{symbol}{amount:,.2f}"

    def format_percentage(self, value: float, decimals: int = 2) -> str:
        """格式化百分比"""
        return f"{value * 100:.{decimals}f}%"

    def format_bytes(self, bytes_count: int) -> str:
        """格式化字节"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_count < 1024:
                return f"{bytes_count:.2f} {unit}"
            bytes_count /= 1024
        return f"{bytes_count:.2f} PB"

    def format_with_commas(self, number: int) -> str:
        """添加千位分隔符"""
        return f"{number:,}"


_formatter: Optional[NumberFormatter] = None


def get_number_formatter() -> NumberFormatter:
    global _formatter
    if _formatter is None:
        _formatter = NumberFormatter()
    return _formatter