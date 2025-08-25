#VI. Dynamic Classes

def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name
    return cls

class MyClass:
    pass

class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)  # Output: "UsefulClass"

class_name_changer(MyClass, "SecondUsefulClass")
print(MyClass.__name__)  # Output: "SecondUsefulClass"
