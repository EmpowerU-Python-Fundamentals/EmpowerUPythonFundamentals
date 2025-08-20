import re

password = input('Enter some made-up password: ')

validation = {'At least 1 letter between [a-z] and 1 letter between [A-Z].':
                lambda s: re.search('[a-z]', s) and re.search('[A-Z]', s),
              'At least 1 number between [0-9].':
                lambda s: re.search(r'\d', s),
              'At least 1 character from [$#@].':
                lambda s: re.search(r'[$#@]', s),
              'Minimum length 6 characters.':
                lambda s: len(s) >= 6,
              'Maximum length 16 characters.':
                lambda s: len(s) <= 16}

for req in validation:
    if not validation[req](password):
        print('Your password does not meet the following requirement:')
        print(req)
        break
else:
    print('Your password is valid!')
