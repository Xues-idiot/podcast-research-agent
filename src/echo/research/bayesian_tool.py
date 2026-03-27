"""贝叶斯推断工具"""

from typing import Optional


class BayesianTool:
    _instance: Optional["BayesianTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def posterior(self, prior: float, likelihood: float, marginal: float) -> Optional[float]:
        if marginal == 0:
            return None
        return (likelihood * prior) / marginal

    def bayes_factor(self, p1: float, p2: float) -> Optional[float]:
        if p2 == 0 or (1 - p2) == 0:
            return None
        if p1 == 0 or (1 - p1) == 0:
            return None
        return (p1 / (1 - p1)) / (p2 / (1 - p2))


def get_bayesian_tool() -> BayesianTool:
    return BayesianTool()
