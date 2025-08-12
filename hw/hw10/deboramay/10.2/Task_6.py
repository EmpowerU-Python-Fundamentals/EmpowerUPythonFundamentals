#Python's Dynamic Classes

def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise Exception("Invalid class name")
    cls.__name__ = new_name

#Test:
class MyClass:
    pass

myObject = MyClass()
print(MyClass.__name__, "MyClass")

class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__, "UsefulClass")

class_name_changer(MyClass, "SecondUsefulClass")
print(MyClass.__name__, "SecondUsefulClass")