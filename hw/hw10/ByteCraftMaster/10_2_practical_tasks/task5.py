import math

class Sphere():
    def __init__(self, radius, mass):
        self.radius= radius
        self.mass=mass
        
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(4/3*math.pi*math.pow(self.radius, 3), 5)
    def get_surface_area(self):
        return round(4*math.pi*self.radius*self.radius, 5)
    def get_density(self):
        return round(self.mass/(4/3*math.pi*math.pow(self.radius, 3)), 5)