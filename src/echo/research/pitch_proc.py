"""
Pitch Processing Module

Singleton class providing pitch shifting functionality
for audio signals without affecting tempo.
"""

from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray


class PitchProc:
    """
    Singleton class for pitch shifting audio signals.

    Provides pitch shifting using phase vocoder and
    resampling techniques for audio effect applications.
    """
    _instance: Optional['PitchProc'] = None

    def __new__(cls) -> 'PitchProc':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def shift(
        self,
        signal: NDArray[np.float64],
        sample_rate: int,
        semitones: float,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Shift pitch by semitones.

        Args:
            signal: Input audio signal.
            sample_rate: Sample rate in Hz.
            semitones: Number of semitones to shift (positive up, negative down).

        Returns:
            Tuple of (pitch-shifted signal, sample rate).
        """
        if semitones == 0:
            return signal, sample_rate

        pitch_factor = 2 ** (semitones / 12.0)
        stretched, rate = self._time_stretch_and_resample(
            signal, sample_rate, pitch_factor
        )
        return stretched, rate

    def shift_octaves(
        self,
        signal: NDArray[np.float64],
        sample_rate: int,
        octaves: float,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Shift pitch by octaves.

        Args:
            signal: Input audio signal.
            sample_rate: Sample rate in Hz.
            octaves: Number of octaves to shift.

        Returns:
            Tuple of (pitch-shifted signal, sample rate).
        """
        semitones = octaves * 12.0
        return self.shift(signal, sample_rate, semitones)

    def shift_hz(
        self,
        signal: NDArray[np.float64],
        sample_rate: int,
        freq_shift: float,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Shift pitch by frequency in Hz.

        Args:
            signal: Input audio signal.
            sample_rate: Sample rate in Hz.
            freq_shift: Frequency shift in Hz.

        Returns:
            Tuple of (pitch-shifted signal, sample rate).
        """
        from scipy import signal as sp_signal

        min_freq = 20.0
        max_freq = sample_rate / 2.0 - 100.0

        dominant_freq = self._estimate_dominant_freq(signal, sample_rate)
        if dominant_freq <= 0:
            dominant_freq = 440.0

        target_freq = dominant_freq + freq_shift
        target_freq = max(min_freq, min(max_freq, target_freq))

        semitones = 12.0 * np.log2(target_freq / dominant_freq)
        return self.shift(signal, sample_rate, semitones)

    def _time_stretch_and_resample(
        self, signal: NDArray[np.float64], sample_rate: int, pitch_factor: float
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Time stretch by pitch factor and resample back.

        Args:
            signal: Input signal.
            sample_rate: Sample rate.
            pitch_factor: Pitch multiplication factor.

        Returns:
            Tuple of (processed signal, new sample rate).
        """
        from scipy import signal as sp_signal

        stretch_factor = 1.0 / pitch_factor
        window_size = 2048
        hop_size = window_size // 4

        stretched_length = int(len(signal) * stretch_factor)
        stretched = np.zeros(stretched_length, dtype=np.float64)

        win = sp_signal.windows.hann(window_size)
        num_frames = (len(signal) - window_size) // hop_size

        for i in range(num_frames):
            start = i * hop_size
            frame = signal[start : start + window_size] * win
            fft_result = np.fft.rfft(frame)
            mag = np.abs(fft_result)
            phase = np.angle(fft_result)

            new_fft = mag * np.exp(1j * phase)
            new_frame = np.fft.irfft(new_fft, n=window_size)

            synth_start = int(i * hop_size * stretch_factor)
            end = synth_start + window_size
            if end <= stretched_length:
                stretched[synth_start:end] += new_frame * win

        new_rate = int(sample_rate * pitch_factor)
        stretched = stretched / np.abs(stretched).max() if np.abs(stretched).max() > 0 else stretched

        return stretched, new_rate

    def _estimate_dominant_freq(
        self, signal: NDArray[np.float64], sample_rate: int
    ) -> float:
        """
        Estimate dominant frequency using autocorrelation.

        Args:
            signal: Input signal.
            sample_rate: Sample rate.

        Returns:
            Dominant frequency in Hz.
        """
        from scipy import signal as sp_signal

        autocorr = sp_signal.correlate(signal, signal, mode='full')
        autocorr = autocorr[len(autocorr) // 2:]

        min_lag = int(sample_rate / 1000)
        max_lag = int(sample_rate / 50)

        if max_lag >= len(autocorr):
            return 440.0

        peak_idx = np.argmax(autocorr[min_lag:max_lag]) + min_lag
        if peak_idx == 0:
            return 440.0

        return sample_rate / peak_idx
