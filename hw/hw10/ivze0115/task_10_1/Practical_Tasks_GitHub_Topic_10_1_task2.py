class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def general_info():
        return "Homo sapiens are originating in Africa roughly 300,000 years ago"


if __name__ == '__main__':
    H=Human('Mykola')
    H.welcome()
    print(H.get_species())
    print(H.general_info())
