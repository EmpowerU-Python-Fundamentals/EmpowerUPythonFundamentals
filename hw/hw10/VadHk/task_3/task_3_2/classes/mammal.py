from animal import Animal

class Mammal(Animal):
    def __init__(self, name: str, species: str, legs: int):
        super().__init__(name, species, legs)

    def make_sound(self):
        return "Roar"

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")