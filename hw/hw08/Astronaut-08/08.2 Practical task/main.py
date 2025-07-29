'''Validity of a password'''
import re

print('''
Hi! Password must have:
    - min 1 letter of a-z and min 1 letter of A-Z
    - min 1 number of 0-9
    - 1 of special character $#@
    - min length 6 and max length 16 char
      ''')
user_password = input('Write your password: ')

if re.findall('[a-z]', user_password) and re.findall('[A-Z]', user_password) \
and re.findall('[0-9]', user_password) and re.findall('[$#@]', user_password) \
and 6 <= len(user_password) <= 16 and ' ' not in user_password:
    print('It\'s VALID password!')
else:
    print('It\'s invalid password!')
