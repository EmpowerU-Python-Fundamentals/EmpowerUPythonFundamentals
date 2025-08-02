"""calculates sphere"""
import math
class Sphere(object):
    """sphere"""
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def get_radius(self):
        """hetting radius

        Returns:
            int: radius
        """
        return self.radius
    def get_mass(self):
        """mass
        Returns:
            int: mass
        """
        return self.mass
    def get_volume(self):
        """getting volume
        Returns:
            int: calculated volume
        """
        self.volume = 4/3 * math.pi * (self.radius ** 3)
        return self.volume
    def get_surface_area(self):
        """calculates surface area
        Returns:
            int: surface area
        """
        return 4 * math.pi * (self.radius ** 2)
    def get_density(self):
        """calculates density
        Returns:
            int: density
        """
        return self.mass/self.volume
