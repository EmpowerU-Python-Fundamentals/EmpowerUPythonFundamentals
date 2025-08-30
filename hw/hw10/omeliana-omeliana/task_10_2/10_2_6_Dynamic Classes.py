def class_name_changer(cls, new_name):
    """Dynamic Classes"""
    if not new_name:
        raise ValueError("Class name cannot be empty!")
    if not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter!")
    if not new_name.isalnum():
        raise ValueError("Class name must contain only legal chars!")
    if new_name[0].isdigit():
        raise ValueError("Class name must start with a letter!")
    cls.__name__ = new_name