import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]

# Bandpass filter around expected carrier (700-900 Hz) to remove noise
from scipy.signal import butter, sosfilt
sos = butter(4, [700, 900], btype='band', fs=fs, output='sos')
filtered = sosfilt(sos, data)

# Envelope detection (rectify + lowpass)
env = np.abs(filtered)
b, a = butter(4, 100/(fs/2), btype='low')
envelope = lfilter(b, a, env)

# Plot first 2 seconds to see detail
time = np.arange(len(data)) / fs
plt.figure(figsize=(12, 8))
plt.subplot(3,1,1)
plt.plot(time, data, alpha=0.5)
plt.title('Raw audio (first 2 sec)')
plt.xlim(0, 2)

plt.subplot(3,1,2)
plt.plot(time, filtered, alpha=0.5)
plt.title('Bandpassed (700-900 Hz)')
plt.xlim(0, 2)

plt.subplot(3,1,3)
plt.plot(time, envelope, label='Envelope')
threshold = envelope.max() * 0.3
plt.axhline(threshold, color='r', linestyle='--', label='Threshold')
plt.title('Envelope & threshold')
plt.xlim(0, 2)
plt.legend()
plt.tight_layout()
plt.savefig('envelope_check.png')
print("Saved envelope_check.png – open it and look for on/off pattern.")

