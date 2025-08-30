"""My way of solving task 2"""


class Human:
    """Base class: Human"""
    species = "Homosapiens"  # species info

    def __init__(self, name):
        self.name = name    # person's name

    def greet(self):
        print(f"Привіт, {self.name}! Радий тебе бачити.")   # greeting

    @classmethod
    def get_species(cls):
        return f"Це вид: {cls.species}"     # return speies info

    @staticmethod
    def random_message():
        return "Життя — це подорож, а не пункт призначення."    # return arbitrary message
