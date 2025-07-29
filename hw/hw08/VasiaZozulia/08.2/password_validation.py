import re

def passwd_valid(password):
    print("The password is ok!") if (6 <= len(password) <= 16 and re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"[0-9]", password) and re.search(r"[$#@]", password)) else print ("The password is not ok")

password = input("Enter your password: ")
passwd_valid(password)

