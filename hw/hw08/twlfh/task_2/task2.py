import re
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
instructions = ('Your password must be:\n'
                '\t- 6 to 16 characters long\n'
                '\t- must contain at least 1 uppercase letter from A-Z\n'
                '\t- 1 lowercase letter from a-z and at least 1 special character #@$')

def validator():
    print(instructions)
    while True:
        password = input('Enter your password: ')
        if re.fullmatch(pattern,password):
            print('Your password is strong!')
            break
        else:
            print('Your password is not strong!\n'
                  'Please try again.\n')
            print(f'{instructions}\n')


validator()

