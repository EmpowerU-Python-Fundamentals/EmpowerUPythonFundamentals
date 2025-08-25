def class_name_changer(cls, new_name):
    if not (new_name and new_name[0].isupper() and new_name.isalnum()):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    cls.__name__ = new_name
    return cls
