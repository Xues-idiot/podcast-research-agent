"""
Window Function Module for Signal Processing

Singleton class providing various window function implementations
for spectral analysis and signal processing applications.
"""

from typing import Optional, List
import numpy as np
from numpy.typing import NDArray


class WindowFn:
    """
    Singleton class for generating window functions.

    Provides common window functions used in digital signal processing
    for spectral analysis, filtering, and STFT applications.
    """
    _instance: Optional['WindowFn'] = None

    def __new__(cls) -> 'WindowFn':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def hann(self, length: int) -> NDArray[np.float64]:
        """
        Generate a Hann window.

        Args:
            length: Window length in samples.

        Returns:
            Hann window array of shape (length,).
        """
        if length < 1:
            return np.array([], dtype=np.float64)
        n = np.arange(length)
        return 0.5 * (1 - np.cos(2 * np.pi * n / (length - 1)))

    def hamming(self, length: int) -> NDArray[np.float64]:
        """
        Generate a Hamming window.

        Args:
            length: Window length in samples.

        Returns:
            Hamming window array of shape (length,).
        """
        if length < 1:
            return np.array([], dtype=np.float64)
        n = np.arange(length)
        return 0.54 - 0.46 * np.cos(2 * np.pi * n / (length - 1))

    def blackman(self, length: int) -> NDArray[np.float64]:
        """
        Generate a Blackman window.

        Args:
            length: Window length in samples.

        Returns:
            Blackman window array of shape (length,).
        """
        if length < 1:
            return np.array([], dtype=np.float64)
        n = np.arange(length)
        a0 = 0.42
        a1 = 0.5
        a2 = 0.08
        return (
            a0
            - a1 * np.cos(2 * np.pi * n / (length - 1))
            + a2 * np.cos(4 * np.pi * n / (length - 1))
        )

    def bartlett(self, length: int) -> NDArray[np.float64]:
        """
        Generate a Bartlett (triangular) window.

        Args:
            length: Window length in samples.

        Returns:
            Bartlett window array of shape (length,).
        """
        if length < 1:
            return np.array([], dtype=np.float64)
        n = np.arange(length)
        return np.where(
            n < (length - 1) / 2,
            2 * n / (length - 1),
            2 - 2 * n / (length - 1),
        )

    def kaiser(self, length: int, beta: float = 14.0) -> NDArray[np.float64]:
        """
        Generate a Kaiser window.

        Args:
            length: Window length in samples.
            beta: Kaiser window parameter (beta > 0).

        Returns:
            Kaiser window array of shape (length,).
        """
        if length < 1:
            return np.array([], dtype=np.float64)
        n = np.arange(length)
        alpha = (length - 1) / 2
        idx = np.abs(n - alpha) / alpha
        return np.i0(beta * np.sqrt(1 - idx**2)) / np.i0(beta)

    def apply(
        self, signal: NDArray[np.float64], window_type: str = "hann"
    ) -> NDArray[np.float64]:
        """
        Apply window function to a signal.

        Args:
            signal: Input signal array.
            window_type: Type of window ("hann", "hamming", "blackman", "bartlett", "kaiser").

        Returns:
            Windowed signal array.
        """
        length = len(signal)
        window_methods = {
            "hann": self.hann,
            "hamming": self.hamming,
            "blackman": self.blackman,
            "bartlett": self.bartlett,
            "kaiser": self.kaiser,
        }
        window_fn = window_methods.get(window_type.lower(), self.hann)
        window = window_fn(length)
        return signal * window
