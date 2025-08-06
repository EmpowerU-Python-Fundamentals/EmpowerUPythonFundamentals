import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass
        self.__volume = None
        self.__surface_area = None
        self.__density = None

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_volume(self):
        self.__volume = round(math.pow(self.__radius, 3) * 4 / 3 * math.pi, 5)
        return self.__volume

    def get_surface_area(self):
        self.__surface_area= round(math.pow(self.__radius, 2) * 4 * math.pi, 5)
        return self.__surface_area

    def get_density(self):
        self.__density = round(self.__mass / self.__volume, 5)
        return self.__density


    # @property
    # def radius(self):
    #     return self.__radius
    #
    # @property
    # def mass(self):
    #     return self.__mass
    #
    # @radius.setter
    # def radius(self, value):
    #     self.__radius = value
    #
    # @mass.setter
    # def mass(self, value):
    #     self.__mass = value
