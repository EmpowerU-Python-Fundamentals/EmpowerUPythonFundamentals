class Polygon:
    def __init__(self, name="Багатокутник"):
        self.name = name
        
    def square(self):
        print(f"Обчислення площі для фігури: {self.name}")
    
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(name="Прямокутник")
        self.length=length
        self.width=width
        
    def square(self):
        print(f"Обчислення площі для фігури: {self.name}")
        return self.length * self.width
    
my_obj_rectangle = Rectangle(4,6)
print(f"{my_obj_rectangle.name}: площа = {my_obj_rectangle.square()}")