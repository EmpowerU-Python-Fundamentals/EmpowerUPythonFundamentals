import re

__requirements__ = [
    re.compile(r"[a-z]+"),
    re.compile(r"[A-Z]+"),
    re.compile(r"\d+"),
    re.compile(r"[$#@]+"),
    re.compile(r"^.{6,16}$")
]

def validate_password(password: str) -> bool:
    for requirement in __requirements__:
        found = requirement.search(password)
        if not found:
            return False
    return True


if __name__ == "__main__":
    # Define color codes
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"  # Resets color to default

    tests = [
        (r"1qaz", False),
        (r"123456789", False),
        (r"QWERTYUIOP", False),
        (r"qwertyuiop", False),
        (r"QwERTYUIOP", False),
        (r"QwERTY$#@UIOP", False),
        (r"!№;%:#?*()", False),
        (r"$1#Qq", False),
        (r"$@#123456QWERqwer", False),
        (r"$@#12345QWERqwer", True),
        (r"qWertyu4$", True)
    ]

    for test in tests:
        is_valid = validate_password(test[0])
        passed = f"{f"{GREEN}Pass{RESET}" if is_valid == test[1] else f"{RED}Fail{RESET}"}"
        print(f"{passed} -- validate_password(\"{test[0]}\") = {is_valid}")