# import random
# import math

# Створення класу Ball, який приймає один необов'язковий аргумент "ball type".
# Якщо аргумент не надано, тип м'яча за замовчуванням "regular".
class Ball:
    """
    Класс для моделювання м'яча з типом.
    """
    def __init__(self, ball_type="regular"):
        """
        Ініціалізує об'єкт Ball.

        Args:
            ball_type (str): Тип м'яча (за замовчуванням "regular").
        """
        self._ball_type = ball_type

    @property
    def ball_type(self):
        """
        Повертає тип м'яча.
        """
        return self._ball_type

# Приклад використання
ball1 = Ball()
ball2 = Ball('super')
print(f"Ball 1 type: {ball1.ball_type}")
print(f"Ball 2 type: {ball2.ball_type}")
print("-" * 20)
