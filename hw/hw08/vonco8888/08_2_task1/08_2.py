import re

password = input("Enter your password: ")

# Умова перевірки довжини
if 6 <= len(password) <= 16:
    # Перевірка за допомогою регулярних виразів
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[$#@]", password)

    if has_lower and has_upper and has_digit and has_special:
        print("Valid password ✅")
    else:
        print("Invalid password ❌")
else:
    print("Password must be between 6 and 16 characters long ❌")