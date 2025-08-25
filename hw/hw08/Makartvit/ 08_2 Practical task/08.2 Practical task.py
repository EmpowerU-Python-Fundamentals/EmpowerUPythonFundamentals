def check(psw):
    if len(psw) < 6 or len(psw) > 16:
        return False

    lower = upper = digit = special = False
    for i in psw:
        if 'a' <= i <= 'z':
            lower = True
        elif 'A' <= i <= 'Z':
            upper = True
        elif '0' <= i <= '9':
            digit = True
        elif i in "$#@":
            special = True
    return lower and upper and digit and special


if __name__ == "__main__":
    while True:
        pwd = input("Enter password: ")
        if check(pwd):
            print("Password is valid")
            break
        else:
            print("Invalid password, try again.\n")