# import random
# import math

# Функція, яка дозволяє змінювати ім'я класу,
# але тільки якщо нове ім'я є допустимим ідентифікатором.
def class_name_changer(cls, new_name: str):
    """
    Змінює ім'я класу, якщо нове ім'я є валідним ідентифікатором.

    Args:
        cls (class): Клас, ім'я якого потрібно змінити.
        new_name (str): Нове ім'я класу.

    Raises:
        ValueError: Якщо нове ім'я не є валідним.
    """
    if not isinstance(new_name, str) or not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError("New class name must be an alphanumeric string starting with an uppercase letter.")
    cls.__name__ = new_name
    return cls

class MyClass:
    """Початковий клас."""
    pass

# Приклад використання
my_obj = MyClass()
print(f"Initial class name: {my_obj.__class__.__name__}")

try:
    class_name_changer(MyClass, 'Super')
    print(f"New class name: {my_obj.__class__.__name__}")
    
    # Спроба змінити на невалідну назву
    class_name_changer(MyClass, 'wrong_name')
except ValueError as e:
    print(f"Caught error: {e}")
