import re

password = input("Input password: \n")

if (re.search ( r"[a-z]", password)
    and re.search(r"[A-Z]", password)
    and re.search(r"[0-9]",password)
    and re.search(r"[$#@]", password)
    and re.search(r"^.{6,16}$", password)):
    print ("Valid")
else:
    print ("Invalid")
