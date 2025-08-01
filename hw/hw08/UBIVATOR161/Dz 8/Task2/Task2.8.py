import re

def c_p(p):
    if len(p) < 6:
        return "Password must contain at least 6 letters"
    elif len(p) > 16:
        return "Maximum count of symbols for password is 16"
    if not re.search(r'\d',p):
        return "Password must contain at least one number"
    if not re.search(r'[A-Z]',p):
        return "Password must contain at least one caps letter"
    if not re.search(r'[a-z]',p):
        return "Password must contain at least one letter"
    if not re.search(r'[!@#$%^&*]',p):
        return "Password must contain at least one spec.symbol"
    return None
while True:
    password = input("Enter password: ")
    e = c_p(password)
    if e:
        print('Error', e)
    else:
        print("Good password")
        break
