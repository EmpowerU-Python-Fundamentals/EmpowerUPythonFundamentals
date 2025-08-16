class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Welcome {self.name}!")

    @classmethod
    def which_species(cls):
        print("Homosapiens")

    @staticmethod
    def message():
        print("This is static method")
