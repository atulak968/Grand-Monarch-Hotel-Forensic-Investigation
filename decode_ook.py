import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter, sosfilt

fs, data = wav.read('clean.wav')
if len(data.shape) > 1:
    data = data[:, 0]

def extract_bits(band_low, band_high, factor=2.5, reverse_bits=False, period_scale=1.0):
    sos = butter(4, [band_low, band_high], btype='band', fs=fs, output='sos')
    filtered = sosfilt(sos, data)
    env = np.abs(filtered)
    b, a = butter(4, 500/(fs/2), btype='low')
    envelope = lfilter(b, a, env)
    threshold = np.median(envelope) * factor
    keying = (envelope > threshold).astype(int)
    diff = np.diff(keying)
    starts = np.where(diff == 1)[0]
    ends = np.where(diff == -1)[0]
    if len(ends) < len(starts):
        ends = np.append(ends, len(keying)-1)
    if len(starts) == 0:
        return None
    gaps = np.diff(starts) / fs
    short_gaps = gaps[gaps < 0.5]
    if len(short_gaps) == 0:
        return None
    bit_period = np.median(short_gaps) * period_scale
    bits = []
    for gap in gaps:
        zeros = int(round(gap / bit_period)) if gap < 0.5 else 0
        bits.extend([0] * zeros)
        bits.append(1)
    if reverse_bits:
        bits = bits[::-1]
    # Pack into bytes
    byte_arr = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            if i+j < len(bits):
                byte = (byte << 1) | bits[i+j]
            else:
                byte <<= 1
        byte_arr.append(byte)
    return byte_arr

# Try all combinations
for (low, high, name) in [(600,800,'600_800'), (1100,1300,'1100_1300')]:
    for rev in [False, True]:
        for scale in [0.9, 1.0, 1.1]:
            data_bytes = extract_bits(low, high, reverse_bits=rev, period_scale=scale)
            if data_bytes:
                fname = f"decoded_{name}_rev{rev}_scale{scale}.bin"
                with open(fname, 'wb') as f:
                    f.write(data_bytes)
                print(f"Saved {len(data_bytes)} bytes to {fname}")
