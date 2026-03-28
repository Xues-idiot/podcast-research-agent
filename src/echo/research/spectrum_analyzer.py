"""
Spectrum Analyzer Module

Singleton class providing spectral analysis functionality
for audio and signal processing applications.
"""

from typing import Optional, Tuple, Dict, List
import numpy as np
from numpy.typing import NDArray


class SpectrumAnalyzer:
    """
    Singleton class for spectral analysis operations.

    Provides frequency analysis, spectral features,
    and spectrum visualization utilities.
    """
    _instance: Optional['SpectrumAnalyzer'] = None

    def __new__(cls) -> 'SpectrumAnalyzer':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def fft(
        self,
        signal: NDArray[np.float64],
        n: Optional[int] = None,
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Compute FFT and return magnitude and phase.

        Args:
            signal: Input signal.
            n: FFT size (default: signal length).

        Returns:
            Tuple of (magnitudes, frequencies).
        """
        if n is None:
            n = len(signal)

        fft_result = np.fft.rfft(signal, n=n)
        magnitudes = np.abs(fft_result)
        frequencies = np.fft.rfftfreq(n, d=1.0 / 44100)

        return magnitudes, frequencies

    def power_spectrum(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
        n: Optional[int] = None,
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Compute power spectrum density.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.
            n: FFT size.

        Returns:
            Tuple of (power spectrum, frequencies).
        """
        if n is None:
            n = len(signal)

        fft_result = np.fft.rfft(signal, n=n)
        power = np.abs(fft_result) ** 2 / n
        frequencies = np.fft.rfftfreq(n, d=1.0 / sample_rate)

        return power, frequencies

    def amplitude_spectrum(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
        n: Optional[int] = None,
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Compute amplitude spectrum.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.
            n: FFT size.

        Returns:
            Tuple of (amplitude spectrum, frequencies).
        """
        if n is None:
            n = len(signal)

        fft_result = np.fft.rfft(signal, n=n)
        amplitude = 2 * np.abs(fft_result) / n
        frequencies = np.fft.rfftfreq(n, d=1.0 / sample_rate)

        return amplitude, frequencies

    def spectral_centroid(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
    ) -> float:
        """
        Compute spectral centroid (center of mass).

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.

        Returns:
            Spectral centroid frequency in Hz.
        """
        magnitudes, frequencies = self.fft(signal)

        if magnitudes.sum() == 0:
            return 0.0

        centroid = np.sum(magnitudes * frequencies) / np.sum(magnitudes)
        return float(centroid)

    def spectral_bandwidth(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
    ) -> float:
        """
        Compute spectral bandwidth.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.

        Returns:
            Spectral bandwidth in Hz.
        """
        magnitudes, frequencies = self.fft(signal)

        if magnitudes.sum() == 0:
            return 0.0

        centroid = self.spectral_centroid(signal, sample_rate)
        bandwidth = np.sqrt(
            np.sum(magnitudes * (frequencies - centroid) ** 2) / np.sum(magnitudes)
        )
        return float(bandwidth)

    def spectral_rolloff(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
        rolloff_percent: float = 0.85,
    ) -> float:
        """
        Compute spectral rolloff point.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.
            rolloff_percent: Percentage of total energy (default 85%).

        Returns:
            Spectral rolloff frequency in Hz.
        """
        magnitudes, frequencies = self.fft(signal)
        cumsum = np.cumsum(magnitudes**2)
        total = cumsum[-1]

        if total == 0:
            return 0.0

        threshold = rolloff_percent * total
        rolloff_idx = np.searchsorted(cumsum, threshold)

        if rolloff_idx >= len(frequencies):
            return float(frequencies[-1])

        return float(frequencies[rolloff_idx])

    def spectral_flatness(
        self,
        signal: NDArray[np.float64],
    ) -> float:
        """
        Compute spectral flatness (Wiener entropy).

        Args:
            signal: Input signal.

        Returns:
            Spectral flatness measure.
        """
        magnitudes, _ = self.fft(signal)

        geometric_mean = np.exp(np.mean(np.log(magnitudes + 1e-10)))
        arithmetic_mean = np.mean(magnitudes)

        if arithmetic_mean == 0:
            return 0.0

        flatness = geometric_mean / arithmetic_mean
        return float(flatness)

    def spectral_features(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
    ) -> Dict[str, float]:
        """
        Compute all spectral features.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.

        Returns:
            Dictionary of spectral features.
        """
        return {
            "centroid": self.spectral_centroid(signal, sample_rate),
            "bandwidth": self.spectral_bandwidth(signal, sample_rate),
            "rolloff_85": self.spectral_rolloff(signal, sample_rate, 0.85),
            "rolloff_95": self.spectral_rolloff(signal, sample_rate, 0.95),
            "flatness": self.spectral_flatness(signal),
        }

    def peak_frequencies(
        self,
        signal: NDArray[np.float64],
        sample_rate: int = 44100,
        num_peaks: int = 10,
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Find dominant peak frequencies.

        Args:
            signal: Input signal.
            sample_rate: Sample rate in Hz.
            num_peaks: Number of peaks to find.

        Returns:
            Tuple of (peak frequencies, peak magnitudes).
        """
        magnitudes, frequencies = self.fft(signal)

        from scipy.signal import find_peaks
        peaks, properties = find_peaks(magnitudes, height=np.max(magnitudes) * 0.1)

        if len(peaks) == 0:
            return np.array([]), np.array([])

        sorted_indices = np.argsort(magnitudes[peaks])[::-1][:num_peaks]
        peak_freqs = frequencies[peaks[sorted_indices]]
        peak_mags = magnitudes[peaks[sorted_indices]]

        return peak_freqs, peak_mags

    def spectrum_db(
        self,
        signal: NDArray[np.float64],
    ) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Compute spectrum in decibels.

        Args:
            signal: Input signal.

        Returns:
            Tuple of (spectrum in dB, frequencies).
        """
        magnitudes, frequencies = self.fft(signal)
        spectrum_db = 20 * np.log10(magnitudes + 1e-10)
        return spectrum_db, frequencies
