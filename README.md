# 🔍 DFIA299 Capstone Project – Grand Monarch Hotel Forensic Investigation

## 📌 Case: Death of Clara Benson (Room 718, May 20, 2025)

![Status](https://img.shields.io/badge/Status-Completed-success)
![Forensics](https://img.shields.io/badge/Digital_Forensics-Success-blue)
![Tools](https://img.shields.io/badge/Tools-SleuthKit%20%7C%20Sox%20%7C%20Python-orange)
![Course](https://img.shields.io/badge/Course-DFIA299_Capstone-red)
![Student](https://img.shields.io/badge/Student-Atul_Paswan-green)

---

## 📑 Table of Contents

- [Case Overview](#-case-overview)
- [Key Findings](#-key-findings)
- [Methodology](#-methodology)
- [Tools Used](#-tools-used)
- [Evidence Analysis](#-evidence-analysis)
- [Audio Forensics](#-audio-forensics)
- [Decoding & Decryption](#-decoding--decryption)
- [Incident Reconstruction](#-incident-reconstruction)
- [Timeline](#-timeline)
- [Chain of Custody](#-chain-of-custody)
- [Reproduction Steps](#-reproduction-steps)
- [Report](#-report)
- [Author](#-author)

---

## 📋 Case Overview

| Detail | Information |
|--------|------------|
| Incident | Death of Clara Benson |
| Location | Room 718, Grand Monarch Hotel |
| Date | May 20, 2025 |
| Time | ~10:00 PM |
| Suspect | Marcus Langston |
| Evidence | USB Disk Image |
| Investigator | Atul Paswan |

---

## 🔑 Key Findings

- ✔ Confession recovered (Base64 decoded)
- ✔ Hidden Morse message found
- ✔ Steganography data extracted
- ✔ PGP keys recovered
- ✔ Encrypted archive analyzed
- ✔ Hidden audio evidence extracted
- ✔ Accomplice identified

---

## 🔬 Methodology

```
1. Image Verification
2. Disk Analysis
3. File Carving
4. Data Recovery
5. Audio Forensics
6. Steganography
7. Decryption
8. PGP Analysis
9. Decompression
10. Timeline Creation
```

---

## 🛠️ Tools Used

| Category | Tools |
|----------|------|
| Disk Analysis | Sleuth Kit |
| Audio | Sox, Audacity |
| Stego | Steghide, Zsteg |
| Network | Wireshark |
| Programming | Python |
| Others | Binwalk, Strings |

---

## 📊 Evidence Analysis

### Disk Verification

| Hash | Status |
|------|--------|
| MD5 | ✅ Verified |
| SHA1 | ✅ Verified |

### Recovered Files

- `murder_plan.docx`
- `secret.txt`
- `confession.txt`
- `pgp_pubkey.bin`
- `recovered_partner.jpg`

---

## 🎧 Audio Forensics

- Bandpass filtering (600–800 Hz)
- Spectrogram analysis
- OOK demodulation

### 🔐 Hidden Message:
```
THE TRUTH IS IN ROOM 718
```

---

## 🔓 Decoding & Decryption

### Base64 Confession
> “Sorry, I could not make up my mind… here is the confession…”

### Steganography
- File: `suspect_image.bmp`
- Password: `monarch`

### Caesar Cipher
- Shift: 3
- Result: Murder plan recovered

---

## 🧠 Incident Reconstruction

- Entry via master key
- Cameras disabled (9:45 PM)
- Victim shot at 10:00 PM
- Escape via east wing
- Evidence cleaned

### 👥 Accomplice:
➡️ Hotel Security Guard

---

## ⏱️ Timeline

| Time | Event |
|------|------|
| 9:45 PM | Cameras disabled |
| 9:50 PM | Entry |
| 10:00 PM | Murder |
| 10:05 PM | Escape |
| 10:30 PM | Body found |

---

## 🔗 Chain of Custody

| Item | From | To | Purpose |
|------|------|----|--------|
| USB | Crime Scene | Lab | Imaging |
| Image | Lab | Investigator | Analysis |
| Files | Scripts | Storage | Evidence |

---

## 🚀 Reproduction Steps

```bash
# Clone repo
git clone https://github.com/yourusername/repo.git
cd repo

# Install tools
sudo apt install sleuthkit sox steghide

# Python libs
pip install numpy scipy matplotlib
```

---

## 📄 Report

📥 Full Report available inside repository:

- Executive Summary
- Methodology
- Evidence Analysis
- Audio Forensics
- Timeline
- Conclusion

---

## 👤 Author

- **Atul Paswan**
- DFIA299 Capstone Project
- Digital Forensics Student

📧 Email: atulak968@gmail.com

---

## ⭐ Support

If you found this useful:

- ⭐ Star the repo  
- 🍴 Fork it  
- 🔄 Share with others  

---

## 💬 Quote

> "In digital forensics, every byte tells a story."
