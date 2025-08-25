class MyClass:
    pass


def class_name_changer(cls, new_name):
    """Change the class name to a new name."""
    if new_name.isalnum() and new_name[0].isalpha() and not new_name[0].islower():
        cls.__name__ = new_name
    else:
        raise ValueError(
            "Class name must start with a letter and contain only alphanumeric characters."
        )
    return cls
