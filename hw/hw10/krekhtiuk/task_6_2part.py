def rename_class(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid name")
    cls.__name__ = new_name
    return cls 

