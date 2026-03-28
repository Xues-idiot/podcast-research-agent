"""
Short-Time Fourier Transform Tool Module

Singleton class providing STFT and related spectral
analysis functionality for signal processing.
"""

from typing import Optional, Tuple, Dict
import numpy as np
from numpy.typing import NDArray


class SpectrogramTool:
    """
    Singleton class for STFT spectral analysis.

    Provides spectrogram computation and related
    time-frequency analysis operations.
    """
    _instance: Optional['SpectrogramTool'] = None

    def __new__(cls) -> 'SpectrogramTool':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

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
            signal: Input signal array.
            window_size: FFT window size in samples.
            hop_size: Hop size between frames in samples.
            window_type: Window function type.

        Returns:
            Tuple of (STFT matrix, num_frames).
        """
        from scipy import signal as sp_signal

        window = self._get_window(window_type, window_size)
        num_frames = (len(signal) - window_size) // hop_size + 1

        stft_matrix = np.zeros((window_size // 2 + 1, num_frames), dtype=np.complex128)

        for i in range(num_frames):
            start = i * hop_size
            frame = signal[start : start + window_size] * window
            stft_matrix[:, i] = np.fft.rfft(frame, n=window_size)

        return stft_matrix, num_frames

    def istft(
        self,
        stft_matrix: NDArray[np.complex128],
        hop_size: int = 512,
        window_type: str = "hann",
    ) -> NDArray[np.float64]:
        """
        Compute Inverse Short-Time Fourier Transform.

        Args:
            stft_matrix: STFT matrix from stft().
            hop_size: Hop size used during STFT.
            window_type: Window function type.

        Returns:
            Reconstructed signal.
        """
        from scipy import signal as sp_signal

        window_size = 2 * (stft_matrix.shape[0] - 1)
        window = self._get_window(window_type, window_size)
        num_frames = stft_matrix.shape[1]

        output_length = (num_frames - 1) * hop_size + window_size
        output = np.zeros(output_length, dtype=np.float64)
        window_sum = np.zeros(output_length, dtype=np.float64)

        for i in range(num_frames):
            start = i * hop_size
            frame = np.fft.irfft(stft_matrix[:, i], n=window_size)
            output[start : start + window_size] += frame * window
            window_sum[start : start + window_size] += window**2

        if np.any(window_sum > 0):
            output = output / window_sum

        return output

    def spectrogram(
        self,
        signal: NDArray[np.float64],
        window_size: int = 2048,
        hop_size: int = 512,
        window_type: str = "hann",
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
        """
        Compute magnitude spectrogram.

        Args:
            signal: Input signal.
            window_size: FFT window size.
            hop_size: Hop size.
            window_type: Window function type.

        Returns:
            Tuple of (magnitude spectrogram, frequencies, times).
        """
        stft_matrix, num_frames = self.stft(signal, window_size, hop_size, window_type)
        mag_spectrogram = np.abs(stft_matrix)

        frequencies = np.fft.rfftfreq(window_size, d=1.0 / 44100)
        times = np.arange(num_frames) * hop_size / 44100.0

        return mag_spectrogram, frequencies, times

    def power_spectrogram(
        self,
        signal: NDArray[np.float64],
        window_size: int = 2048,
        hop_size: int = 512,
        window_type: str = "hann",
    ) -> NDArray[np.float64]:
        """
        Compute power spectrogram.

        Args:
            signal: Input signal.
            window_size: FFT window size.
            hop_size: Hop size.
            window_type: Window function type.

        Returns:
            Power spectrogram array.
        """
        stft_matrix, _ = self.stft(signal, window_size, hop_size, window_type)
        return np.abs(stft_matrix) ** 2

    def phase_spectrum(
        self,
        signal: NDArray[np.float64],
        window_size: int = 2048,
        hop_size: int = 512,
        window_type: str = "hann",
    ) -> NDArray[np.float64]:
        """
        Compute phase spectrum.

        Args:
            signal: Input signal.
            window_size: FFT window size.
            hop_size: Hop size.
            window_type: Window function type.

        Returns:
            Phase spectrum array.
        """
        stft_matrix, _ = self.stft(signal, window_size, hop_size, window_type)
        return np.angle(stft_matrix)

    def mel_spectrogram(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
        window_size: int = 2048,
        hop_size: int = 512,
        n_mels: int = 128,
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
        """
        Compute mel-frequency spectrogram.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.
            window_size: FFT window size.
            hop_size: Hop size.
            n_mels: Number of mel frequency bins.

        Returns:
            Tuple of (mel spectrogram, frequencies, times).
        """
        stft_matrix, _ = self.stft(signal, window_size, hop_size)
        mag_spectrogram = np.abs(stft_matrix)

        mel_basis = self._mel_filterbank(sample_rate, window_size, n_mels)
        mel_spec = np.dot(mel_basis, mag_spectrogram**2)

        frequencies = np.fft.rfftfreq(window_size, d=1.0 / sample_rate)
        times = np.arange(stft_matrix.shape[1]) * hop_size / sample_rate

        return mel_spec, frequencies, times

    def _mel_filterbank(
        self, sample_rate: int, n_fft: int, n_mels: int = 128
    ) -> NDArray[np.float64]:
        """Compute mel filterbank matrix."""
        from scipy import signal as sp_signal

        fmin = 0
        fmax = sample_rate / 2

        mel_min = self._hz_to_mel(fmin)
        mel_max = self._hz_to_mel(fmax)
        mel_points = np.linspace(mel_min, mel_max, n_mels + 2)
        hz_points = self._mel_to_hz(mel_points)

        bin_points = np.floor((n_fft + 1) * hz_points / sample_rate).astype(int)
        bin_points = np.clip(bin_points, 0, n_fft // 2)

        filterbank = np.zeros((n_mels, n_fft // 2 + 1))
        for i in range(n_mels):
            left = bin_points[i]
            center = bin_points[i + 1]
            right = bin_points[i + 2]

            for j in range(left, center):
                filterbank[i, j] = (j - left) / (center - left)
            for j in range(center, right):
                filterbank[i, j] = (right - j) / (right - center)

        return filterbank

    def _hz_to_mel(self, hz: float) -> float:
        """Convert Hz to mel scale."""
        return 2595 * np.log10(1 + hz / 700)

    def _mel_to_hz(self, mel: float) -> float:
        """Convert mel scale to Hz."""
        return 700 * (10 ** (mel / 2595) - 1)

    def _get_window(
        self, window_type: str, size: int
    ) -> NDArray[np.float64]:
        """Get window function array."""
        from scipy import signal as sp_signal

        windows = {
            "hann": sp_signal.windows.hann(size),
            "hamming": sp_signal.windows.hamming(size),
            "blackman": sp_signal.windows.blackman(size),
            "bartlett": sp_signal.windows.bartlett(size),
        }
        return windows.get(window_type.lower(), sp_signal.windows.hann(size))
