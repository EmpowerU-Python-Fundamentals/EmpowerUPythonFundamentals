# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# Arguments for the constructor
#   radius -> integer or float (do not round it)
#   mass -> integer or float (do not round it)
# Methods to be defined
#   get_radius()       =>  radius of the Sphere (do not round it)
#   get_mass()         =>  mass of the Sphere (do not round it)
#   get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
#   get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
#   get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

from math import pi, pow

class Sphere(object):
    def __init__(self, radius: float, mass: float):
        self._radius_ = radius
        self._mass_ = mass
    
    def get_radius(self):
        return self._radius_

    def get_mass(self):
        return self._mass_
    
    def get_volume(self):
        raw_volume = 4. / 3. * pi * pow(self.get_radius(), 3)
        return round(raw_volume, 5)
    
    def get_surface_area(self):
        raw_area = pi * 4 * pow(self.get_radius(), 2)
        return round(raw_area, 5)
    
    def get_density(self):
        raw_density = self.get_mass() / self.get_volume()
        return round(raw_density, 5)