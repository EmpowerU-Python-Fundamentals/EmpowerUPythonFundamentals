def class_name_changer(cls, new_name):
    if not new_name or not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name. Must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name
    return cls
