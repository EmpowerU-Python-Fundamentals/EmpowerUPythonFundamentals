class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is a static method message."