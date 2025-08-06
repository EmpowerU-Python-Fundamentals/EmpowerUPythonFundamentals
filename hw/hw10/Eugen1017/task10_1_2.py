class Human:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_value):
        self.__name = name_value

    def greeting(self):
        print(f"Hello, {self.name}")

    @classmethod
    def get_species(cls):
        return "Homosapiens"

    @staticmethod
    def show_default_msg():
        print("Hello, world!")