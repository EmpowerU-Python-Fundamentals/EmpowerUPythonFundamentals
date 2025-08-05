class Human():
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Welcome {self.name}")
    @classmethod
    def species_type(cls):
        return "Homosapiens"
    @staticmethod
    def message():
        return "Message"