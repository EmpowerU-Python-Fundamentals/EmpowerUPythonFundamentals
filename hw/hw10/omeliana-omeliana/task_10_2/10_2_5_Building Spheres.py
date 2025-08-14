import math

class Sphere(object):
    """
    Building Spheres
    """
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)
        
    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        density = self.mass / volume
        return round(density, 5)