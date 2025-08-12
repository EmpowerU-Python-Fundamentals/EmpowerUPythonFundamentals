class Polygon:
    def __init__(self, num_sides: int):
        self.num_sides = num_sides

class Rectangle(Polygon):
    def __init__(self, width: float, height: float):
        super().__init__(4) 
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

#Test:
my_rectangle = Rectangle(5.0, 10.0)
print(f"Прямокутник: ширина = {my_rectangle.width}, висота = {my_rectangle.height}")
print(f"Кількість сторін: {my_rectangle.num_sides}")
print(f"Площа прямокутника: {my_rectangle.get_area():.2f}")