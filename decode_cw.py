import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]

# Envelope detection (rectify + lowpass)
from scipy.signal import butter, lfilter
env = np.abs(data)
b, a = butter(4, 100/(fs/2), btype='low')
envelope = lfilter(b, a, env)

# Threshold to get on/off
threshold = envelope.max() * 0.3
keying = envelope > threshold

# Find transitions
diff = np.diff(keying.astype(int))
on_starts = np.where(diff == 1)[0]
on_ends = np.where(diff == -1)[0]
if len(on_ends) < len(on_starts):
    on_ends = np.append(on_ends, len(keying)-1)

durations = (on_ends - on_starts) / fs
print("On durations (seconds):", durations)
# Classify: short (<0.2s?) = dot, long = dash

