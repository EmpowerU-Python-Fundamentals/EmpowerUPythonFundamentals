password = input()

if len(password) < 6 or len(password) > 16:
    print("Invalid password")
elif not any(c.islower() for c in password):
    print("Invalid password")
elif not any(c.isupper() for c in password):
    print("Invalid password")
elif not any(c.isdigit() for c in password):
    print("Invalid password")
elif not any(c in "$#@" for c in password):
    print("Invalid password")
else:
    print("Valid password")