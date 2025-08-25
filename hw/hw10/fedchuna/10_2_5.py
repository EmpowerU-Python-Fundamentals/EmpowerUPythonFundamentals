import math


class Sphere(object):
    def __init__(self,r, m):
        self.m = m
        self.r = r
    def get_radius(self):
        return self.r
    def get_mass(self):
        return self.m
    def get_volume(self):
        V = (4/3)*math.pi*self.r**3
        V = round(V,5)
        return V
    def get_surface_area(self):
        s = 4*math.pi*self.r**2
        s = round(s,5)
        return s
    def get_density(self):
        p = self.m/((4/3)*math.pi*self.r**3)
        p = round(p,5)
        return p
    
ball = Sphere(0.11, 19.61)

ball.get_radius()
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_density()