import math

class Sphere(object):
    def __init__(self, radius, mass):
        if isinstance(radius, int) or isinstance(radius, float):
            self.radius = radius
        if isinstance(mass, int) or isinstance(mass, float):
            self.mass = mass
            
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = 4/3*math.pi*pow(self.radius, 3)
        return round( volume ,5)
    
    def get_surface_area(self):
        surface_area = 4*math.pi*pow(self.radius, 2)
        return round(surface_area ,5)
        
    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density ,5)
    

