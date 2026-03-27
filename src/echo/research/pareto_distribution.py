"""帕累托分布"""

from typing import Optional


class ParetoDistribution:
    _instance: Optional["ParetoDistribution"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def mean(self, alpha: float, xm: float) -> Optional[float]:
        if alpha <= 1:
            return None
        return alpha * xm / (alpha - 1)

    def variance(self, alpha: float, xm: float) -> Optional[float]:
        if alpha <= 2:
            return None
        return (xm ** 2 * alpha) / ((alpha - 1) ** 2 * (alpha - 2))


def get_pareto_distribution() -> ParetoDistribution:
    return ParetoDistribution()
