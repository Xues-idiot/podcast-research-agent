"""信号积分器"""

from typing import List, Optional


class SignalIntegrator:
    _instance: Optional["SignalIntegrator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def integrate(self, signal: List[float], dt: float = 1.0) -> List[float]:
        result = [0.0]
        for i in range(1, len(signal)):
            result.append(result[-1] + 0.5 * (signal[i] + signal[i-1]) * dt)
        return result


def get_signal_integrator() -> SignalIntegrator:
    return SignalIntegrator()
