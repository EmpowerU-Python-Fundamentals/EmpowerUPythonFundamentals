class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return "This is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary static message."

person1 = Human("Mia")
print(person1.welcome_message())
print(Human.get_species())
print(Human.arbitrary_message())
