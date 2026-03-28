"""
Signal Interpolation Module

Singleton class providing interpolation methods for
digital signal processing and audio applications.
"""

from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray


class InterpSignal:
    """
    Singleton class for signal interpolation operations.

    Provides various interpolation methods for resampling,
    upsampling, and curve fitting in signal processing.
    """
    _instance: Optional['InterpSignal'] = None

    def __new__(cls) -> 'InterpSignal':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def linear(
        self, x: NDArray[np.float64], y: NDArray[np.float64], x_new: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        """
        Linear interpolation.

        Args:
            x: Original x coordinates.
            y: Original y values.
            x_new: New x coordinates for interpolation.

        Returns:
            Interpolated y values at x_new positions.
        """
        return np.interp(x_new, x, y)

    def cubic(
        self,
        x: NDArray[np.float64],
        y: NDArray[np.float64],
        x_new: NDArray[np.float64],
    ) -> NDArray[np.float64]:
        """
        Cubic spline interpolation.

        Args:
            x: Original x coordinates.
            y: Original y values.
            x_new: New x coordinates for interpolation.

        Returns:
            Interpolated y values at x_new positions.
        """
        from scipy import interpolate
        cubic_interp = interpolate.interp1d(x, y, kind='cubic', fill_value='extrapolate')
        return cubic_interp(x_new)

    def nearest(
        self, x: NDArray[np.float64], y: NDArray[np.float64], x_new: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        """
        Nearest-neighbor interpolation.

        Args:
            x: Original x coordinates.
            y: Original y values.
            x_new: New x coordinates for interpolation.

        Returns:
            Interpolated y values at x_new positions.
        """
        nearest_interp = interpolate.interp1d(x, y, kind='nearest', fill_value='extrapolate')
        return nearest_interp(x_new)

    def spline(
        self,
        x: NDArray[np.float64],
        y: NDArray[np.float64],
        x_new: NDArray[np.float64],
        smoothing: float = 0.0,
    ) -> Tuple[NDArray[np.float64], Optional[NDArray[np.float64]]]:
        """
        Smoothing spline interpolation.

        Args:
            x: Original x coordinates.
            y: Original y values.
            x_new: New x coordinates for interpolation.
            smoothing: Smoothing factor (0 for exact interpolation).

        Returns:
            Tuple of (interpolated y values, optionally derivatives).
        """
        from scipy import interpolate
        tck = interpolate.splrep(x, y, s=smoothing)
        y_new = interpolate.splev(x_new, tck)
        return y_new, None

    def lanczos(
        self, x: NDArray[np.float64], y: NDArray[np.float64], x_new: NDArray[np.float64], a: int = 3
    ) -> NDArray[np.float64]:
        """
        Lanczos (sinc) interpolation.

        Args:
            x: Original x coordinates.
            y: Original y values.
            x_new: New x coordinates for interpolation.
            a: Lanczos radius parameter.

        Returns:
            Interpolated y values at x_new positions.
        """
        y_new = np.zeros_like(x_new, dtype=np.float64)
        for i, xi in enumerate(x_new):
            idx = np.searchsorted(x, xi)
            weight_sum = 0.0
            for j in range(max(0, idx - a), min(len(x), idx + a)):
                t = abs(xi - x[j])
                if t < 1e-10:
                    y_new[i] = y[j]
                    break
                weight = a * np.sin(np.pi * t) * np.sin(np.pi * t / a) / (np.pi**2 * t**2)
                y_new[i] += y[j] * weight
                weight_sum += weight
            else:
                y_new[i] /= weight_sum if weight_sum > 0 else 1.0
        return y_new

    def resample_with_interp(
        self,
        signal: NDArray[np.float64],
        original_length: int,
        target_length: int,
        method: str = "linear",
    ) -> NDArray[np.float64]:
        """
        Resample signal to target length using specified interpolation.

        Args:
            signal: Input signal array.
            original_length: Original signal length.
            target_length: Target signal length.
            method: Interpolation method ("linear", "cubic", "nearest", "lanczos").

        Returns:
            Resampled signal array of length target_length.
        """
        x = np.linspace(0, 1, original_length)
        x_new = np.linspace(0, 1, target_length)

        methods = {
            "linear": self.linear,
            "cubic": self.cubic,
            "nearest": self.nearest,
            "lanczos": self.lanczos,
        }

        interp_fn = methods.get(method.lower(), self.linear)
        return interp_fn(x, signal, x_new)
