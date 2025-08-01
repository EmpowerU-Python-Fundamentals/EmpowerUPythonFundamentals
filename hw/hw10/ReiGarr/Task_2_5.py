import math

class Sphere:
    def __init__(self, radius, mass):
        self._radius = radius
        self._mass = mass

    def get_radius(self):
        return self._radius

    def get_mass(self):
        return self._mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self._radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self._radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        volume = (4/3) * math.pi * (self._radius ** 3)
        density = self._mass / volume
        return round(density, 5)