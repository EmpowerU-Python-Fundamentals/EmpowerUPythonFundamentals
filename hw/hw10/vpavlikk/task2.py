class Human:
    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        print(f"Welcome, {self.name}")

    def species(self):
        print(f"{self.name} is a species of homosapiens")

    @staticmethod
    def arbitraty_msg():
        print("arbitraty message")


person = Human("Jack")
person.welcome_msg()
person.species()

Human.arbitraty_msg()
