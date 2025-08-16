import random
# import math

# Створення класу Ghost, об'єкти якого при ініціалізації отримують
# випадковий колір з певного списку.
class Ghost:
    """
    Класс для моделювання привида з випадковим кольором.
    """
    def __init__(self):
        """
        Ініціалізує об'єкт Ghost і призначає випадковий колір.
        """
        self._color = random.choice(['white', 'yellow', 'purple', 'red'])

    @property
    def color(self):
        """
        Повертає колір привида.
        """
        return self._color

# Приклад використання
ghost1 = Ghost()
ghost2 = Ghost()
print(f"Ghost 1 color: {ghost1.color}")
print(f"Ghost 2 color: {ghost2.color}")
print("-" * 20)
