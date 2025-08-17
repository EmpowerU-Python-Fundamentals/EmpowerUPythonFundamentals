class Polygon():
    pass

class Rectangle(Polygon):
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    @property
    def area(self):
        return self.side_a*self.side_b

print("Write sides for rectangle:")
a = float(input("side a = "))
b = float(input("side b = "))
figure = Rectangle(a,b)
print(f"Area = {figure.area}")