import math

class Sphere(object):
    def __init__(self, radius , mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        """Return the volume of the Sphere (rounded to 5 decimal places)."""
        # Volume formula: V = (4/3) * π * r³
        return round(4/3 * math.pi * self.radius**3, 5)

    def get_surface_area(self):
        """Return the surface area of the Sphere (rounded to 5 decimal places)."""
        # Surface area formula: A = 4 * π * r²
        return round(4 * math.pi * self.radius**2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)