class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello, {self.name}"
    
    @staticmethod
    def species():
        return "Homosapiens"
    
    @staticmethod
    def message():
        return "Random thing"

human = Human("Danil-Shevchenko")
print(human.hello())
print(human.species())
print(human.message())