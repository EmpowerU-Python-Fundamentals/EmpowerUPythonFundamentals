class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."
