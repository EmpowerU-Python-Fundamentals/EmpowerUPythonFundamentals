from animal import Animal

class Reptile(Animal):
    def __init__(self, name: str, species: str, legs: int):
        super().__init__(name, species, legs)

    def make_sound(self):
        return "Hiss"

    def shed_skin(self):
        print(f"{self.name} is shedding its skin.")