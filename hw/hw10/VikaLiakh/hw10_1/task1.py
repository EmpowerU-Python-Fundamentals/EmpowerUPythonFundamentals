class Polygon():
    def __init__ (self, n: int):
        self.n = n
        self.sides = []
        
    def input_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__ (self):
        super().__init__ (2)
            
    def area (self):
        return self.sides[0]* self.sides[1]
        
rect1 = Rectangle()
rect1.input_sides()
area_of_rect1 = rect1.area()
print("Area of rectangle:", area_of_rect1)