from math import pi

class Sphere():
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = 4 / 3 * pi * self.radius ** 3
        return round(volume, 5)
    
    def get_surface_area(self):
        surface_area = 4 * pi * self.radius ** 2
        return round(surface_area, 5)
    
    def get_density(self):
        density = self.mass / (4 / 3 * pi * self.radius ** 3)
        return round(density, 5)
    