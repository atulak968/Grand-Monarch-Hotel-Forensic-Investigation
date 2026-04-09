# 🔍 DFIA299 Capstone Project – Grand Monarch Hotel Forensic Investigation

## Case: Death of Clara Benson (Room 718, May 20, 2025)

| Badge | Status |
|-------|--------|
| ![Status](https://img.shields.io/badge/Status-Completed-success) | Investigation Complete |
| ![Forensics](https://img.shields.io/badge/Digital_Forensics-Success-blue) | All Evidence Recovered |
| ![Tools](https://img.shields.io/badge/Tools-SleuthKit%20%7C%20Sox%20%7C%20Python-orange) | Multiple Tools Used |
| ![Course](https://img.shields.io/badge/Course-DFIA299_Capstone-red) | Final Project |
| ![Student](https://img.shields.io/badge/Student-2025CFP7076_Atul_Paswan-green) | Author |

---

## 📌 Table of Contents

1. [Case Overview](#case-overview)
2. [Key Findings](#key-findings)
3. [Investigation Methodology](#investigation-methodology)
4. [Tools Used](#tools-used)
5. [Complete File Structure](#complete-file-structure)
6. [Evidence Analysis](#evidence-analysis)
7. [Audio Forensics Details](#audio-forensics-details)
8. [Decoding & Decryption](#decoding--decryption)
9. [Incident Reconstruction](#incident-reconstruction)
10. [Timeline of Events](#timeline-of-events)
11. [Chain of Custody](#chain-of-custody)
12. [How to Reproduce](#how-to-reproduce)
13. [Report](#report)
14. [Author](#author)
15. [License](#license)

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
| 2 | Hidden Morse message | `"THE TRUTH IS IN ROOM 718"` |
| 3 | PGP Public Key recovered | `pgp_pubkey.bin`, `pgp_seckey1.bin` |
| 4 | Encrypted archive found | `pex_archive.pgp`, `pex_archive.zip` |
| 5 | Steganography extracted | `secret.txt`, `recovered_partner.jpg` |
| 6 | OOK decoded binaries | `decoded_600_800_*.bin` |
| 7 | Zlib compressed data extracted | `zlib_data.bin`, `decompressed.bin` |
| 8 | Hidden audio recovered | `hidden_audio.wav` |
| 9 | PCAP file recovered | `pex_test.pcap` |
| 10 | Accomplice identified | Hotel Security Guard |

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
└─────────────────────────────────────────────────────────────────┘

text

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
| **Python Libraries** | NumPy, SciPy, Matplotlib |
| **Compression** | `gunzip`, `unzip`, `zlib` |
| **Analysis & Visualization** | `xxd`, `strings`, `binwalk` |

---

## 📁 Complete File Structure
DFIA299 - Capstone Project_Digital_Forensics_2025CFP7076_Atul_Paswan/
│
├── 📄 2025CFP7076__DFIA299 - Capstone Project_Digital_Forensics_Atul_Paswan.pdf
│
├── 🖼️ Evidence Images & Audio
│ ├── suspect_image.wav # Original audio evidence
│ ├── suspect_image.bmp # Original image evidence
│ ├── clean.wav # Filtered audio (600-800 Hz)
│ ├── hidden_audio.wav # Extracted hidden audio
│ └── bw.png # Processed image
│
├── 🎵 Audio Spectrograms
│ ├── morse_spectrogram.png # Morse code visualization
│ ├── full_spec.png # Full spectrogram
│ └── envelope_check.png # Envelope detection
│
├── 🔓 Decoded Outputs
│ ├── decoded_600_800_revFalse_scale0.9.bin
│ ├── decoded_600_800_revFalse_scale1.0.bin
│ ├── decoded_1100_1300_revFalse_scale0.9.bin
│ └── decoded_data_1200Hz.bin
│
├── 🔐 PGP & Encryption Analysis
│ ├── pgp_pubkey.bin # PGP Public Key
│ ├── pgp_seckey1.bin # PGP Secret Key
│ ├── pex_archive.pgp # PGP encrypted archive
│ └── pex_archive.zip # ZIP archive
│
├── 📜 Recovered Evidence
│ ├── confession.txt # Base64 decoded confession
│ ├── secret.txt # Steganography extracted
│ ├── recovered_partner.jpg # Accomplice image
│ └── recovered_files/ # All carved files
│
├── 🐍 Python Analysis Scripts
│ ├── decode_ook.py # OOK demodulation
│ ├── pulse_detector.py # Burst detection
│ ├── spec.py # Spectrogram generator
│ └── view_spec.py # Spectrogram viewer
│
├── 📊 Analysis Outputs
│ ├── timeline.csv # Timeline of events
│ └── bodyfile.txt # Sleuth Kit bodyfile
│
├── 📸 Screenshots/
│ └── [All forensic procedure screenshots]
│
└── 💾 Disk Image
├── Mrs_Clara_Benson_case_image.001.txt
└── Mrs_Clara_Benson_case_image.001

text

---

## 📊 Evidence Analysis

### 1. Disk Image Verification

| Hash Type | Value | Status |
|-----------|-------|--------|
| **MD5** | `583bb23631d54dfe5446f1f094681f30` | ✅ Verified |
| **SHA1** | `467176bdfeffef80f8fde152a187575735023dbea` | ✅ Verified |

### 2. Partition Layout (from `mmls`)

| Slot | Start | End | Length | Description |
|------|-------|-----|--------|-------------|
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
| `pgp_pubkey.bin` | Recovered | PGP analysis |
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
├──► morse_spectrogram.png
│
▼
Envelope Detection (Python)
│
▼
OOK Demodulation
│
├──► Bit period: 13-15 ms
├──► Scale: 0.9, 1.0, 1.1
└──► Bit order: normal & reversed
│
▼
Morse Message Extracted

text

### Extracted Morse Message
THE TRUTH IS IN ROOM 718

text

### Spectrogram Analysis Results

| Observation | Interpretation |
|-------------|----------------|
| Vertical lines below 500 Hz | OOK bursts (on-off keying) |
| Burst duration ~5 ms | High-speed data (200 baud) |
| Carriers at 630 Hz, 720 Hz, 1200 Hz | Multiple frequency components |

---

## 🔓 Decoding & Decryption

### Base64 Decoded Confession

**Original:**
U29ycnsIEkgY291bGQgbm90IG1ha2UgdxAgbXkgbWluZcWgYnV0IGhlcmUgaXmgdGhIGFjdHvHbCBjb25mZXnzaW9uOiAKTWlIdCBtZSbhdCB0aGUgY2FzYSwgSSdtIHJ1WRSLg==

text

**Decoded:**
Sorry, I could not make up my mind but here is the confession:
Meet me at the case, I'm Ready...

text

### Steganography Extraction

| Parameter | Value |
|-----------|-------|
| Carrier File | `suspect_image.bmp` |
| Passphrase | `monarch` |
| Extracted File | `secret.txt` |

**Extracted Content:**
> "To the fools digging through my secrets... The real story is locked inside murder_plan.docx... Caesar cipher shift 3..."

### Caesar Cipher Decryption (Shift 3)

| Original | Decrypted |
|----------|-----------|
| `murder_plan.docx` | Full murder plan outline |
| `Encrypted Letter.docx` | Cipher mapping table |

### PGP Key Analysis

| File | Type | Status |
|------|------|--------|
| `pgp_pubkey.bin` | Public Key | Valid |
| `pgp_seckey1.bin` | Secret Key | Encrypted |

---

## 📝 Incident Reconstruction

### Decrypted Murder Plan Outline
Target: Ms. Clara Benson
Location: Grand Monarch Hotel, Room 718
Date & Time: May 20, 2025, 10:00 PM

Plan Details:

Gain access using master key card

Disable security cameras prior to event

Use silenced pistol to avoid noise

Leave no fingerprints or DNA evidence

Escape through fire exit on east wing

Additional Notes:

Security systems disabled at 9:45 PM sharp

No one outside the team knows the plan

text

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
| 9:45 PM | Security systems disabled | Whispered audio |
| 9:50 PM | Langston enters Room 718 | Access logs |
| 10:00 PM | Clara Benson shot | Murder plan |
| 10:05 PM | Langston escapes | Murder plan |
| 10:30 PM | Body discovered | Case file |

### May 21, 2025

| Time | Event |
|------|-------|
| 09:00 AM | USB device recovered |
| 11:30 AM | Disk imaging completed |
| 02:00 PM | Forensic analysis began |

---

## 🔗 Chain of Custody

| Item | Description | From | To | Purpose |
|------|-------------|------|-----|---------|
| 1 | USB disk (physical) | Crime scene | Forensic Lab | Imaging |
| 2 | Disk image | Imaging process | Investigator | Analysis |
| 3 | Audio files | Carving | Audio Lab | Forensics |
| 4 | Decrypted files | Python scripts | Evidence locker | Preservation |
| 5 | Final report | Compiled | Instructor | Submission |

---

## 🚀 How to Reproduce

### Prerequisites

```bash
sudo apt update
Clone Repository
bash
git clone https://github.com/atulak968/Grand-Monarch-Hotel-Forensic-Investigation.git
cd Grand-Monarch-Hotel-Forensic-Investigation
Install Dependencies
bash
# System tools
sudo apt install -y sleuthkit sox audacity steghide

# Python dependencies
pip install numpy scipy matplotlib
Run Audio Analysis
bash
python spec.py
python decode_ook.py
python pulse_detector.py
Extract Steganography
bash
steghide extract -sf suspect_image.bmp -p monarch
Caesar Cipher Decryption (Python)
python
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
Decompress Zlib Data
python
import zlib
with open('zlib_data.bin', 'rb') as f:
    compressed = f.read()
decompressed = zlib.decompress(compressed)
with open('decompressed.bin', 'wb') as f:
    f.write(decompressed)
📄 Report
The complete forensic report is available as:

text
2025CFP7076__DFIA299 - Capstone Project_Digital_Forensics_Atul_Paswan.pdf
Report Sections
✅ Executive Summary

✅ Investigation Methodology

✅ Tools and Techniques Used

✅ Evidence Recovered and Analysis

✅ Hidden Data Analysis

✅ Audio Forensics Results

✅ Decoding & Decryption Results

✅ Timeline of Events

✅ Chain of Custody

✅ Recommendations

✅ Conclusion

👤 Author
Detail	Information
Name	Atul Paswan
Student ID	2025CFP7076
Course	DFIA299 Capstone – Digital Forensics
Institution	ICDFA
Date	May 2025
Email	atulak968@gmail.com
GitHub	atulak968
🙏 Acknowledgments
NIST DFIR Challenge – For the adapted disk image

Sleuth Kit Developers – For forensic framework

Open Source Community – For Python libraries

Course Instructor – For project guidance

⭐ Show Your Support
⭐ Star this repository

🍴 Fork for your own learning

🔄 Share with fellow students

📧 Contact
GitHub Issues: Create an issue

Email: atulak968@gmail.com

📜 License
MIT License

🔍 Quote
"In digital forensics, every byte tells a story."

This investigation was conducted as part of the DFIA299 Capstone Project – Digital Forensics. All findings follow standard forensic best practices.
