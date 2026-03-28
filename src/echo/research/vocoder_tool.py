"""
Phase Vocoder Tool Module

Singleton class providing phase vocoder functionality
for time-stretching and pitch-shifting audio signals.
"""

from typing import Optional, Tuple, Dict
import numpy as np
from numpy.typing import NDArray


class VocoderTool:
    """
    Singleton class for phase vocoder operations.

    Implements phase vocoder algorithm for high-quality
    time stretching and pitch shifting of audio signals.
    """
    _instance: Optional['VocoderTool'] = None

    def __new__(cls) -> 'VocoderTool':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self._initialized = True

    def analyze(
        self,
        signal: NDArray[np.float64],
        window_size: int = 2048,
        hop_size: int = 512,
    ) -> Dict[str, NDArray]:
        """
        Analyze signal using STFT.

        Args:
            signal: Input signal.
            window_size: FFT window size.
            hop_size: Hop size between frames.

        Returns:
            Dictionary with 'mag' and 'phase' arrays.
        """
        from scipy import signal as sp_signal

        win = sp_signal.windows.hann(window_size)
        num_frames = (len(signal) - window_size) // hop_size + 1

        stft_matrix = np.zeros((window_size // 2 + 1, num_frames), dtype=np.complex128)

        for i in range(num_frames):
            start = i * hop_size
            frame = signal[start : start + window_size] * win
            stft_matrix[:, i] = np.fft.rfft(frame)

        mag = np.abs(stft_matrix)
        phase = np.angle(stft_matrix)

        return {"mag": mag, "phase": phase, "hop_size": hop_size, "window_size": window_size}

    def synthesize(
        self,
        analysis: Dict[str, NDArray],
        synthesis_hop: Optional[int] = None,
    ) -> NDArray[np.float64]:
        """
        Synthesize signal from STFT representation.

        Args:
            analysis: Analysis dictionary from analyze().
            synthesis_hop: Synthesis hop size (default: same as analysis).

        Returns:
            Reconstructed signal.
        """
        from scipy import signal as sp_signal

        mag = analysis["mag"]
        phase = analysis["phase"]
        window_size = analysis["window_size"]
        hop_size = analysis["hop_size"]

        if synthesis_hop is None:
            synthesis_hop = hop_size

        win = sp_signal.windows.hann(window_size)
        num_frames = mag.shape[1]

        output_length = (num_frames - 1) * synthesis_hop + window_size
        output = np.zeros(output_length, dtype=np.float64)

        for i in range(num_frames):
            stft_frame = mag[:, i] * np.exp(1j * phase[:, i])
            time_frame = np.fft.irfft(stft_frame, n=window_size)
            start = i * synthesis_hop
            output[start : start + window_size] += time_frame * win

        return self._normalize(output)

    def time_stretch(
        self,
        signal: NDArray[np.float64],
        stretch_factor: float,
        window_size: int = 2048,
        hop_size: int = 512,
    ) -> NDArray[np.float64]:
        """
        Stretch signal in time using phase vocoder.

        Args:
            signal: Input signal.
            stretch_factor: Stretch factor (>1 slows down).
            window_size: FFT window size.
            hop_size: Analysis hop size.

        Returns:
            Time-stretched signal.
        """
        from scipy import signal as sp_signal

        analysis_hop = hop_size
        synthesis_hop = int(analysis_hop * stretch_factor)

        win = sp_signal.windows.hann(window_size)
        num_frames = (len(signal) - window_size) // analysis_hop + 1

        output_length = int((len(signal) / analysis_hop) * synthesis_hop) + window_size
        output = np.zeros(output_length, dtype=np.float64)

        phase_accum = np.zeros(window_size // 2 + 1, dtype=np.float64)
        prev_phase = np.zeros(window_size // 2 + 1, dtype=np.float64)

        for i in range(num_frames):
            start = i * analysis_hop
            frame = signal[start : start + window_size] * win

            fft_result = np.fft.rfft(frame)
            mag = np.abs(fft_result)
            phase = np.angle(fft_result)

            phase_diff = phase - prev_phase
            prev_phase = phase

            phase_diff_unwrapped = np.unwrap(phase_diff)
            instant_freq = phase_diff_unwrapped / (2 * np.pi * analysis_hop)
            phase_accum += instant_freq * 2 * np.pi * synthesis_hop

            new_fft = mag * np.exp(1j * phase_accum)
            new_frame = np.fft.irfft(new_fft, n=window_size)

            synth_start = i * synthesis_hop
            output[synth_start : synth_start + window_size] += new_frame * win

        return self._normalize(output)

    def _normalize(self, signal: NDArray[np.float64]) -> NDArray[np.float64]:
        """Normalize signal to prevent clipping."""
        max_val = np.abs(signal).max()
        if max_val > 1.0:
            return signal / max_val
        return signal
