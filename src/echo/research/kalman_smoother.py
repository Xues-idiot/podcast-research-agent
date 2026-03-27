"""卡尔曼平滑器"""

from typing import List


class KalmanSmoother:
    _instance: Optional["KalmanSmoother"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def smooth(self, measurements: List[float], process_variance: float = 0.1, measurement_variance: float = 0.1) -> List[float]:
        if len(measurements) == 0:
            return []
        from echo.research.kalman_filter import get_kalman_filter
        return get_kalman_filter().filter(measurements, process_variance, measurement_variance)


def get_kalman_smoother() -> KalmanSmoother:
    return KalmanSmoother()
