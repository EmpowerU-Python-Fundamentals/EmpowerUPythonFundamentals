import re

def class_name_changer(cls, new_name):
    if re.fullmatch(r'[A-Z][A-Za-z0-9]*', new_name):
        cls.__name__ = new_name
    else:
        raise Exception("Invalid class name")