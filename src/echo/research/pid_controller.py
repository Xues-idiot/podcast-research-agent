"""PID控制器"""

from typing import List, Optional


class PidController:
    _instance: Optional["PidController"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def compute(self, setpoint: float, current: float, kp: float = 1.0, ki: float = 0.0, kd: float = 0.0, integral: float = 0.0, prev_error: float = 0.0) -> tuple:
        error = setpoint - current
        integral = integral + error
        derivative = error - prev_error
        output = kp * error + ki * integral + kd * derivative
        return (output, integral, error)


def get_pid_controller() -> PidController:
    return PidController()
