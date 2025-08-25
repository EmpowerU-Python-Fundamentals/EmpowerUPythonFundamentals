import re

def class_name_changer(cls, new_name):
    if not isinstance(new_name, str):
        raise ValueError("Class name must be a string.")
    
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name
    return cls

# Example usage:

class MyClass:
    pass