import re

def class_name_changer(cls, new_name):
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError("Invalid class name")
        
    cls.__name__ = new_name