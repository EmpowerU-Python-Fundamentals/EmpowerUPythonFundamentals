from math import pi


class Sphere(object):
    def __init__(self, radius=0, mass=0):
        self.radius = float(radius)
        self.mass = float(mass)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4 / 3) * pi * (self.radius**3), 5)

    def get_surface_area(self):
        return round(4 * pi * (self.radius**2), 5)

    def get_density(self):
        if self.mass == 0:
            return 0
        return self.mass / self.get_volume()
