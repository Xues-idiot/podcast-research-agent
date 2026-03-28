"""
Time Stretching Module for Audio Signals

Singleton class providing time stretching functionality
without affecting pitch for audio processing applications.
"""

from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray


class TimeStretch:
    """
    Singleton class for time stretching audio signals.

    Provides phase vocoder based time stretching to change
    playback speed without altering pitch.
    """
    _instance: Optional['TimeStretch'] = None

    def __new__(cls) -> 'TimeStretch':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def stretch(
        self,
        signal: NDArray[np.float64],
        sample_rate: int,
        stretch_factor: float,
        hop_size: Optional[int] = None,
        window_size: Optional[int] = None,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Stretch audio signal in time.

        Args:
            signal: Input audio signal.
            sample_rate: Sample rate in Hz.
            stretch_factor: Stretch factor (>1 slows down, <1 speeds up).
            hop_size: Analysis hop size in samples.
            window_size: Window size in samples.

        Returns:
            Tuple of (stretched signal, new sample rate).
        """
        if stretch_factor == 1.0:
            return signal, sample_rate

        if window_size is None:
            window_size = 2048
        if hop_size is None:
            hop_size = window_size // 4

        synthesis_hop = int(hop_size * stretch_factor)
        stretched = self._phase_vocoder_stretch(
            signal, window_size, hop_size, synthesis_hop
        )
        return stretched, sample_rate

    def _phase_vocoder_stretch(
        self,
        signal: NDArray[np.float64],
        window_size: int,
        analysis_hop: int,
        synthesis_hop: int,
    ) -> NDArray[np.float64]:
        """
        Phase vocoder based time stretching.

        Args:
            signal: Input signal.
            window_size: FFT window size.
            analysis_hop: Input hop size.
            synthesis_hop: Output hop size.

        Returns:
            Time-stretched signal.
        """
        from scipy import signal as sp_signal

        fft_size = window_size
        win = sp_signal.windows.hann(fft_size)

        num_frames = (len(signal) - fft_size) // analysis_hop
        if num_frames <= 0:
            return signal

        stretched_length = num_frames * synthesis_hop + fft_size
        stretched = np.zeros(stretched_length, dtype=np.float64)

        phase_accum = np.zeros(fft_size // 2 + 1, dtype=np.float64)
        prev_phase = np.zeros(fft_size // 2 + 1, dtype=np.float64)

        for i in range(num_frames):
            start = i * analysis_hop
            frame = signal[start : start + fft_size] * win

            fft_result = np.fft.rfft(frame)
            mag = np.abs(fft_result)
            phase = np.angle(fft_result)

            phase_diff = phase - prev_phase
            prev_phase = phase

            phase_diff_unwrapped = np.unwrap(phase_diff)
            true_freq = phase_diff_unwrapped / (2 * np.pi * analysis_hop)
            phase_accum += true_freq * 2 * np.pi * synthesis_hop

            new_fft = mag * np.exp(1j * phase_accum)
            new_frame = np.fft.irfft(new_fft, n=fft_size)

            synth_start = i * synthesis_hop
            stretched[synth_start : synth_start + fft_size] += new_frame * win

        return self._normalize(stretched)

    def compress(
        self,
        signal: NDArray[np.float64],
        sample_rate: int,
        compress_factor: float,
        hop_size: Optional[int] = None,
        window_size: Optional[int] = None,
    ) -> Tuple[NDArray[np.float64], int]:
        """
        Compress audio signal in time (inverse of stretch).

        Args:
            signal: Input audio signal.
            sample_rate: Sample rate in Hz.
            compress_factor: Compression factor (>1 speeds up).
            hop_size: Analysis hop size in samples.
            window_size: Window size in samples.

        Returns:
            Tuple of (compressed signal, sample rate).
        """
        return self.stretch(signal, sample_rate, 1.0 / compress_factor, hop_size, window_size)

    def _normalize(self, signal: NDArray[np.float64]) -> NDArray[np.float64]:
        """Normalize signal to prevent clipping."""
        max_val = np.abs(signal).max()
        if max_val > 1.0:
            return signal / max_val
        return signal
