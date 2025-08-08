class Polygon():
    def __init__(self,sides):
        self.sides = sides
        if isinstance(sides, list) and all(isinstance(side, (int, float)) and side > 0 for side in sides):
            self.sides = sides
        print(f"Poligon sides incapsulate from rectangle : {self.sides}")
        return self.sides

class Rectangle(Polygon):
    def __init__(self):
        a = int(input("Input side a for recrtangle:  "))
        b = int(input("Input side b fore rectangle:  "))
        if a >= 0 and b >= 0:
            super().__init__([a, b, a, b])
        else:
            raise ValueError ("Sides must be none negative")

    
    def find_area(self):
        return self.sides[0] * self.sides[1]

if __name__ == "__main__":
    try:
        rectangle = Rectangle()
        print(f"The square of rectangle = {rectangle.find_area()}")
    except ValueError as e:
        print(f"Error:{e}")