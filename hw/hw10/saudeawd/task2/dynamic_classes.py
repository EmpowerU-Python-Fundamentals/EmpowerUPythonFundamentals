def class_name_changer(cls, new_name):
    if not new_name:
        raise ValueError("Class name cannot be empty")
    first_char = new_name[0]
    if not (first_char >= 'A' and first_char <= 'Z'):
        raise ValueError("Class name must start with an uppercase letter")
    for char in new_name[1:]:
        if not (char >= 'a' and char <= 'z') and \
           not (char >= 'A' and char <= 'Z') and \
           not (char >= '0' and char <= '9'):
            raise ValueError("Class name can only contain alphanumeric characters")
    cls.__name__ = new_name
