# В описі задачі помилка. Фраза "Find the square of a rectangle" не має змісту.
# Розв'язую вважаючи що малася на увазі площа (area)
from typing import override

class Polygon:
    def calc_area() -> float: pass

class Rectangle(Polygon):
    def __init__(self, side_a: float = 0.0, side_b: float = 0.0):
        self.side_a = side_a
        self.side_b = side_b


    @override
    def calc_area(self) -> float:
        return self.side_a * self.side_b
    
# Test
rect = Rectangle(2.4, 5.6)
print(rect.calc_area())