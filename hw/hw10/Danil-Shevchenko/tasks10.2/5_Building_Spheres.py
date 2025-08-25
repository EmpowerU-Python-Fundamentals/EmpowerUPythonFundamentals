import math
class Sphere(object):
    def __init__(self, radius, mass): 
        self.__radius = radius
        self.__mass = mass
    def get_radius(self):
        return self.__radius
    def get_mass(self):
        return self.__mass
    def get_volume(self):
        return round((4/3)*math.pi*math.pow(self.__radius,3),5)
    def get_surface_area(self):
         return round(4*math.pi*math.pow(self.__radius,2),5)
    def get_density(self):
        return round(self.__mass/self.get_volume(),5)