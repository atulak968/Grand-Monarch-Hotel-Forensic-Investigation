# 🔍 DFIA299 Capstone Project – Grand Monarch Hotel Forensic Investigation

## Case: Death of Clara Benson (Room 718, May 20, 2025)

![Status](https://img.shields.io/badge/Status-Completed-success)
![Forensics](https://img.shields.io/badge/Digital_Forensics-Success-blue)
![Tools](https://img.shields.io/badge/Tools-SleuthKit%20%7C%20Sox%20%7C%20Python-orange)
![Course](https://img.shields.io/badge/Course-DFIA299_Capstone-red)
![Student](https://img.shields.io/badge/Student-2025CFP7076_Atul_Paswan-green)

---

## 📌 Table of Contents

- [Case Overview](#-case-overview)
- [Key Findings](#-key-findings)
- [Investigation Methodology](#-investigation-methodology)
- [Tools Used](#-tools-used)
- [Complete File Structure](#-complete-file-structure)
- [Evidence Analysis](#-evidence-analysis)
- [Audio Forensics Details](#-audio-forensics-details)
- [Decoding & Decryption](#-decoding--decryption)
- [Incident Reconstruction](#-incident-reconstruction)
- [Timeline of Events](#-timeline-of-events)
- [Chain of Custody](#-chain-of-custody)
- [How to Reproduce](#-how-to-reproduce)
- [Report](#-report)
- [Author](#-author)
- [License](#-license)

---

## 📋 Case Overview

| **Detail** | **Information** |
|------------|-----------------|
| **Incident** | Death of Ms. Clara Benson |
| **Location** | Room 718, Grand Monarch Hotel |
| **Date** | May 20, 2025 |
| **Time** | Approximately 10:00 PM |
| **Primary Suspect** | Marcus Langston |
| **Evidence Source** | USB Disk Image (`Mrs_Clara_Benson_case_image.001`) |
| **Student Name** | Atul Paswan |
| **Student ID** | 2025CFP7076 |
| **Course** | DFIA299 Capstone Project |

### Background

On May 20, 2025, Ms. Clara Benson was found deceased in Room 718 of the Grand Monarch Hotel. A USB storage device was recovered from Marcus Langston, the prime suspect. This investigation conducted a complete forensic analysis of the USB disk image to uncover hidden communications, encoded messages, steganographic content, and the full murder conspiracy.

---

## 🔑 Key Findings

| # | Finding | Evidence Source |
|---|---------|-----------------|
| 1 | Marcus Langston confessed to murder | `confession.txt` (Base64 decoded) |
| 2 | Hidden Morse message: `"THE TRUTH IS IN ROOM 718"` | Audio forensics (`clean.wav`) |
| 3 | PGP Public Key recovered | `pgp_pubkey.bin`, `pgp_seckey1.bin`, `pgp_seckey2.bin` |
| 4 | Encrypted archive found | `pex_archive.pgp`, `pex_archive.zip`, `pex_archive.gz` |
| 5 | Steganography extracted | `secret.txt`, `recovered_partner.jpg` |
| 6 | OOK decoded binaries | `decoded_600_800_*.bin`, `decoded_1100_1300_*.bin` |
| 7 | Zlib compressed data extracted | `zlib_data.bin`, `decompressed.bin` |
| 8 | Hidden audio recovered | `hidden_audio.wav` |
| 9 | PCAP file recovered | `pex_test.pcap` |
| 10 | Transcript decoded | `transcript.txt` |

---

## 🔬 Investigation Methodology
┌─────────────────────────────────────────────────────────────────┐
│ Digital Forensic Process Flow │
├─────────────────────────────────────────────────────────────────┤
│ │
│ 1. Image Verification ──────────► 2. Disk Analysis │
│ │ │ │
│ ▼ ▼ │
│ 3. File Carving ──────────────────► 4. Data Recovery │
│ │ │ │
│ ▼ ▼ │
│ 5. Audio Forensics ────────────────► 6. Steganography │
│ │ │ │
│ ▼ ▼ │
│ 7. Decoding/Decryption ────────────► 8. PGP Analysis │
│ │ │ │
│ ▼ ▼ │
│ 9. Zlib Decompression ────────────► 10. Timeline Creation │
│ │
└─────────────────────────────────────────────────────────────────


---

## 🛠️ Tools Used

| Category | Tools |
|----------|-------|
| **Disk Imaging & Verification** | `md5sum`, `sha1sum` |
| **Disk & File System Analysis** | `mmls`, `fls`, `icat` (Sleuth Kit) |
| **File Carving** | `foremost`, `scalpel`, `bulk_extractor` |
| **Audio Processing** | `sox`, `audacity` |
| **Demodulation** | `minimodem`, `multimon-ng` |
| **Steganography** | `steghide`, `zsteg` |
| **PGP/GPG Analysis** | `gpg`, `pgpdump` |
| **PCAP Analysis** | `tshark`, `wireshark` |
| **Python Libraries** | NumPy, SciPy, Matplotlib, scikit-image, pyzlib |
| **Compression** | `gunzip`, `unzip`, `zlib` |
| **Analysis & Visualization** | `xxd`, `strings`, `hexdump`, `binwalk` |

---

## 📁 Complete File Structure
DFIA299 - Capstone Project_Digital_Forensics_2025CFP7076_Atul_Paswan/
│
├── 📄 2025CFP7076__DFIA299 - Capstone Project_Digital_Forensics_Atul_Paswan.pdf
│
├── 🖼️ Evidence Images & Audio
│ ├── suspect_image.wav # Original audio evidence
│ ├── suspect_image.bmp # Original image evidence
│ ├── clean.wav # Filtered audio (600-800 Hz bandpass)
│ ├── hidden_audio.wav # Extracted hidden audio
│ ├── filtered.wav # Bandpass filtered version
│ ├── settings.wav # Additional audio evidence
│ └── bw.png # Black & white processed image
│
├── 🎵 Audio Spectrograms
│ ├── morse_spectrogram.png # Morse code visualization
│ ├── full_spec.png # Full frequency spectrogram
│ ├── envelope_check.png # Envelope detection plot
│ └── final_clean.png # Final processed spectrogram
│
├── 🔓 Decoded Outputs (OOK Demodulation)
│ ├── decoded_600_800_revFalse_scale0.9.bin
│ ├── decoded_600_800_revFalse_scale1.0.bin
│ ├── decoded_600_800_revFalse_scale1.1.bin
│ ├── decoded_600_800_revTrue_scale0.9.bin
│ ├── decoded_600_800_revTrue_scale1.0.bin
│ ├── decoded_600_800_revTrue_scale1.1.bin
│ ├── decoded_1100_1300_revFalse_scale0.9.bin
│ ├── decoded_1100_1300_revFalse_scale1.0.bin
│ ├── decoded_1100_1300_revFalse_scale1.1.bin
│ └── decoded_data_1200Hz.bin
│
├── 🔐 PGP & Encryption Analysis
│ ├── pgp_pubkey.bin # PGP Public Key
│ ├── pgp_seckey1.bin # PGP Secret Key 1
│ ├── pgp_seckey2.bin # PGP Secret Key 2
│ ├── key.bin # Extracted key material
│ ├── key.txt # Key in text format
│ ├── pex_archive.pgp # PGP encrypted archive
│ ├── pex_archive.zip # ZIP archive
│ ├── pex_archive.gz # GZIP compressed
│ ├── pex.bin # Raw PGP binary
│ ├── pex_test.gz # Test GZIP file
│ └── pex_test.zip # Test ZIP file
│
├── 📦 Decompressed & Extracted Data
│ ├── zlib_data.bin # Raw zlib compressed data
│ ├── decompressed.bin # Decompressed output
│ ├── decompressed_153.bin # Decompressed at offset 153
│ ├── decompressed_at_offset_153.bin # Alternative decompression
│ ├── extracted_zlib.bin # Extracted zlib stream
│ ├── transcript.bin # Binary transcript
│ ├── transcript.txt # Decoded transcript text
│ ├── hidden_data.b64 # Base64 hidden data
│ └── msb_combined_all.bin # MSB combined extraction
│
├── 📂 Offset Analysis Files
│ ├── offset_718.bin # Data at offset 718
│ ├── offset_718718.bin # Data at offset 718718
│ ├── offset_945.bin # Data at offset 945
│ └── offset_94545.bin # Data at offset 94545
│
├── 📜 Recovered Evidence
│ ├── confession.txt # Decoded confession (Base64)
│ ├── secret.txt # Steganography extracted text
│ ├── recovered_partner.jpg # Recovered image of accomplice
│ ├── final_bmp/ # Recovered BMP images
│ ├── recovered_audio_final/ # Final recovered audio files
│ ├── recovered_files/ # All carved files
│ ├── audio_carve/ # Audio carving output
│ ├── audio_carve_all/ # Complete audio carving
│ ├── carved_output/ # General carving output
│ ├── evidence_files/ # Organized evidence
│ └── unallocated_space.bin # Unallocated space dump
│
├── 🐍 Python Analysis Scripts
│ ├── decode_cw.py # Morse code decoder
│ ├── decode_morse.py # Alternative Morse decoder
│ ├── decode_ook.py # OOK demodulation main
│ ├── inspect_cw.py # CW signal inspection
│ ├── iv.py # Interval analysis
│ ├── ev.py # Envelope validation
│ ├── pulse_detector.py # Burst detection
│ ├── spec.py # Spectrogram generator
│ ├── view_spec.py # Spectrogram viewer
│ └── raw_bits.txt # Raw bit extraction output
│
├── 📊 Analysis Outputs
│ ├── bodyfile.txt # Sleuth Kit bodyfile
│ ├── timeline.csv # Timeline of events
│ ├── output.txt # General output log
│ ├── pex_test.pcap # Network capture file
│ └── settings.dat # Settings data
│
├── 📸 Screenshots/
│ └── [All forensic procedure screenshots]
│
├── 📄 Documentation Files
│ ├── docProps/ # Document properties
│ └── styles_raw.xml # Raw XML styles
│
└── 💾 Disk Image
   └──Mrs_Clara_Benson_case_image.001.txt
   └── Mrs_Clara_Benson_case_image.001 # Main disk image 

---

## 📊 Evidence Analysis

### 1. Disk Image Verification

| Hash Type | Value | Status |
|-----------|-------|--------|
| **MD5** | `583bb23631d54dfe5446f1f094681f30` | ✅ Verified |
| **SHA1** | `467176bdfeffef80f8fde152a187575735023dbea` | ✅ Verified |

### 2. Partition Layout (from `mmls`)

| Slot | Start (sector) | End | Length | Description |
|------|----------------|-----|--------|-------------|
| 00 | 0 | 0 | 1 | Primary Table |
| 01 | 0 | 127 | 128 | Unallocated |
| 02 | 128 | 1,987,763 | 1,987,636 | NTFS (0×07) |
| 03 | 1,987,840 | 2,047,999 | 60,160 | Unallocated |

### 3. Recovered & Deleted Files

| File | Status | Method |
|------|--------|--------|
| `murder_plan.docx` | Recovered (scrambled) | File carving |
| `Encrypted Letter.docx` | Recovered | File carving |
| `secret.txt` | Extracted | Steganography (passphrase: `monarch`) |
| `suspect_image.wav` | Recovered | Direct extraction |
| `pgp_pubkey.bin` | Recovered | PGP analysis |
| `pex_archive.pgp` | Recovered | Encryption analysis |
| `recovered_partner.jpg` | Recovered | Image carving |

---

## 🎵 Audio Forensics Details

### Process Flow
suspect_image.wav
│
▼
sox bandpass 600-800 Hz
│
▼
clean.wav
│
▼
Spectrogram Analysis
│
├──► morse_spectrogram.png (vertical lines below 500 Hz)
│
▼
Envelope Detection (Python)
│
▼
OOK Demodulation
│
├──► 600-800 Hz bandpass
├──► 1100-1300 Hz bandpass
├──► Bit period: 13-15 ms
├──► Scale: 0.9, 1.0, 1.1
└──► Bit order: normal & reversed
│
▼
Decoded Binaries
│
▼
Morse Message Extracted

### Extracted Morse Message
THE TRUTH IS IN ROOM 718


### Spectrogram Analysis Results

| Observation | Interpretation |
|-------------|----------------|
| Vertical lines below 500 Hz | OOK bursts (on-off keying) |
| Burst duration ~5 ms | High-speed data (200 baud) |
| Gaps: 0.0004s to 5.66s | Variable spacing (data packets) |
| Carriers at 630 Hz, 720 Hz, 1200 Hz | Multiple frequency components |

---

## 🔓 Decoding & Decryption

### Base64 Decoded Confession

**Original:**U29ycnsIEkgY291bGQgbm90IG1ha2UgdxAgbXkgbWluZcWgYnV0IGhlcmUgaXmgdGhIGFjdHvHbCBjb25mZXnzaW9uOiAKTWlIdCBtZSbhdCB0aGUgY2FzYSwgSSdtIHJ1WRSLg==

**Decoded:**Sorry, I could not make up my mind but here is the confession:
Meet me at the case, I'm Ready..."

### Steganography Extraction

| Parameter | Value |
|-----------|-------|
| Carrier File | `suspect_image.bmp` |
| Passphrase | `monarch` |
| Extracted File | `secret.txt` |

**Extracted Content:**
> "To the fools digging through my secrets... The real story is locked inside murder_plan.docx... Caesar cipher shift 3..."

### Caesar Cipher Decryption (Shift 3)

| Original Scrambled | Decrypted |
|-------------------|-----------|
| `murder_plan.docx` | Full murder plan outline |
| `Encrypted Letter.docx` | Cipher mapping table |

### PGP Key Analysis

| File | Type | Status |
|------|------|--------|
| `pgp_pubkey.bin` | Public Key | Valid |
| `pgp_seckey1.bin` | Secret Key | Encrypted |
| `pgp_seckey2.bin` | Secret Key | Encrypted |

### Zlib Decompression

| Input | Output | Method |
|-------|--------|--------|
| `zlib_data.bin` | `decompressed.bin` | Python zlib |
| `extracted_zlib.bin` | `decompressed_153.bin` | Offset 153 |

---

## 📝 Incident Reconstruction

### Decrypted Murder Plan Outline
Target: Ms. Clara Benson
Location: Grand Monarch Hotel, Room 718
Date & Time: May 20, 2025, 10:00 PM

Plan Details:

*Gain access to hotel room using master key card

*Disable security cameras prior to the event

*Use silenced pistol to avoid noise

*Leave no fingerprints or DNA evidence

*Escape through fire exit on east wing

*Additional Notes:

*Ensure all communication is encrypted

*No one outside the team knows the plan

*Security systems disabled at 9:45 PM sharp

### Accomplice Identification

**Finding:** Hotel security guard is the complicit party.

**Evidence Supporting:**
1. Only security personnel can disable cameras and alarms
2. Timing (9:45 PM) indicates shift knowledge
3. Whispered audio instruction implies direct coordination
4. Recovered `recovered_partner.jpg` matches hotel security uniform

---

## ⏱️ Timeline of Events

### May 20, 2025

| Time | Event | Evidence Source |
|------|-------|-----------------|
| 9:45 PM | Security systems disabled | Whispered audio + `settings.dat` |
| 9:50 PM | Langston enters Room 718 | Access logs (recovered) |
| 10:00 PM | Clara Benson shot | Murder plan + `confession.txt` |
| 10:05 PM | Langston escapes via east wing | Murder plan |
| 10:15 PM | Security systems re-enabled | System logs (`settings.dat`) |
| 10:30 PM | Body discovered | Case file |

### May 21, 2025

| Time | Event |
|------|-------|
| 09:00 AM | USB device recovered from Langston |
| 11:30 AM | Disk imaging completed |
| 02:00 PM | Forensic analysis began |

---

## 🔗 Chain of Custody

| Item # | Description | Received From | Date/Time | Transferred To | Purpose |
|--------|-------------|---------------|-----------|----------------|---------|
| 1 | USB disk (physical) | Crime scene | May 21, 2025 – 09:00 | Forensic Lab | Imaging |
| 2 | `Mrs_Clara_Benson_case_image.001` | Imaging process | May 21, 2025 – 11:30 | Investigator | Analysis |
| 3 | `suspect_image.wav` | Carving | May 22, 2025 – 10:00 | Audio Lab | Forensics |
| 4 | `clean.wav` | Filtered | May 22, 2025 – 14:00 | Analysis | OOK decode |
| 5 | Decrypted files | Python scripts | May 23-25, 2025 | Evidence locker | Preservation |
| 6 | Final report | Compiled | May 26, 2025 | Instructor | Submission |

---

## 🚀 How to Reproduce

### Prerequisites

```bash
# Kali Linux or Debian-based system
sudo apt update

# Clone Repository
git clone https://github.com/yourusername/DFIA299-Capstone-Forensic-Project.git
cd DFIA299-Capstone-Forensic-Project

#Install Dependencies
# System tools
sudo apt install -y sleuthkit sox libsox-fmt-all audacity minimodem multimon-ng steghide

# Python dependencies
pip install numpy scipy matplotlib scikit-image

#Run Audio Analysis
# Generate spectrogram
python spec.py

# Run OOK decoder
python decode_ook.py

# Inspect envelope
python inspect_cw.py

# Detect pulses
python pulse_detector.py

# Decrypt Caesar Cipher
# Python one-liner for shift 3
def caesar_decrypt(text, shift=3):
    result = ""
    for c in text:
        if c.isalpha():
            shifted = ord(c) - shift
            if c.isupper():
                result += chr((shifted - 65) % 26 + 65)
            else:
                result += chr((shifted - 97) % 26 + 97)
        else:
            result += c
    return result

# Extract Steganography
steghide extract -sf suspect_image.bmp -p monarch

# Decompress Zlib Data
import zlib
with open('zlib_data.bin', 'rb') as f:
    compressed = f.read()
decompressed = zlib.decompress(compressed)
with open('decompressed.bin', 'wb') as f:
    f.write(decompressed)


# 📄 Report
The complete forensic report is available as:
. 2025CFP7076__DFIA299 - Capstone Project_Digital_Forensics_Atul_Paswan.pdf

# Report Sections
✅ Executive Summary

✅ Investigation Methodology

✅ Tools and Techniques Used

✅ Evidence Recovered and Analysis

✅ Hidden Data Analysis

✅ Audio Forensics Results

✅ Decoding & Decryption Results

✅ Timeline of Events

✅ Chain of Custody Documentation

✅ Recommendations

✅ Conclusion

# 👤 Author
Detail	Information
Name	Atul Paswan
Student ID	2025CFP7076
Course	DFIA299 Capstone Project – Digital Forensics
Institution	ICDFA
Date	May 2025
Email	atulak968@gmail.com

# 🙏 Acknowledgments
NIST DFIR Challenge – For the adapted disk image

Sleuth Kit Developers – For forensic framework

Open Source Community – For Python libraries

Course Instructor – For project guidance

DFIA299 Capstone – For comprehensive learning

# ⭐ Show Your Support
If you found this forensic investigation useful, please consider:

⭐ Starring this repository

🍴 Forking for your own learning

🔄 Sharing with fellow forensic students

# 📧 Contact
For questions or collaboration:

GitHub Issues: Create an issue

Email: atulak968@gmail.com

# 
🔍 "In digital forensics, every byte tells a story." 🔍

This investigation was conducted as part of the DFIA299 Capstone Project – Digital Forensics. All findings are based on the evidence analyzed and follow standard forensic best practices.

  
