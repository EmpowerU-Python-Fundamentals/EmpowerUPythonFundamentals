class Polygon():
    def __init__(self, *args):
        if not args:
            raise ValueError("Provide at list one pargument as a side.")
        try:
            self.sides = [float(el) for el in args]
        except (TypeError, ValueError) as e:
            exit(f"Error: {e}\nProvide numerical values.")


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height
    

# Test    
rect = Rectangle(28.07, 4.0123)
print(f"Area of rectangle is {rect.area}.")