"""
Overlap-Add Processor Module

Singleton class providing overlap-add signal processing
for windowed analysis and synthesis operations.
"""

from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray


class OlaProcessor:
    """
    Singleton class for overlap-add processing.

    Implements the overlap-add method for combining
    windowed signal frames in STFT processing.
    """
    _instance: Optional['OlaProcessor'] = None

    def __new__(cls) -> 'OlaProcessor':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def segment(
        self,
        signal: NDArray[np.float64],
        window_size: int,
        hop_size: int,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Segment signal into overlapping frames.

        Args:
            signal: Input signal.
            window_size: Size of each segment in samples.
            hop_size: Hop size between consecutive frames.

        Returns:
            Tuple of (2D array of shape (num_frames, window_size), num_frames).
        """
        num_frames = (len(signal) - window_size) // hop_size + 1
        segments = np.zeros((num_frames, window_size), dtype=signal.dtype)

        for i in range(num_frames):
            start = i * hop_size
            segments[i] = signal[start : start + window_size]

        return segments, num_frames

    def add(
        self,
        segments: NDArray[np.float64],
        hop_size: int,
        output_length: Optional[int] = None,
    ) -> NDArray[np.float64]:
        """
        Combine overlapping segments using overlap-add.

        Args:
            segments: 2D array of shape (num_frames, window_size).
            hop_size: Hop size used during segmentation.
            output_length: Expected output length (optional).

        Returns:
            Combined signal array.
        """
        num_frames, window_size = segments.shape

        if output_length is None:
            output_length = (num_frames - 1) * hop_size + window_size

        output = np.zeros(output_length, dtype=segments.dtype)
        window_sum = np.zeros(output_length, dtype=np.float64)

        for i in range(num_frames):
            start = i * hop_size
            end = start + window_size
            if end <= output_length:
                output[start:end] += segments[i]
                window_sum[start:end] += 1.0

        if np.any(window_sum > 0):
            output = output / window_sum

        return output

    def apply_window(
        self,
        signal: NDArray[np.float64],
        window_size: int,
        hop_size: int,
        window_type: str = "hann",
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Apply window function to signal frames.

        Args:
            signal: Input signal.
            window_size: Window size in samples.
            hop_size: Hop size between frames.
            window_type: Type of window function ("hann", "hamming", "blackman").

        Returns:
            Tuple of (windowed segments, num_frames).
        """
        window = self._get_window(window_type, window_size)
        segments, num_frames = self.segment(signal, window_size, hop_size)
        windowed_segments = segments * window
        return windowed_segments, num_frames

    def overlap_add_synthesis(
        self,
        windowed_segments: NDArray[np.float64],
        hop_size: int,
        output_length: Optional[int] = None,
        window_type: str = "hann",
    ) -> NDArray[np.float64]:
        """
        Perform overlap-add synthesis with window normalization.

        Args:
            windowed_segments: 2D array of windowed frames.
            hop_size: Hop size between frames.
            output_length: Expected output length.
            window_type: Window type used (for normalization).

        Returns:
            Reconstructed signal.
        """
        window_size = windowed_segments.shape[1]
        window = self._get_window(window_type, window_size)
        windowed_segments = windowed_segments / (window + 1e-10)
        return self.add(windowed_segments, hop_size, output_length)

    def stft(
        self,
        signal: NDArray[np.float64],
        window_size: int = 2048,
        hop_size: int = 512,
        window_type: str = "hann",
    ) -> Tuple[NDArray[np.complex128], int]:
        """
        Compute Short-Time Fourier Transform.

        Args:
            signal: Input signal.
            window_size: FFT window size.
            hop_size: Hop size between frames.
            window_type: Window function type.

        Returns:
            Tuple of (STFT matrix, num_frames).
        """
        segments, num_frames = self.apply_window(signal, window_size, hop_size, window_type)
        stft_matrix = np.zeros((window_size // 2 + 1, num_frames), dtype=np.complex128)

        for i in range(num_frames):
            stft_matrix[:, i] = np.fft.rfft(segments[i], n=window_size)

        return stft_matrix, num_frames

    def istft(
        self,
        stft_matrix: NDArray[np.complex128],
        hop_size: int = 512,
        window_type: str = "hann",
        output_length: Optional[int] = None,
    ) -> NDArray[np.float64]:
        """
        Compute Inverse Short-Time Fourier Transform.

        Args:
            stft_matrix: STFT matrix from stft().
            hop_size: Hop size used during STFT.
            window_type: Window function type.
            output_length: Expected output length.

        Returns:
            Reconstructed signal.
        """
        window_size = 2 * (stft_matrix.shape[0] - 1)
        num_frames = stft_matrix.shape[1]

        segments = np.zeros((num_frames, window_size), dtype=np.float64)

        for i in range(num_frames):
            segments[i] = np.fft.irfft(stft_matrix[:, i], n=window_size)

        return self.overlap_add_synthesis(segments, hop_size, output_length, window_type)

    def _get_window(self, window_type: str, size: int) -> NDArray[np.float64]:
        """Get window function array."""
        from scipy import signal as sp_signal

        windows = {
            "hann": sp_signal.windows.hann(size),
            "hamming": sp_signal.windows.hamming(size),
            "blackman": sp_signal.windows.blackman(size),
            "bartlett": sp_signal.windows.bartlett(size),
        }
        return windows.get(window_type.lower(), sp_signal.windows.hann(size))
