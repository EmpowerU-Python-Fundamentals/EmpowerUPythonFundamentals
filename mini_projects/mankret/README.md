# Mini Console htop (Python)

A lightweight **console-based system monitoring tool** inspired by `htop (resource manager for Linux)`.  
It works on **Linux, macOS, and Windows** using Python and the `psutil, rich` libraries.  

---

## Features

✅ Real-time CPU usage (per core)  
✅ Memory and swap usage  
✅ Disk usage  
✅ Top 5 processes by CPU usage  
✅ Works across platforms (Linux, macOS, Windows)  
✅ Runs directly in the terminal  

---

## Demo

Example dashboard (Linux/macOS):
==================================================
   MINI HTOP DASHBOARD
==================================================

  _CPU Info_    

| Cores | Frequency (MHz) | Usage (%) |
|:------|:----------------|:----------|
| 8     | 3228.00         | 10.9      |


 _Memory_

| Total   | Used   | Available | Usage(%) |
|:--------|:-------|:----------|:---------|
| 16.00GB | 8.31GB | 6.89GB    | 56.9     |

 _Top Processes (by CPU %)_:

| PID  | NAME         | CPU % |
|:-----|:-------------|:------|
| 8571 | pycharm      | 31.9  |
| 8499 | plugin       | 7.6   |
| 8515 | UTM          | 5.3   |
| 8526 | QEMULauncher | 5.3   |
| 8490 | firefox      | 2.9   |

---

## Install dependencies

### 1. Make sure you are in the correct directory
Check that you are inside the project folder where `requirements_htop.txt` is located.

**Linux / macOS:**

```bash
pwd
ls
```
**Windows (PowerShell / CMD):**

```bash
cd
dir
```

## Create and activate a virtual environment

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```bash
python -m venv venv
venv\Scripts\activate
```

## Install dependencies

```bash
pip install psutil rich
```
or

```bash
pip install -r requirements_htop.txt
```


## Usage

```bash
python mini_htop.py
```
or 
```bash
python3 mini_htop.py
```


✨ Created by Mankret ✨

License

MIT License © 2025
Feel free to use, modify, and share 🚀
