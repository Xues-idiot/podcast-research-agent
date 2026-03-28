"""年龄计算工具"""

from datetime import datetime, date
from typing import Optional


class AgeCalculatorTool:
    _instance: Optional["AgeCalculatorTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate(self, birth_date: str) -> int:
        try:
            birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
            today = date.today()
            age = today.year - birth.year
            if (today.month, today.day) < (birth.month, birth.day):
                age -= 1
            return age
        except:
            return 0

    def days_until_birthday(self, birth_date: str) -> int:
        try:
            birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
            today = date.today()
            this_birthday = birth.replace(year=today.year)
            if this_birthday < today:
                this_birthday = this_birthday.replace(year=today.year + 1)
            return (this_birthday - today).days
        except:
            return 0


def get_age_calculator_tool() -> AgeCalculatorTool:
    return AgeCalculatorTool()