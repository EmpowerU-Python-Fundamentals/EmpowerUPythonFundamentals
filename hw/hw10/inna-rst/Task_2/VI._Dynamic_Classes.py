import re

def change_class_name(cls, new_name):
    if not isinstance(new_name, str):
        raise ValueError("Class name must be a string")

    if not new_name:
        raise ValueError("Class name cannot be empty")

    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError("Class name must start with uppercase letter and contain only alphanumeric characters")

    cls.__name__ = new_name
    cls.__qualname__ = new_name
    return cls


if __name__ == "__main__":
    class MyClass:
        pass

    class A333sdf44:
        def __str__(self):
            return "Help"

    myObject = MyClass()
    print(id(myObject), type(myObject))
    change_class_name(MyClass, "A333sdf44")
    print(id(myObject), type(myObject))
    # change_class_name(MyClass, "9000")