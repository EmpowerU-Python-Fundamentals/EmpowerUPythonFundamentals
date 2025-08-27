def rename_class(cls, new_name: str):

    if not (new_name and new_name[0].isupper() and new_name.isalnum()):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")

    
    cls.__name__ = new_name
    return cls

class MyClass:
    pass

print(MyClass.__name__)
rename_class(MyClass, "UsefulClass")
print(MyClass.__name__)
rename_class(MyClass, "SecondUsefulClass")
print(MyClass.__name__)

# rename_class(MyClass, "badName!")
