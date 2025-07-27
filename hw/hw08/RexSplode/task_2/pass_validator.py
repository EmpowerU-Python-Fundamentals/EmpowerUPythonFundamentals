import re as regex

user_input = input("Please enter a password. 6-16 symbols,\
                    lowercase and uppercase symbols, at least one symbol like #,@,$")

# from 6 to 16 symbols
# at least 1 lowercase letter a-z
# at least 1 uppercase letter A-Z
# at least 1 special symbol #, @, or $
pattern = regex.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#]).{6,16}$')
if pattern.match(user_input):
    print("Your password is accepted")
else:
    print("Your password didn't match the description")
