# import random
# import math

# Створення класу Person, який приймає ім'я та вік,
# і має властивість `info`, що повертає відформатований рядок.
class Person:
    """
    Клас для представлення людини з ім'ям, віком та інформаційним рядком.
    """
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._info = f"{name}'s age is {age}"

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @property
    def info(self):
        """
        Повертає інформаційний рядок про людину.
        """
        return self._info

# Приклад використання
person = Person('John', 34)
print(f"Person info: {person.info}")
print("-" * 20)
