import math

class Sphere:
    def __init__(self, radius: float, mass: float):
        self.radius = radius
        self.mass = mass

    def get_radius(self) -> float:
        return self.radius

    def get_mass(self) -> float:
        return self.mass

    def get_volume(self) -> float:
        volume = (4 / 3) * math.pi * (math.pow(self.radius,3))
        return round(volume, 5)

    def get_surface_area(self) -> float:
        surface_area = 4 * math.pi * (math.pow(self.radius, 2))
        return round(surface_area, 5)

    def get_density(self) -> float:
        volume = self.get_volume()
        density = self.mass / volume
        return round(density, 5)
