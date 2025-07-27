
---

# 🐍 Python Virtual Environment (venv) Setup Guide

This guide provides **step-by-step instructions** to set up and use Python **virtual environments (`venv`)** on both **Windows** and **Linux** using **VS Code**.

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

* **Python 3.x** installed (already available in your system)
* **VS Code** installed with **Python extension**
* **Git** (optional, for pushing this repo)
* Internet connection for installing packages

---

## 🪟 Setting Up `venv` on Windows

> Full HTML guide: [`windows/index.html`](windows/index.html)

### ✅ Steps:

1. **Install `venv` (if not installed)**
   Run in **Command Prompt**:

   ```bash
   pip install virtualenv
   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv test
   ```

3. **Activate venv**

   * **Command Prompt**:

     ```bash
     test\Scripts\activate
     ```
   * **PowerShell** (if needed): # Ignore for cmd 

     ```powershell 
     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
     .\test\Scripts\Activate.ps1
     ```

4. **Install Required Modules**
   Paste this in **CMD** after activating venv:

   ```bash
   pip install pandas matplotlib scikit-learn
   ```

5. **Deactivate venv**

   ```bash
   deactivate
   ```

---

## 🐧 Setting Up `venv` on Linux

> Full HTML guide: [`linux/index.html`](linux/index.html)

### ✅ Steps:

1. **Install `venv` (if not installed)**

   ```bash
   sudo apt update
   sudo apt install python3-venv python3-pip
   ```

2. **Create Virtual Environment**

   ```bash
   python3 -m venv test
   ```

3. **Activate venv**

   ```bash
   source test/bin/activate
   ```

4. **Install Required Modules**
   Paste this in **Terminal** after activating venv:

   ```bash
   pip install pandas matplotlib scikit-learn
   ```

5. **Deactivate venv**

   ```bash
   deactivate
   ```

---



