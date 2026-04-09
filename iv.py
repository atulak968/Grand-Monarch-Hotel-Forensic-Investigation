import numpy as np
# Detect burst starts and ends
diff = np.diff(keying)
starts = np.where(diff == 1)[0]
ends = np.where(diff == -1)[0]
if len(ends) < len(starts):
    ends = np.append(ends, len(keying)-1)

burst_durations = (ends - starts) / fs
gaps = np.diff(starts) / fs

# Simple decoding: treat each burst as '1', each gap as a number of '0's based on duration
# Use median gap as reference for '0' bit length
median_gap = np.median(gaps[gaps < 0.5])  # ignore long inter-message gaps
bits_list = []
for i, gap in enumerate(gaps):
    # number of '0' bits in this gap
    zeros = int(round(gap / median_gap)) if gap < 0.5 else 0
    bits_list.extend([0] * zeros)
    bits_list.append(1)  # the burst itself
# Write as binary string
with open('decoded_bits.bin', 'wb') as f:
    # pack bits into bytes (MSB first)
    byte = 0
    bit_count = 0
    for b in bits_list:
        byte = (byte << 1) | b
        bit_count += 1
        if bit_count == 8:
            f.write(bytes([byte]))
            byte = 0
            bit_count = 0
    if bit_count:
        byte <<= (8 - bit_count)
        f.write(bytes([byte]))
print("Saved decoded_bits.bin – try `file decoded_bits.bin` or `strings decoded_bits.bin`")
