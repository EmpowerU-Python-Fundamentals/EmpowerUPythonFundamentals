class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = []
        for _ in range(num_sides):
            self.sides.append(0)

    def set_sides(self, sides_length):
        if self.num_sides != len(sides_length):
            print ("The number of sides does not match")
        else:
            for side in sides_length:
                if side <=0:
                    print ("All lengths must be positive")
                else:
                    self.sides = sides_length

    def get_sides(self): 
        return self.sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.set_sides([width, height, width, height])

    def area(self):
        return self.get_sides()[0]*self.get_sides()[1]


a = Rectangle(4, 5)
print(a.area())