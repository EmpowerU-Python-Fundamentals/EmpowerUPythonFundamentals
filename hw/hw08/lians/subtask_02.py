import re


def main():
    p = input("Provide a password to validate it: ").strip()
    if not p:
        exit("Cannot be empty")
    val, msg = validity(p)
    if not val:
        print(msg)
    else:
        print("Provided password is valid.")


def validity(p):
    val = False
    text = "Provided password is not valid.\n Should have:\n"
    msg = text

    if not re.search(r"[a-z]", p):
        msg += "\t- at least one lowercase letter\n"
    if not re.search(r"[A-Z]", p):
        msg += "\t- at least one uppercase letter\n"
    if not re.search(r"[0-9]", p):
        msg += "\t- at least one number in [0 - 9]\n"
    if not re.search(r"[$#@]", p):
        msg += "\t- at least one char from [$, #, @]\n"
    if not re.match(r"^.{6,}", p):
        msg += f"\t- at least 6 characters\n"
    if not re.match(r"^.{6,16}$", p):
        msg += f"\t- up to 16 characters"        
    if msg == text:
        val = True
    return val, msg


if __name__ == "__main__":
    main()