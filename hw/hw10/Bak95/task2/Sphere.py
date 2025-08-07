import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4/3) * math.pi * self.radius**3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

ball = Sphere(2, 50)
print("Радіус:", ball.get_radius())
print("Маса:", ball.get_mass())
print("Об’єм:", ball.get_volume())
print("Площа поверхні:", ball.get_surface_area())
print("Густина:", ball.get_density())
