"""08.2 Practical tasks. 'Check password validity' """

import re

password_is_valid = True
passwords_reasons = []
pswd = input("Enter the password: ")
# pswd = 'aaaaaaaaa1aaA'

# check password for length
if not re.match(r'^.{6,16}$', pswd):
    password_is_valid = False
    passwords_reasons.append("Password length should be between 6 and 16.")

# check password for lowercase letters
if not re.search(r'[a-z]', pswd):
    password_is_valid = False
    passwords_reasons.append("Password should countain at least one lowercase letter")

# check password for uppercase letters
if not re.search(r'[A-Z]', pswd):
    password_is_valid = False
    passwords_reasons.append("Password should countain at least one uppercase letter")

# check password for digits
if not re.search(r'\d', pswd):
    password_is_valid = False
    passwords_reasons.append("Password should countain at least one digit")

# check password for special characters
if not re.search(r'[\$|#|@]', pswd):
    password_is_valid = False
    passwords_reasons.append("Password should countain one of special character: $ # @")

if not password_is_valid:
    print("Password is invalid: ")
    for str in passwords_reasons:
        print(str)
else:
    print("Password is valid")
