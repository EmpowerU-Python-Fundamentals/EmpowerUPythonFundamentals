import re

def class_name_changer(cls, new_name):
    if not new_name:
        raise TypeError("Cannot be empty.")
    if re.search(r"[^A-Za-z0-9]", new_name):
        raise ValueError("Has non-allowed characters.")
    if not re.match(r"[A-Z]", new_name):
        raise ValueError("Should start from uppercase letter.")
    cls.__name__ = new_name
    
    # assert new_name[0].isupper() and new_name.isalnum()
