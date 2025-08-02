class Animal:
    def __init__(self, name: str, species: str, legs: int):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")