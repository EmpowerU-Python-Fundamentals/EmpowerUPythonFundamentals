"""My way of solving task 5"""
import math


class Sphere:
    """Base class: Sphere"""
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        """Return value for sphere's radius"""
        return self.radius

    def get_mass(self):
        """Return value for sphere's mass"""
        return self.mass

    def get_volume(self):
        """Return value for sphere's volume"""
        volume = (4/3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        """Return value for sphere's surface area"""
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        """Return value for sphere's density"""
        volume = (4/3) * math.pi * self.radius**3
        density = self.mass / volume
        return round(density, 5)
