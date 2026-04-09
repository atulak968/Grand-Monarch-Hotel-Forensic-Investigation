import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]

# Focus on first 30 seconds (where activity was seen)
data_short = data[:30*fs]

plt.figure(figsize=(14, 6))
plt.specgram(data_short, NFFT=256, Fs=fs, cmap='gray', vmin=-40, vmax=0)
plt.ylim(0, 1500)          # up to 1500 Hz to see 630/720/1200
plt.xlim(0, 30)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram - look for short bursts')
plt.colorbar(label='Power (dB)')
plt.savefig('full_spec.png', dpi=150)
print("Saved full_spec.png – look for short, isolated bursts.")

