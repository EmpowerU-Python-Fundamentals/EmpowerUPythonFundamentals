class Human:
    species = "Homosapiens" # class attribute

    def __init__(self, name):
        self.name = name

    # instance method
    def welcome(self):
        print(f"Hellow, {self.name}! ")

    # class method
    @classmethod
    def get_species(cls):
        return f"Вид: {cls.species}"

    # static method
    @staticmethod
    def message():
        return "Good Luck!!!."

person1 = Human("Adam")
person2 = Human("Eva")

person1.welcome()
person2.welcome()

print(Human.get_species())
print(Human.message())