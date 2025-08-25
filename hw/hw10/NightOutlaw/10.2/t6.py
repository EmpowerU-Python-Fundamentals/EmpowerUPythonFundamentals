"""My way of solving task 6"""


class MyClass:
    """Base class: MyClass"""
    pass


def rename_class(cls, new_name):
    """Rename the given class"""
    if not isinstance(new_name, str):
        raise TypeError("Назва класу має бути рядком.")

    if not new_name:
        raise ValueError("Назва класу не може бути порожньою.")

    if not new_name[0].isupper():
        raise ValueError("Назва класу має починатися з великої літери.")

    if not new_name.isalnum():
        raise ValueError("Назва класу має містити лише літери та цифри.")

    cls.__name__ = new_name
    return cls


# Перейменування на UsefulClass
rename_class(MyClass, "UsefulClass")
print(MyClass.__name__)  # Виведе: UsefulClass

# Перейменування на SecondUsefulClass
rename_class(MyClass, "SecondUsefulClass")
print(MyClass.__name__)  # Виведе: SecondUsefulClass
