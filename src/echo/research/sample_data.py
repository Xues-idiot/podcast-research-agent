"""样本数据生成工具"""

from typing import Optional, List
import random
import string


class SampleDataTool:
    _instance: Optional["SampleDataTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def random_ints(self, count: int, min_val: int = 0, max_val: int = 100) -> List[int]:
        """生成随机整数"""
        return [random.randint(min_val, max_val) for _ in range(count)]

    def random_floats(self, count: int, min_val: float = 0, max_val: float = 1) -> List[float]:
        """生成随机浮点数"""
        return [random.uniform(min_val, max_val) for _ in range(count)]

    def random_strings(self, count: int, length: int = 10) -> List[str]:
        """生成随机字符串"""
        return ["".join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(count)]

    def random_dates(self, count: int, start_year: int = 2020, end_year: int = 2024) -> List[str]:
        """生成随机日期"""
        from datetime import date, timedelta
        start = date(start_year, 1, 1)
        end = date(end_year, 12, 31)
        delta = (end - start).days
        return [(start + timedelta(days=random.randint(0, delta))).isoformat() for _ in range(count)]

    def random_emails(self, count: int) -> List[str]:
        """生成随机邮箱"""
        domains = ["gmail.com", "qq.com", "163.com", "outlook.com"]
        return [f"{self.random_strings(1, 8)[0]}@{random.choice(domains)}" for _ in range(count)]

    def random_ips(self, count: int) -> List[str]:
        """生成随机IP地址"""
        return [f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}" for _ in range(count)]


_sample_instance: Optional[SampleDataTool] = None


def get_sample_data_tool() -> SampleDataTool:
    global _sample_instance
    if _sample_instance is None:
        _sample_instance = SampleDataTool()
    return _sample_instance