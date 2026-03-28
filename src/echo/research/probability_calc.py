"""概率计算工具"""

from typing import Optional
import math


class ProbabilityCalcTool:
    _instance: Optional["ProbabilityCalcTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def factorial(self, n: int) -> int:
        """阶乘"""
        return math.factorial(n)

    def permutation(self, n: int, r: int) -> int:
        """排列数"""
        return math.perm(n, r)

    def combination(self, n: int, r: int) -> int:
        """组合数"""
        return math.comb(n, r)

    def binomial_prob(self, n: int, k: int, p: float) -> float:
        """二项概率"""
        return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

    def normal_cdf(self, x: float, mean: float = 0, std: float = 1) -> float:
        """正态分布CDF"""
        return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

    def poisson_prob(self, k: int, lambda_: float) -> float:
        """泊松概率"""
        return (lambda_ ** k) * math.exp(-lambda_) / math.factorial(k)

    def expected_value(self, values: list, probabilities: list) -> float:
        """期望值"""
        return sum(v * p for v, p in zip(values, probabilities))


_prob_instance: Optional[ProbabilityCalcTool] = None


def get_probability_calc_tool() -> ProbabilityCalcTool:
    global _prob_instance
    if _prob_instance is None:
        _prob_instance = ProbabilityCalcTool()
    return _prob_instance