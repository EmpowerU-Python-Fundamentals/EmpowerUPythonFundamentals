import re

def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#]).{6,16}$')
    if pattern.match(password): 
        return True 
    else: 
        return False

# Main program
password = input("Enter your password: ")

if is_valid_password(password):
    print("Your password is accepted")
else:
    print("Your password didn't match the description")