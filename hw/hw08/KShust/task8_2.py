import re

def main():
    p = input("Enter a password to validate: ").strip()
    if not p:
        exit("Password cannot be empty.")
    is_valid, message = validate_password(p)
    if is_valid:
        print("Password is valid.")
    else:
        print(message)

def validate_password(password):
    is_valid = False
    core_msg = "Password is not valid.\nIt must contain:\n"
    message = core_msg

    if not re.search(r"[a-z]", password):
        message += "\t- at least one lowercase letter [a-z]\n"
    if not re.search(r"[A-Z]", password):
        message += "\t- at least one uppercase letter [A-Z]\n"
    if not re.search(r"[0-9]", password):
        message += "\t- at least one digit [0-9]\n"
    if not re.search(r"[$#@]", password):
        message += "\t- at least one special character from [$, #, @]\n"
    if len(password) < 6:
        message += "\t- a minimum length of 6 characters\n"
    if len(password) > 16:
        message += "\t- a maximum length of 16 characters\n"

    if message == core_msg:
        is_valid = True

    return is_valid, message

if __name__ == "__main__":
    main()

