def class_name_changer(cls, new_name: str):
    if not isinstance(new_name, str):
        print ("Class name must be a string.")

    if not new_name or not new_name[0].isupper() or not new_name.isalnum():
        print ("Class name must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name
    return cls
