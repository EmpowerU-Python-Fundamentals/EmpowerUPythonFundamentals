"""task2"""
import re
password = input()
if (6 <= len(password) <= 16 and
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"\d", password) and
    re.search(r"[$#@]", password)):
    print("Valid password")
else:
    print("Invalid password")
