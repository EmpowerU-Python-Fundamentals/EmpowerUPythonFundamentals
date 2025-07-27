# password_validator.py
"""
Simple password validator (SoftServe Task 2).
"""

import re

# Прекомпільовані патерни → працює швидше
_LOWER   = re.compile(r"[a-z]")
_UPPER   = re.compile(r"[A-Z]")
_DIGIT   = re.compile(r"\d")
_SPECIAL = re.compile(r"[#$@]")

MIN_LEN = 6
MAX_LEN = 16

def validate_password(pwd: str) -> bool:
    """Return True if *pwd* satisfies all rules."""
    if not (MIN_LEN <= len(pwd) <= MAX_LEN):
        return False
    if not _LOWER.search(pwd):
        return False
    if not _UPPER.search(pwd):
        return False
    if not _DIGIT.search(pwd):
        return False
    if not _SPECIAL.search(pwd):
        return False
    return True

