"""
Signal Resampling Module

Singleton class providing signal resampling functionality
for audio and digital signal processing.
"""

from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray


class SignalResample:
    """
    Singleton class for signal resampling operations.

    Provides downsampling and upsampling with appropriate
    anti-aliasing filtering for audio processing applications.
    """
    _instance: Optional['SignalResample'] = None

    def __new__(cls) -> 'SignalResample':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def downsample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Downsample a signal to a lower sample rate.

        Args:
            signal: Input signal array.
            original_rate: Original sample rate in Hz.
            target_rate: Target sample rate in Hz.

        Returns:
            Tuple of (downsampled signal, new sample rate).
        """
        if target_rate >= original_rate:
            return signal, original_rate

        if original_rate % target_rate != 0:
            from scipy import signal as sp_signal
            gcd = self._gcd(original_rate, target_rate)
            up = target_rate // gcd
            down = original_rate // gcd
            resampled = sp_signal.resample_poly(signal, up, down)
            return resampled, target_rate

        ratio = original_rate // target_rate
        filtered = self._anti_alias_filter(signal, ratio)
        return filtered[::ratio], target_rate

    def upsample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Upsample a signal to a higher sample rate.

        Args:
            signal: Input signal array.
            original_rate: Original sample rate in Hz.
            target_rate: Target sample rate in Hz.

        Returns:
            Tuple of (upsampled signal, new sample rate).
        """
        if target_rate <= original_rate:
            return signal, original_rate

        if target_rate % original_rate != 0:
            from scipy import signal as sp_signal
            gcd = self._gcd(target_rate, original_rate)
            up = target_rate // gcd
            down = original_rate // gcd
            resampled = sp_signal.resample_poly(signal, up, down)
            return resampled, target_rate

        ratio = target_rate // original_rate
        upsampled = np.zeros(len(signal) * ratio, dtype=signal.dtype)
        upsampled[::ratio] = signal
        filtered = self._interpolation_filter(upsampled, ratio)
        return filtered, target_rate

    def resample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Resample signal to target sample rate.

        Args:
            signal: Input signal array.
            original_rate: Original sample rate in Hz.
            target_rate: Target sample rate in Hz.

        Returns:
            Tuple of (resampled signal, new sample rate).
        """
        if original_rate == target_rate:
            return signal, original_rate

        if target_rate < original_rate:
            return self.downsample(signal, original_rate, target_rate)
        return self.upsample(signal, original_rate, target_rate)

    def _gcd(self, a: int, b: int) -> int:
        """Compute greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    def _anti_alias_filter(
        self, signal: NDArray[np.float64], ratio: int
    ) -> NDArray[np.float64]:
        """Apply anti-aliasing filter before downsampling."""
        from scipy import signal as sp_signal
        nyquist = 0.5 / ratio
        cutoff = min(0.95 * nyquist, 0.5)
        b, a = sp_signal.butter(8, cutoff, btype='low')
        return sp_signal.filtfilt(b, a, signal)

    def _interpolation_filter(
        self, signal: NDArray[np.float64], ratio: int
    ) -> NDArray[np.float64]:
        """Apply interpolation filter after upsampling."""
        from scipy import signal as sp_signal
        cutoff = 0.5 / ratio
        b, a = sp_signal.butter(8, cutoff, btype='low')
        return sp_signal.filtfilt(b, a, signal)
