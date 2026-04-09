import numpy as np
from scipy.io import wavfile
from scipy.signal import hilbert

# =========================
# 1. LOAD AUDIO
# =========================
fs, data = wavfile.read('suspect_image.wav')
if len(data.shape) > 1:
    data = data[:, 0]

data = data.astype(float)
data = data / (np.max(np.abs(data)) + 1e-9)

print(f"[+] Duration: {len(data)/fs:.2f}s")

# =========================
# 2. ENVELOPE + SMOOTH
# =========================
env = np.abs(hilbert(data))
win = int(fs * 0.02)  # 20 ms
smooth = np.convolve(env, np.ones(win)/win, mode='same')
smooth = smooth / (np.max(smooth) + 1e-9)

# =========================
# 3. K-MEANS (2 CLUSTERS) → SIGNAL vs SILENCE
# =========================
# simple 2-means on 1D
c1, c2 = 0.2, 0.8  # init
for _ in range(10):
    d1 = np.abs(smooth - c1)
    d2 = np.abs(smooth - c2)
    lab = (d2 < d1).astype(int)
    if np.any(lab == 0): c1 = smooth[lab == 0].mean()
    if np.any(lab == 1): c2 = smooth[lab == 1].mean()

# choose higher-mean cluster as "signal"
signal = (lab == (1 if c2 > c1 else 0)).astype(int)

# =========================
# 4. REMOVE GLITCHES (CRITICAL)
# =========================
def remove_short_runs(x, min_len):
    out = x.copy()
    n = len(x)
    i = 0
    while i < n:
        j = i
        while j < n and x[j] == x[i]:
            j += 1
        run_len = j - i
        if run_len < min_len:
            out[i:j] = 1 - x[i]  # flip short run
        i = j
    return out

# remove very short ON/OFF bursts (noise)
min_run = int(0.02 * fs)  # 20 ms
signal = remove_short_runs(signal, min_run)

print(f"[+] Active Samples: {signal.sum()}")

# =========================
# 5. EDGE DETECTION
# =========================
diff = np.diff(signal)
starts = np.where(diff == 1)[0]
ends   = np.where(diff == -1)[0]

if signal[0] == 1:
    starts = np.insert(starts, 0, 0)
if signal[-1] == 1:
    ends = np.append(ends, len(signal)-1)

m = min(len(starts), len(ends))
starts, ends = starts[:m], ends[:m]

print(f"[+] Pulses Found: {m}")

if m < 5:
    print("❌ Not enough pulses → likely not Morse")
    exit()

# =========================
# 6. DURATIONS (ms)
# =========================
pulse = (ends - starts) / fs * 1000.0
gap   = (starts[1:] - ends[:-1]) / fs * 1000.0

# trim outliers (robust)
lo, hi = np.percentile(pulse, [10, 90])
pulse = pulse[(pulse >= lo) & (pulse <= hi)]

print(f"[+] Clean Pulses: {len(pulse)}")

if len(pulse) < 5:
    print("❌ Clean pulses too few")
    exit()

# =========================
# 7. DOT/DASH (2 CLUSTERS)
# =========================
p = np.sort(pulse)
mid = len(p)//2
dot_avg  = p[:mid].mean()
dash_avg = p[mid:].mean()
th_dd = (dot_avg + dash_avg) / 2.0

print(f"[+] Dot ≈ {dot_avg:.2f} ms | Dash ≈ {dash_avg:.2f} ms")

# =========================
# 8. GAP CLUSTERS (LETTER/WORD)
# =========================
if len(gap) > 0:
    g = np.sort(gap)
    midg = len(g)//2
    short_g = g[:midg].mean()
    long_g  = g[midg:].mean()
else:
    short_g = long_g = 0

# =========================
# 9. BUILD MORSE
# =========================
morse = []
cur = ""

for i in range(len(pulse)):
    cur += "." if pulse[i] < th_dd else "-"

    if i < len(gap):
        g = gap[i]
        # letter gap
        if g > short_g * 2:
            morse.append(cur)
            cur = ""
        # word gap
        if g > long_g * 1.5:
            morse.append("/")

if cur:
    morse.append(cur)

print("\n[+] Morse:", " ".join(morse))

# =========================
# 10. DECODE
# =========================
M = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E',
    '..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
    '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
    '.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
    '..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
    '/':' '
}

decoded = "".join(M.get(code, '?') for code in morse)
print("\n[+] FINAL DECODED MESSAGE:\n", decoded)
