import math
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def volume(self):
        return round((4/3) * math.pi * self.radius**3, 5)

    def surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)

    def density(self):
        return round(self.mass / self.volume(), 5)

ball = Sphere(2,50)

print(f"Radius: {ball.radius}")
print(f"Mass: {ball.mass}")
print(f"Volume: {ball.volume()}")
print(f"Surface Area: {ball.surface_area()}")
print(f"Density: {ball.density()}")
