import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]  # mono

plt.specgram(data, NFFT=512, Fs=fs, cmap='gray')
plt.ylim(0, 2000)  # Morse frequency range
plt.xlim(27, 29)   # Time range where carrier was detected
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram of clean.wav - Look for vertical lines')
plt.savefig('morse_spectrogram.png', dpi=150)
print("Saved morse_spectrogram.png - open this file and look for vertical lines.")
