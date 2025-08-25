class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привіт, {self.name}!")

    @classmethod
    def get_species(cls):
        print(f"Людина належить до виду {cls.species}")

    @staticmethod
    def message():
        print("Залишайтеся добрими та допитливими!")

person = Human("Олена")
person.greet()
Human.get_species()
Human.message()
