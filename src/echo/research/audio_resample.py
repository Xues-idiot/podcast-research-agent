"""
Audio Resampling Module

Singleton class providing high-quality audio resampling
using polyphase filters for sample rate conversion.
"""

from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray


class AudioResample:
    """
    Singleton class for audio resampling operations.

    Provides high-quality sample rate conversion using
    polyphase filtering and optimal filter design.
    """
    _instance: Optional['AudioResample'] = None

    def __new__(cls) -> 'AudioResample':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def resample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
        quality: str = "medium",
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Resample audio signal to target sample rate.

        Args:
            signal: Input audio signal.
            original_rate: Original sample rate in Hz.
            target_rate: Target sample rate in Hz.
            quality: Resampling quality ("low", "medium", "high").

        Returns:
            Tuple of (resampled signal, new sample rate).
        """
        if original_rate == target_rate:
            return signal, original_rate

        from scipy import signal as sp_signal

        gcd = self._gcd(original_rate, target_rate)
        up = target_rate // gcd
        down = original_rate // gcd

        filter_params = self._get_filter_params(quality, up, down)
        resampled = sp_signal.resample_poly(signal, up, down, **filter_params)

        return resampled, target_rate

    def upsample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Upsample audio to higher sample rate.

        Args:
            signal: Input audio signal.
            original_rate: Original sample rate.
            target_rate: Target sample rate (must be higher).

        Returns:
            Tuple of (upsampled signal, new rate).
        """
        if target_rate <= original_rate:
            return signal, original_rate

        gcd = self._gcd(target_rate, original_rate)
        up = target_rate // gcd
        down = original_rate // gcd

        from scipy import signal as sp_signal
        resampled = sp_signal.resample_poly(signal, up, down, window='hann')

        return resampled, target_rate

    def downsample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Downsample audio to lower sample rate.

        Args:
            signal: Input audio signal.
            original_rate: Original sample rate.
            target_rate: Target sample rate (must be lower).

        Returns:
            Tuple of (downsampled signal, new rate).
        """
        if target_rate >= original_rate:
            return signal, original_rate

        gcd = self._gcd(original_rate, target_rate)
        up = target_rate // gcd
        down = original_rate // gcd

        from scipy import signal as sp_signal
        resampled = sp_signal.resample_poly(signal, up, down, window='hann')

        return resampled, target_rate

    def fractional_resample(
        self,
        signal: NDArray[np.float64],
        sample_rate: int,
        ratio: float,
        quality: str = "medium",
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Resample by a fractional ratio.

        Args:
            signal: Input audio signal.
            sample_rate: Sample rate in Hz.
            ratio: Resampling ratio (>1 upsample, <1 downsample).
            quality: Resampling quality.

        Returns:
            Tuple of (resampled signal, new sample rate).
        """
        from scipy import signal as sp_signal

        if abs(ratio - 1.0) < 1e-6:
            return signal, sample_rate

        gcd = self._gcd(int(sample_rate * ratio), sample_rate)
        up = int(sample_rate * ratio) // gcd
        down = sample_rate // gcd

        filter_params = self._get_filter_params(quality, up, down)
        resampled = sp_signal.resample_poly(signal, up, down, **filter_params)
        new_rate = int(sample_rate * ratio)

        return resampled, new_rate

    def zoh_resample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Zero-order hold resampling (simple repetition).

        Args:
            signal: Input audio signal.
            original_rate: Original sample rate.
            target_rate: Target sample rate.

        Returns:
            Tuple of (resampled signal, new rate).
        """
        if original_rate == target_rate:
            return signal, original_rate

        gcd = self._gcd(original_rate, target_rate)
        up = target_rate // gcd
        down = original_rate // gcd

        if up < down:
            ratio = down // up
            indices = np.arange(0, len(signal) * ratio, ratio)[:len(signal)]
            resampled = signal[indices]
        else:
            ratio = up // down
            resampled = np.repeat(signal, ratio)

        return resampled, target_rate

    def linear_resample(
        self,
        signal: NDArray[np.float64],
        original_rate: int,
        target_rate: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Linear interpolation resampling.

        Args:
            signal: Input audio signal.
            original_rate: Original sample rate.
            target_rate: Target sample rate.

        Returns:
            Tuple of (resampled signal, new rate).
        """
        if original_rate == target_rate:
            return signal, original_rate

        gcd = self._gcd(original_rate, target_rate)
        up = target_rate // gcd
        down = original_rate // gcd

        from scipy import signal as sp_signal
        resampled = sp_signal.resample_poly(signal, up, down, window='linear')

        return resampled, target_rate

    def _gcd(self, a: int, b: int) -> int:
        """Compute greatest common divisor."""
        while b:
            a, b = b, a % b
        return a

    def _get_filter_params(
        self, quality: str, up: int, down: int
    ) -> dict:
        """
        Get filter parameters based on quality level.

        Args:
            quality: Quality level.
            up: Upsampling factor.
            down: Downsampling factor.

        Returns:
            Dictionary with filter parameters.
        """
        max_ratio = max(up, down)

        if quality == "low":
            num_taps = 16
        elif quality == "medium":
            num_taps = 64
        elif quality == "high":
            num_taps = 256
        else:
            num_taps = 64

        cutoff = 0.5 / max_ratio
        return {
            'window': 'hann',
            'padlen': num_taps - 1,
        }
