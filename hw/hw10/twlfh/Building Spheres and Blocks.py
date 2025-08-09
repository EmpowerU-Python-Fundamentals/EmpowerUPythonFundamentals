from math import pi


class Block:
    def __init__(self, lst):
        self.lst = lst

    def get_width(self):
        return self.lst[0]
    def get_length(self):
       return self.lst[1]
    def get_height(self):
        return self.lst[2]
    def get_volume(self):
        return self.lst[0] * self.lst[1] * self.lst[2]
    def get_surface_area(self):
        return 2 * (self.lst[0] * self.lst[1] + self.lst[0] * self.lst[2] + self.lst[1] * self.lst[2])

data = [2,4,6]
b = Block(data)

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4/3) * pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

s = Sphere(2, 50)


