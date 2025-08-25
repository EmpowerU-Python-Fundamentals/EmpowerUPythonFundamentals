class MyClass:
    pass


def change_class_name(cls, name: str):
    if name[0].islower():
        raise ValueError("Class name must start with an uppercase letter.")
    if not name.isalnum():
        raise ValueError("Class name must contain only alphanumeric characters.")

    cls.__name__ = name
    return cls


if __name__ == '__main__':
    print(MyClass.__name__)

    change_class_name(MyClass, "UsefulClass")
    print(MyClass.__name__)
