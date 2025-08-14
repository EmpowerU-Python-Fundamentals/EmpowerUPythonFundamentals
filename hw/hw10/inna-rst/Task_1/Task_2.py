class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greeting_message(self):
        print(f"Hello {self.name}!")

    @classmethod
    def get_species(cls):
        print(f"We are  {cls.species}")

    @staticmethod
    def get_info_mammal():
        print("Human is mammal")

if __name__ == '__main__':
    human = Human("Peter")
    human.greeting_message()
    Human.get_species()
    Human.get_info_mammal()