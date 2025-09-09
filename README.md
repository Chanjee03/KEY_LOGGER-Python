# KEY_LOGGER-Python
# 🖥️ Python Keylogger (Educational Cybersecurity Project)

> **Disclaimer**  
> This project is for **educational and cybersecurity research purposes only**.  
> **Do not** deploy it on any system without **explicit written permission**.  
> Unauthorized use may violate privacy laws, computer misuse acts, or other regulations.

---

## 📌 Overview

This is a modular, Python-based **keylogging and system activity monitoring** tool designed to help cybersecurity learners and professionals understand how keylogging, data exfiltration, and stealth mechanisms work.  

By analyzing how attackers build such tools, defenders can develop **better detection and prevention** strategies.

---

## ✨ Features

### 🖱️ Activity Monitoring (Monitor Module)
- **Keystroke Logging (`monitor/keylogger.py`)**  
  Captures all keystrokes with timestamps for forensic correlation.

- **Clipboard Monitoring (`monitor/clipboard.py`)**  
  Periodically reads clipboard content (text) for analysis.

- **Screenshot Capture (`monitor/screenshot.py`)**  
  Takes periodic screenshots, correlating user input with visual context.

- **Window Tracking (`monitor/window.py`)**  
  Logs currently active window titles to link keystrokes to specific applications or websites.

---

### 📤 Data Exfiltration (Exfil Module)
- **Dropbox Upload (`exfil/dropbox_upload.py`)**  
  Sends captured logs, screenshots, or clipboard data to a Dropbox account using an API token (stored in `.env`).

- **Email Upload (`exfil/email_check.py`)**  
  Emails collected data to a specified email account at configurable intervals.

---

### 🛠️ Core Utilities
- **Stealth Mode (`stealth.py`)**  
  Hides the program window and minimizes visibility on the system.

- **Self-Destruct (`self_destruct.py`)**  
  Securely deletes the program and its traces after a trigger condition is met.

- **Centralized Configuration (`config.py`)**  
  Stores file paths, timing intervals, API keys, and other settings.

- **Logging Setup (`logger_setup.py`)**  
  Manages log formatting and storage (debug, info, or silent mode).

- **Main Controller (`main.py`)**  
  Orchestrates all modules (monitoring, exfiltration, stealth, self-destruction) into a single workflow.

---

## 📦 Build & Packaging
- The project can be converted into an executable using [PyInstaller](https://www.pyinstaller.org/).  
- The provided `main.spec` is a configuration file for creating a standalone binary (`.exe`).



🧩 Project Structure
KEY_LOGGER/
│
├── build/                     # Build artifacts (auto-generated)
├── dist/                      # Distribution files (auto-generated)
│
├── exfil/                     # Data exfiltration modules
│   ├── __init__.py
│   ├── dropbox_upload.py
│   └── email_check.py
│
├── monitor/                   # Monitoring modules
│   ├── __init__.py
│   ├── clipboard.py
│   ├── keylogger.py
│   ├── screenshot.py
│   └── window.py
│
├── .env                       # Environment variables (tokens, credentials)
├── config.py                  # Central configuration
├── logger_setup.py            # Logger utility
├── main.py                    # Main controller script
├── main.spec                  # PyInstaller build specification
├── self_destruct.py           # Secure self-deletion logic
└── stealth.py                 # Stealth mode functions
