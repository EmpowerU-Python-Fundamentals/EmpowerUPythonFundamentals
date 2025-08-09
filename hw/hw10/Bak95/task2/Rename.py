def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Неправильне ім’я класу. Воно повинно починатися з великої літери та містити лише літери та цифри.")
    cls.__name__ = new_name
    return cls

class MyClass:
    pass

MyClass = class_name_changer(MyClass, "SecondUsefulClass")
print("Нове ім’я класу:", MyClass.__name__)
