"""欧拉角四元数转换工具"""

import math
from typing import List, Optional


class EulerQuaternionTool:
    _instance: Optional["EulerQuaternionTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def euler_to_quaternion(self, euler: List[float]) -> List[float]:
        if len(euler) != 3:
            return [1.0, 0.0, 0.0, 0.0]
        pitch, yaw, roll = euler
        cy = math.cos(yaw * 0.5)
        sy = math.sin(yaw * 0.5)
        cp = math.cos(pitch * 0.5)
        sp = math.sin(pitch * 0.5)
        cr = math.cos(roll * 0.5)
        sr = math.sin(roll * 0.5)
        return [
            cr * cp * cy + sr * sp * sy,
            sr * cp * cy - cr * sp * sy,
            cr * sp * cy + sr * cp * sy,
            cr * cp * sy - sr * sp * cy
        ]

    def quaternion_to_euler(self, q: List[float]) -> List[float]:
        if len(q) != 4:
            return [0.0, 0.0, 0.0]
        w, x, y, z = q
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = math.atan2(sinr_cosp, cosr_cosp)
        sinp = 2 * (w * y - z * x)
        if abs(sinp) >= 1:
            pitch = math.copysign(math.pi * 0.5, sinp)
        else:
            pitch = math.asin(sinp)
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        return [pitch, yaw, roll]


def get_euler_quaternion_tool() -> EulerQuaternionTool:
    return EulerQuaternionTool()