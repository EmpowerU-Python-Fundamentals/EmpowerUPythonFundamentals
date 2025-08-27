class Polygon:
    def __init__(self, S = None):
        self.S = S

class Rectangle(Polygon):
    def square(self,a,b):
        self.S = a * b
        return self.S
    
r = Rectangle()
print(r.square(4,5))


