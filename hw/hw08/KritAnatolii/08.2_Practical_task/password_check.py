import re

def password_check():
    """Program to check the validity of a password"""
    
    print("Enter your password:")
 
    password = input().strip()
    
    alph = re.findall("[a-z]", password)
    ALPH = re.findall("[A-Z]", password)
    dig = re.findall("\d", password)
    spec = re.findall("[$#@]", password)
    
    if not alph:
        return "At least 1 lowercase letter [a-z]"
    elif not ALPH:
        return "At least 1 uppercase letter [A-Z]"
    elif not dig:
        return "At least 1 digit [0-9]"
    elif not spec:
        return "At least 1 special character from [$#@]"
    elif len(password) < 6 or len(password) > 16:
        return "Minimum length 6 characters, maximum length 16 characters"
    else:
        return "Your password is valid"


def main():
     while True:
         result = password_check()
         print (result)
         if result == "Your password is valid":
            break
         print("Please try again.\n")




if __name__ == "__main__":
    main ()
