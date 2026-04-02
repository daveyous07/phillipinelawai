"""
Quick check: Python version must be 3.10, 3.11, or 3.12.
Run: py setup-check.py
"""
import sys
v = sys.version_info
if v.major != 3 or v.minor > 12:
    print(f"ERROR: Python {v.major}.{v.minor} detected.")
    print("This project needs Python 3.10, 3.11, or 3.12.")
    print("Download Python 3.12 from: https://www.python.org/downloads/release/python-3120/")
    sys.exit(1)
print(f"OK: Python {v.major}.{v.minor}")
