from animal import Animal

class Bird(Animal):
    def __init__(self, name: str, species: str, legs: int):
        super().__init__(name, species, legs)

    def make_sound(self):
        return "Squawk"

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")