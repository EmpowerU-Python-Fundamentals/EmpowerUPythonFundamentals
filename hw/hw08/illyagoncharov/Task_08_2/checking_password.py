import re
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'
password = input("write the password for check: ")
if len(password.split(" ")) ==1:
    if re.match(pattern, password) is None:
        print("Password is not valid")
    else: print("Password is valid")
else: print("You must write 1 word without space")