# import random
# import math

# Створення класів Human, Man та Woman, де Man і Woman є спадкоємцями Human.
# Функція god() має повертати список, що містить об'єкти Man та Woman.
class Human:
    """Базовий клас для людини."""
    pass

class Man(Human):
    """Клас для чоловіка, спадкоємець Human."""
    pass

class Woman(Human):
    """Клас для жінки, спадкоємець Human."""
    pass

def god():
    """
    Створює та повертає список з об'єктів Man та Woman.
    """
    return [Man(), Woman()]

# Приклад використання
creation = god()
print(f"First human: {creation[0].__class__.__name__}")
print(f"Second human: {creation[1].__class__.__name__}")
print("-" * 20)
