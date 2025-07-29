from core import validate_password
if __name__ == "__main__":
    pwd = input("Enter password to validate: ")
    print("Valid password ✅" if validate_password(pwd) else "Invalid password ❌")
