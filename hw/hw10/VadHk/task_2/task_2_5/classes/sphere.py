class Sphere:
    def __init__(self, radius: float, mass: float):
        self._radius = radius
        self._mass = mass

    def get_volume(self):
        return (4/3) * 3.141592653589793 * (self._radius ** 3)

    def get_surface_area(self):
        return 4 * 3.141592653589793 * (self._radius ** 2)
    
    def get_density(self):
        volume = self.get_volume()
        if volume == 0:
            return 0
        return self._mass / volume
    
    def get_radius(self):
        return self._radius
    
    def get_mass(self):
        return self._mass