import re

def validate_password(password):
     if not password:
         return False

     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
     return bool(re.search(pattern, password))


