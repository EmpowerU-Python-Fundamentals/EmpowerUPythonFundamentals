class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species_info(cls):
        return "Species: Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is a static method."

human = Human("Hryhorii")
print(human.welcome())
print(Human.species_info())
print(Human.arbitrary_message())