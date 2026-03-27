"""卡尔曼滤波器"""

import numpy as np
from typing import List, Optional, Tuple


class KalmanFilter:
    _instance: Optional["KalmanFilter"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def filter(self, measurements: List[float], process_variance: float = 0.1, measurement_variance: float = 0.1) -> List[float]:
        if len(measurements) == 0:
            return []
        estimates = []
        estimate = measurements[0]
        estimate_error = 1.0
        for measurement in measurements:
            prediction_error = estimate_error + process_variance
            kalman_gain = prediction_error / (prediction_error + measurement_variance)
            estimate = estimate + kalman_gain * (measurement - estimate)
            estimate_error = (1 - kalman_gain) * prediction_error
            estimates.append(estimate)
        return estimates


def get_kalman_filter() -> KalmanFilter:
    return KalmanFilter()
