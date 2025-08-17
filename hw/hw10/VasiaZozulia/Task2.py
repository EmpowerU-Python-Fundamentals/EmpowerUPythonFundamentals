class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "This is a static method."