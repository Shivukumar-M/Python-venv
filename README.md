# 🐍 Python Virtual Environment (venv) Setup Guide

This guide provides step-by-step instructions to set up and use Python virtual environments (`venv`) on both **Windows** and **Linux** using **VS Code**.

---

## 📁 Folder Structure

```
project/
├── image/               # Screenshots for visual reference
│   ├── images1.jpg
│   ├── images2.png
│   ├── images3.png
│   └── ...
├── windows/             # HTML guide for Windows
│   └── index.html
├── linux/               # HTML guide for Linux
│   └── index.html
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x installed
- VS Code installed with Python extension
- Git (for pushing this repo if needed)

---

## 🪟 Setting Up `venv` on Windows

> See: [`windows/index.html`](windows/index.html)

### Steps:
1. Install Python and ensure "Add Python to PATH" is checked.
2. Create a venv:
   ```bash
   python -m venv test
   ```
3. Activate venv:
   - In Command Prompt:
     ```
     test\Scripts\activate
     ```
   - In PowerShell (if needed):
     ```
     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
     .\test\Scripts\Activate.ps1
     ```
4. Install packages:
   ```
   pip install requests
   ```
5. Deactivate:
   ```
   deactivate
   ```

---

## 🐧 Setting Up `venv` on Linux

> See: [`linux/index.html`](linux/index.html)

### Steps:
1. Install Python and venv:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```
2. Create a venv:
   ```bash
   python3 -m venv test
   ```
3. Activate venv:
   ```bash
   source test/bin/activate
   ```
4. Install packages:
   ```bash
   pip install requests
   ```
5. Deactivate:
   ```bash
   deactivate
   ```

---
