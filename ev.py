import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter, sosfilt

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]

# Bandpass around strongest carrier (e.g., 600-800 Hz)
sos = butter(4, [600, 800], btype='band', fs=fs, output='sos')
filtered = sosfilt(sos, data)

# Envelope
env = np.abs(filtered)
b, a = butter(4, 500/(fs/2), btype='low')  # 500 Hz cutoff to follow fast bursts
envelope = lfilter(b, a, env)

# Adaptive threshold
threshold = np.median(envelope) * 2.5
keying = (envelope > threshold).astype(int)

# Write raw bits to file (1 bit per sample? No, too many. Better to downsample)
# Instead, record transitions: 1 = burst, 0 = gap
bits = keying.astype(np.uint8)
np.savetxt('raw_bits.txt', bits, fmt='%d', delimiter='')

print(f"Saved raw_bits.txt – length {len(bits)} samples at {fs} Hz")
