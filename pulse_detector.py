import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter, sosfilt

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]

# Bandpass around the strongest carrier (e.g., 600-800 Hz)
sos = butter(4, [600, 800], btype='band', fs=fs, output='sos')
filtered = sosfilt(sos, data)

# Envelope
env = np.abs(filtered)
b, a = butter(4, 200/(fs/2), btype='low')
envelope = lfilter(b, a, env)

# Adaptive threshold: median of envelope * 2.5
threshold = np.median(envelope) * 2.5

# Binary signal
keying = (envelope > threshold).astype(int)

# Find transitions
diff = np.diff(keying)
on_starts = np.where(diff == 1)[0]
on_ends = np.where(diff == -1)[0]
if len(on_ends) < len(on_starts):
    on_ends = np.append(on_ends, len(keying)-1)

burst_durations = (on_ends - on_starts) / fs
gaps = np.diff(on_starts) / fs

print(f"Number of bursts: {len(burst_durations)}")
print(f"Burst durations (seconds): {burst_durations}")
print(f"Gaps between bursts (seconds): {gaps}")

# Classify as dot/dash if most durations fall into two clusters
if len(burst_durations) > 0:
    short = burst_durations[burst_durations < 0.2]
    long = burst_durations[burst_durations >= 0.2]
    print(f"Short bursts (<0.2s): {len(short)}  |  Long bursts (≥0.2s): {len(long)}")

