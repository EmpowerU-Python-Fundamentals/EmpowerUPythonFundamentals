class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.__info= f"{name}s age is #{age}"

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, value):
        self.__info = value