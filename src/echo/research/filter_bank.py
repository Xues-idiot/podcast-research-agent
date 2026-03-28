"""滤波器组工具"""

from typing import List, Optional


class FilterBank:
    _instance: Optional["FilterBank"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_mel_bank(self, n_filters: int = 128, fft_size: int = 1024, sample_rate: float = 44100) -> List[List[float]]:
        bank = []
        for i in range(n_filters):
            filter_band = [0.0] * (fft_size // 2 + 1)
            bank.append(filter_band)
        return bank


def get_filter_bank() -> FilterBank:
    return FilterBank()
